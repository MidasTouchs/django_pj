web: gunicorn virtual_classroom.wsgi --log-file - 
#or works good with external database
web: python manage.py migrate && gunicorn virtual_classroom.wsgi