# sites-ratereview
### Django University Project<br>
<hr>
Install all library in requirements.txt using pip with command<br>
pip install -r requirements.txt<br>
make sure to be in the directory of requirements.txt<br>
Before installing make sure to uninstall the previous version first to avoid conflict<br>
<hr>
After every pull run the following command lines (This will generates all the tables required)<br>
manage.py makemigrations<br>
manage.py migrate<br>
<hr>
To run the server use the command<br>
manage.py runserver<br>
localhost:8000/sites/home is the homepage of the sites<br>
<hr>
To create a superuseraccount run the command<br>
manage.py createsuperuser<br>
This account can be used to login to admin page<br>
<hr>
Places for html and static images,css,js files should be within<br>
(app_name)/templates/(app_name)/ or (app_name)/static/(app_name)/<br>
For examples of login page within accounts<br>
accounts/templates/accounts/login.html<br>
accounts/static/accounts/scripts/login.js for javascript<br>
accounts/static/accounts/styles/login.css for css<br>
accounts/static/accounts/images/login_background.jpg for images<br>
