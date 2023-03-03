# Work

Instructions:

go to https://github.com/digitalexpertfellows/Work/tree/main/Actual%20Projects/SkinCare
git clone from here

on your local machine:
open the project in vs code or pycharm
with the terminal(provided by vs code),after opening the project, create a new virtualenvironment:

https://www.freecodecamp.org/news/how-to-setup-virtual-environments-in-python/

if you don't know how, search on google how to install a virtual env for python(make sure to have python interpreter properlly installed first)

after creating the virtual env, activate it(it is different depending on operating systen)

in linux, you use:"source 'venv/bin/activate " 
so you user source comand with the path ov venv with the activation file

after activating the venv, go in the terminal to the path of requirements.txt, afer thath write:
pip install -r requirements.txt

https://note.nkmk.me/en/python-pip-install-requirements/

after pip has finished isntalling all the needed libraries, go in the terminal to the path where the file "manage.py" is lcoated and enter: python manage.py runserver

acces the localhost at the indicated port(8000 usually),

and go to /home or /products /product in the browser

