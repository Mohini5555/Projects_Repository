"""
<<<<<<< HEAD
WSGI config for pro1 project.
=======
WSGI config for pro2 project.
>>>>>>> 11fe4acaf6edb7e1da6191ef105be16fb11685aa

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

<<<<<<< HEAD
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pro1.settings')
=======
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pro2.settings')
>>>>>>> 11fe4acaf6edb7e1da6191ef105be16fb11685aa

application = get_wsgi_application()
