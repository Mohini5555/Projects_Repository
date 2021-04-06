<<<<<<< HEAD
#!c:\users\armya\onedrive\desktop\django\project_2\env\scripts\python.exe
=======
#!c:\users\armya\onedrive\desktop\django_projects\project01\env\scripts\python.exe
>>>>>>> fe32d605f5e00f7dfd3e357762f7f29eff9a6145
# When the django-admin.py deprecation ends, remove this script.
import warnings

from django.core import management

try:
    from django.utils.deprecation import RemovedInDjango40Warning
except ImportError:
    raise ImportError(
        'django-admin.py was deprecated in Django 3.1 and removed in Django '
        '4.0. Please manually remove this script from your virtual environment '
        'and use django-admin instead.'
    )

if __name__ == "__main__":
    warnings.warn(
        'django-admin.py is deprecated in favor of django-admin.',
        RemovedInDjango40Warning,
    )
    management.execute_from_command_line()
