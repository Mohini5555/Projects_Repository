"""
<<<<<<< HEAD
WSGI config for pro project.
=======
WSGI config for pro1 project.
>>>>>>> fe32d605f5e00f7dfd3e357762f7f29eff9a6145

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

<<<<<<< HEAD
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pro.settings')
=======
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pro1.settings')
>>>>>>> fe32d605f5e00f7dfd3e357762f7f29eff9a6145

application = get_wsgi_application()
