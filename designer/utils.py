# /usr/bin/python
# -*- coding: utf-8 -*-
from io import BytesIO, StringIO
# from Django.template import Context
from django.http import HttpResponse
from django.template import context
from django.template.loader import get_template
from django.conf import settings
import os


from xhtml2pdf import pisa


def fetch_pdf_resources(uri, rel):
	if uri.find(settings.MEDIA_URL) != -1:
		path = os.path.join(settings.MEDIA_ROOT, uri.replace(settings.MEDIA_URL, ''))
	elif uri.find(settings.STATIC_URL) != -1:
		path = os.path.join(settings.STATIC_ROOT, uri.replace(settings.STATIC_URL, ''))
	else:
		path = None
	return path


def render_to_pdf(template_src, context_dict):
	try:
		template = get_template(template_src)
		# context = Context(context_dict)
		html = template.render(context_dict)
		# print('html', html)
		result = BytesIO()
		print('result', result)
		pdf = pisa.pisaDocument(BytesIO(html.encode("UTF-8")), result, encoding="UTF-8")
		if not pdf.err:
			return HttpResponse(result.getvalue(), content_type='application/pdf')
		print('pdf.err', pdf.err)
	except Exception as e:
		print('e', e)
		return HttpResponse(str(e), status=500)