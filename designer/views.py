from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from designer.forms import UserForm, ProjectForm, StatementForm
from .models import User, Project, Statement
from django.contrib.auth.backends import ModelBackend

# from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

# from .tebles import Statement as teble_statement
# Create your views here.


def home(request):
	# return render(request, 'designer/sign_in.html', {})
	print(request.POST)
	print(request.GET)
	return redirect(authapp_home)


# вход
@login_required(login_url='/designer/sign_in')
def authapp_home(request):
	all_project = Project.objects.filter(user=request.user.pk)
	print(all_project)
	return render(request, 'designer/projects.html', {'all_project': all_project})


# Регистрация/вход
def authapp_sign_up(request):
	print(request.POST)
	user_form = UserForm()
	# profile_form = ProfileForm()

	if request.method == 'POST':

		# profile_form = ProfileForm(request.POST, request.FILES)
		username = {'username': str(request.POST.__getitem__('email'))}

		response = request.POST.copy()
		response.update(username)
		print(response)
		print(user_form)

		user_form = UserForm(response)
		if user_form.is_valid():
			print(' i m here')
			User.objects.create_user(**user_form.cleaned_data)
			# email = user_form.cleaned_data['email']
			# password = user_form.cleaned_data['password']
			# user = User.objects.create_user()
			# user.set_password(password)
			# user = User(email=email)
			# user.set_password(password)
			# user.save()
			# new_user = User.objects.create_user(**user_form.cleaned_data)
			# print(new_user)
			# new_profile = profile_form.save(commit=False)
			# new_profile.user = new_user
			# new_profile.save()
			# print(user)

			user = authenticate(
				username=user_form.cleaned_data['email'],
				password=user_form.cleaned_data['password']
			)

			login(request, user)
			EmailAuthBackend.authenticate(request, user_form.cleaned_data['email'], user_form.cleaned_data['password'])

			return redirect(authapp_home)

	return render(request, 'designer/sign_up.html', {
		'user_form': user_form,
		# 'profile_form': profile_form,
	})


# Создаем новый проект
def new_project(request):
	print(request.POST)

	if request.method == 'POST':
		user = {'user': str(request.user.pk)}
		response = request.POST.copy()
		response.update(user)

		print('res', response)
		project_form = ProjectForm(response)

		print('project_form.is_valid', project_form.is_valid())

		if project_form.is_valid():
			# new_project = project_form.save(commit=False)
			# creator = request.user
			# new_project.user = creator
			project_form.save()
			# statement_form = StatementForm()
			# return render(request, 'designer/statement.html', {
			#     'statement_form': statement_form,
			# })
			return redirect('project-statement')
			# print("response.get('name')", response.get('name'))
			# return get_project_statement(request, response.get('name'))
		else:
			print(project_form.errors)

	project_form = ProjectForm()
	return render(request, 'designer/newproject.html', {
		'project_form': project_form,
	})


# get
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


def statement(request):
	# print(request.POST)

	if request.method == 'POST':
		statement_data = request.POST.copy()
		print('statement_data', statement_data)
		print('statement_data.name', statement_data.get('project'))
		statement_form = StatementForm(request.POST, request.FILES)
		print('statement_form.is_valid()', statement_form.is_valid())
		if statement_form.is_valid():
			print('here')
			statement_form.save()

			print("statement_data.get('project')", statement_data.get('project'))

		return get_project_statement(request, int(statement_data.get('project')))
		#
		# da = Statement.objects.all()
		# statement_form = StatementForm()
		# print('da', da)
		# return render(request, 'designer/statement.html', {
		#     'statement_form': statement_form,
		#     'statement': da,
		# })
	# if request.method == 'GET':
	#     print('GET', request.GET)
	#     if row_id != None:
	#         try:
	#             Statement.objects.filter(id=row_id).delete()
	#         except Exception as e:
	#             print(e)
	print('im here, statement')
	statement_form = StatementForm()
	return render(request, 'designer/statement.html', {
					'statement_form': statement_form
				})


# func to get the project statement)
def get_project_statement(request, project_name):
	try:
		project_id = project_name
		if type(project_name) == type("str"):

			project_id = Project.objects.get(name=project_name).id

		project = Statement.objects.filter(project=project_id)
		statement_form = StatementForm()
		return render(request, 'designer/statement.html', {
					'statement_form': statement_form,
					'statement': project,
				})
	except Exception as e:
		print('e', e)
		return redirect(authapp_home)
		# statement_form = StatementForm()
		# return render(request, 'designer/statement.html', {
		#     'statement_form': statement_form
		# })


# fun for to del the statement row
def delete_statement_row(request, row):
	print('row_id', row)
	print('request.POST', request.POST)
	print('request.GET', request.GET)
	print('request.method', request.method)

	if request.method == 'POST':
		print('POST', request.POST)
		# redirect(statement)
		return statement(request)

	if row != None:
		try:
			project_id = Statement.objects.get(id=row).project
			print('project_id', project_id)
			Statement.objects.filter(id=row).delete()
		except Exception as e:
			print(e)
	# redirect(statement, request)
	return get_project_statement(request, project_id)

# send id
# project
# dele
# ret
