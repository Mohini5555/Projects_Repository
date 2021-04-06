"""
<<<<<<< HEAD
ASGI config for pro1 project.
=======
ASGI config for pro2 project.
>>>>>>> 11fe4acaf6edb7e1da6191ef105be16fb11685aa

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

<<<<<<< HEAD
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pro1.settings')
=======
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pro2.settings')
>>>>>>> 11fe4acaf6edb7e1da6191ef105be16fb11685aa

application = get_asgi_application()
