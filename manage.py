#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangobasico.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


#___________________Django Shell__________________________

# Criar projeto: (django-admin.py  startproject 'projectname')
# Carrega um console python: (python manage.py shell)
    # No shell: object=Class(args), object.save(), object.delete(); Criam o registro de modelo, salva-o no banco de dados, e deleta-o de lá.
# Usado para estartar a aplicação: (python manage.py runserver)
# Criar as migrations: (python manage.py makemigrations)
# Fazer a migração dos modelos: (python manage.py migration)
# Criar usuario de acesso à sessão de administração: (python manage.py createsuperuser)
# Lista de comando executáveis: (python manage.py)

if __name__ == '__main__':
    main()
