# /usr/bin/python
# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from designer.forms import UserForm, ProjectForm, StatementForm
from .models import User, Project, Statement
from django.contrib.auth.backends import ModelBackend

from django.http import HttpResponse
from django.template.loader import get_template
import pdfkit

from django.contrib.auth.views import LoginView

# from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

from urllib.parse import unquote


# Create your views here.
def home(request):
	return redirect(authapp_home)


# вход
@login_required(login_url='/designer/sign_in')
def authapp_home(request):
	all_project = Project.objects.filter(user=request.user.pk)
	return render(request, 'designer/projects.html', {'all_project': all_project})


def login_in(request):
	print(request.method)
	print(request.POST)
	return HttpResponse(LoginView.as_view(template_name='designer/sign_in.html'))


# Регистрация/вход
def authapp_sign_up(request):
	user_form = UserForm()
	# 'username', 'email'
	if request.method == 'POST':
		# profile_form = ProfileForm(request.POST, request.FILES)
		username = {'username': str(request.POST.__getitem__('email')).lower(),
		            'email': str(request.POST.__getitem__('email')).lower()}

		response = request.POST.copy()
		response.update(username)
		print(response)

		user_form = UserForm(response)
		if user_form.is_valid():
			User.objects.create_user(**user_form.cleaned_data)

			user = authenticate(
				username=user_form.cleaned_data['email'],
				password=user_form.cleaned_data['password']
			)

			login(request, user)
			EmailAuthBackend.authenticate(request, user_form.cleaned_data['email'], user_form.cleaned_data['password'])

			return redirect(authapp_home)

	return render(request, 'designer/sign_up.html', {
		'user_form': user_form,
	})


# Создаем новый проект
def new_project(request):
	if request.method == 'POST':
		user = {'user': str(request.user.pk)}
		response = request.POST.copy()
		response.update(user)

		# print("response", response)
		# print('response.__getitem__(name)', response.__getitem__('name'))
		# name_project = {'name': response.__getitem__('name').encode('utf8')}
		# response.pop('name')
		# print("response", response)
		# response.update(name_project)

		# create_project.update({request.user.pk: response.__getitem__('name')})
		# project_name = create_project.get(request.user.pk)

		project_form = ProjectForm(response)

		if response.__getitem__('name'):
			user_id = request.user.pk
			project_name = response.__getitem__('name')

			if exiting_project(user_id, project_name) == []:
				if project_form.is_valid():
					# new_project = project_form.save(commit=False)
					# creator = request.user
					# new_project.user = creator
					project_form.save()
					return redirect(f'/designer/statement/{project_name}')
				else:
					print(project_form.errors)
			else:
				return HttpResponse('Such project with the name have alredy exite')
	else:
		return redirect(authapp_home)


# Проверка на сущестование проекта, чтобы исключить дублирование проетков.
def exiting_project(user_id, project_name):
	try:
		project = Project.objects.get(user=user_id, name=project_name)
	except Exception as e:
		print('e', e)
		project = []
	return project


# Функция для входа на платформу через почту
class EmailAuthBackend(ModelBackend):
	def authenticate(self, request, username=None, password=None, **kwargs):
		if '@' in username:
			kwargs = {'email': username}
		else:
			kwargs = {'username': username}

		try:
			user = User.objects.get(**kwargs)
			if user.check_password(password):
				return user
			else:
				return None
		except User.DoesNotExist:
			return None

	def get_user(self, user_id):
		try:
			return User.objects.get(pk=user_id)
		except User.DoesNotExist:
			return None


# Функция для работы с таблицей ведомости
def statement(request, project_name):

	if request.method == 'POST':
		statement_data = request.POST.copy()

		# if request.FILES.getlist('images'):
		# 	print(request.FILES.getlist('images')[0].name)
		# 	print(type(request.FILES.getlist('images')[0].name))
		# 	request.FILES.getlist('images')[0].name = str(request.FILES.getlist('images')[0].name).encode(
		# 		'utf8').decode('utf8')
		#
		# if request.FILES.getlist('file_3dmax'):
		# 	print(request.FILES.getlist('file_3dmax')[0].name)
		# 	print(type(request.FILES.getlist('file_3dmax')[0].name))
		# 	request.FILES.getlist('file_3dmax')[0].name = str(request.FILES.getlist('file_3dmax')[0].name).encode(
		# 		'utf8').decode('utf8')
		#
		# if request.FILES.getlist('file_revit'):
		# 	print(request.FILES.getlist('file_revit')[0].name)
		# 	print(type(request.FILES.getlist('file_revit')[0].name))
		# 	request.FILES.getlist('file_revit')[0].name = str(request.FILES.getlist('file_revit')[0].name).encode(
		# 		'utf8').decode('utf8')
		#
		# if request.FILES.getlist('file_technical_instruction'):
		# 	print(request.FILES.getlist('file_technical_instruction')[0].name)
		# 	print(type(request.FILES.getlist('file_technical_instruction')[0].name))
		# 	request.FILES.getlist('file_technical_instruction')[0].name = str(
		# 		request.FILES.getlist('file_technical_instruction')[0].name).encode('utf8').decode('utf8')

		total_client_price = int(statement_data.__getitem__('retail_price')) * int(statement_data.__getitem__('qty'))
		project_id = {'project': get_project_id(project_name, request.user), 'total_client_price': total_client_price}

		statement_data.update(project_id)
		statement_form = StatementForm(statement_data, request.FILES)

		if statement_form.is_valid():
			statement_form.save()

		return get_project_statement(request, int(statement_data.get('project')))
	return get_project_statement(request, project_name)


# Функция для проверки и получения id проекта
def get_project_id(project_name, user=None):
	if type(project_name)==type("str"):
		try:
			# project_name = unquote(unquote(unquote(project_name)))
			return Project.objects.get(name=project_name, user=user).id
		except Exception as e:
			return HttpResponse(e)
	elif type(project_name)==type(1):
		return project_name
	return 'Error, nut such project name'


# func to get the project statement)
def get_project_statement(request, project_name):
	try:
		project_id = get_project_id(project_name, request.user)
		project = Statement.objects.filter(project=project_id)

		total_money = 0
		for row in project:
			total_money += row.total_client_price

		statement_form = StatementForm()
		return render(request, 'designer/statement.html', {
					'statement_form': statement_form,
					'statement': project,
					'total_money': total_money,
				})
	except Exception as e:
		print('e', e)
		return redirect(authapp_home)


# fun for to del the statement row
def delete_statement_row(request, project_name, row):
	if request.method == 'GET':
		if row != None:
			try:
				project_id = Statement.objects.get(id=row).project
				print('project_id', project_id)
				Statement.objects.filter(id=row).delete()
			except Exception as e:
				print(e)
		# return get_project_statement(request, project_name)
		return redirect(f'/designer/statement/{project_name}')

	if request.method == 'POST':
		return statement(request, project_name)


# Функция для генерации пдф
def generate_pdf(request, project_name):
		project_id = get_project_id(project_name, request.user)
		project = Statement.objects.filter(project=project_id)
		template = get_template('designer/pdf_statement.html')

		html = template.render({'project': project})
		print('in generate_pdf html', html)
		options = {
		    'page-size': 'Letter',
		    'margin-top': '0.75in',
		    'margin-right': '0.75in',
		    'margin-bottom': '0.75in',
		    'margin-left': '0.75in',
		    'encoding': "UTF-8",
		    'no-outline': None
		}

		# config = pdfkit.configuration(wkhtmltopdf="D:\\Programs\\Python38-32\\lib\\site-packages\\wkhtmltopdf")
		# config = pdfkit.configuration(wkhtmltopdf="D:\\wkhtmltopdf\\bin")

		name = 'statement_pdf_1'
		pdf = pdfkit.from_string(html, name, options=options)
		print('in generate_pdf  pdf', pdf)
		with open(name, 'rb') as f:
			pdf = f.read()
			response = HttpResponse(pdf, content_type='application/pdf')
			response['Content-Disposition'] = 'attachment; filename=report.pdf'
			# os.remove(name)
		return response





# from django.http import HttpResponse
# from django.template.loader import render_to_string
# from weasyprint import HTML
# import tempfile
#
# def generate_pdf(request, project_name):
# 	"""Создание pdf."""
# 	# Данные модели
# 	project_id = get_project_id(project_name)
# 	project = Statement.objects.filter(project=project_id)
#
# 	# Обработка шаблона
# 	html_string = render_to_string('designer/pdf_statement.html', {'project': project})
# 	html = HTML(string=html_string)
# 	result = html.write_pdf()
#
# 	# Создание http ответа
# 	response = HttpResponse(content_type='application/pdf;')
# 	response['Content-Disposition'] = 'inline; filename=list_people.pdf'
# 	response['Content-Transfer-Encoding'] = 'binary'
# 	with tempfile.NamedTemporaryFile(delete=True) as output:
# 		output.write(result)
# 		output.flush()
# 		output = open(output.name, 'r')
# 		response.write(output.read())
#
# 	return response


		# pdf = HttpResponse(pdf.getvalue(), content_type='application/pdf')


		# try:
		#
		# 	if pdf:
		# 		response = HttpResponse(pdf, content_type='application/pdf')
		#
		# 		filename = "%s%s.pdf" % (name, "12341231")
		# 		content = "inline; filename='%s'" % (filename)
		# 		download = request.GET.get("download")
		# 		if download:
		# 			content = "attachment; filename='%s'" % (filename)
		# 		response['Content-Disposition'] = content
		# 		return response
		# 	# return HttpResponse("Not found")
		# except Exception as e:
		# 	return HttpResponse(str(e), status=500)


		# response = HttpResponse(pdf, content_type='application/pdf')
		# response['Content-Disposition'] = 'attachment filename = "statement.pdf"'
		# return response

	# def get(self, request, project_name, *args, **kwargs):
		# try:

		# 	# template = get_template('designer/pdf_statement.html')
		# 	# print('project_name in the class generatePDF', project_name)
		# 	project_id = get_project_id(project_name)
		# 	print('project_id', project_id)
		# 	project = Statement.objects.filter(project=project_id)
		# 	print('project', project)
		# 	context = {
		# 		'project': project,
		# 		'pagesize': 'A4',
		# 	}
		# 	print('context', context)
		# 	# html = template.render(context)
		# 	# print('html', html)
		# 	pdf = render_to_pdf('designer/pdf_statement.html', context)
		# 	print('pdf', pdf)
		# 	if pdf:
		# 		response = HttpResponse(pdf, content_type='application/pdf')
		# 		filename = "statement_%s.pdf" % ("12341231")
		# 		content = "inline; filename='%s'" % (filename)
		# 		download = request.GET.get("download")
		# 		if download:
		# 			content = "attachment; filename='%s'" % (filename)
		# 		response['Content-Disposition'] = content
		# 		return response
		# 	# return HttpResponse("Not found")
		# except Exception as e:
		# 	return HttpResponse(str(e), status=500)


#
# from django.conf import settings
# from easy_pdf.views import PDFTemplateView
#
#
# class PDFView(PDFTemplateView):
# 	template_name = 'designer/pdf_statement.html'
#
# 	base_url = 'file://' + settings.STATIC_ROOT
# 	download_filename = 'pdf_statement.pdf'
#
# 	def get_context_data(self, **kwargs):
# 		return super(PDFView, self).get_context_data(
# 			pagesize='A4',
# 			title='Statement',
# 			**kwargs
# 		)

# from django.http import HttpResponse
# from django.template.loader import render_to_string
# from weasyprint import HTML
# import tempfile
#
# def generate_pdf(request, project_name):
# 	"""Создание pdf."""
# 	# Данные модели
# 	project_id = project_name
# 	if type(project_name) == type("str"):
# 		project_id = Project.objects.get(name=project_name).id
#
# 	project = Statement.objects.filter(project=project_id)
#
# 	# people = Statement.objects.all().order_by('last_name')
#
# 	# Обработка шаблона
# 	html_string = render_to_string('designer/pdf_statement.html', {'project': project})
# 	html = HTML(string=html_string)
# 	result = html.write_pdf()
#
# 	# Создание http ответа
# 	response = HttpResponse(content_type='application/pdf;')
# 	response['Content-Disposition'] = 'inline; filename=project_statement.pdf'
# 	response['Content-Transfer-Encoding'] = 'binary'
# 	with tempfile.NamedTemporaryFile(delete=True) as output:
# 		output.write(result)
# 		output.flush()
# 		output = open(output.name, 'r')
# 		response.write(output.read())
#
# 	return response

# class GeneratePdf(APIView):
# 	def post(self, request, *args, **kwargs):
# 		pdf = render_to_pdf('invoice.html', request.data)
# 		if pdf:
# 			response = HttpResponse(pdf, content_type='application/pdf')
# 			filename = "Invoice_%s.pdf" % "12341231"
# 			content = "inline; filename='%s'" % filename
# 			download = request.GET.get("download")
# 			if download:
# 				content = "attachment; filename='%s'" % filename
# 			response['Content-Disposition'] = content
# 			return response
# 		return HttpResponse("Not found")
# send id
# project
# dele
# ret
