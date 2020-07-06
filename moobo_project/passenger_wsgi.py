# -*- coding: utf-8 -*-
import os, sys
sys.path.insert(0, '/var/www/murad/data/www/moobo.space/moobo')
sys.path.insert(1, '/var/www/murad/data/www/moobo.space/moobo/mooboenv/lib/python3.6/site-packages')
os.environ['DJANGO_SETTINGS_MODULE'] = 'moobo_project.settings'
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()