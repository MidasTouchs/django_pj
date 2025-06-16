pip install -r requirement.txt
python manage.py migrate --noinput
python manage.py collectstatic --noinput --clear
gunicorn virtual_classroom.wsgi:application --bind 0.0.0.0:$PORT

chmod +x build_files.sh
