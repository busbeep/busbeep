cd ..
virtualenv --no-site-packages env
source env/bin/activate
easy_install pyramid

python setup.py develop

initialize_app_db development.ini
