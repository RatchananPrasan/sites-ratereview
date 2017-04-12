# sites-ratereview
Django University Project<br>
<br>
Install all library in requirements.txt using pip with command<br>
pip install -r requirements.txt<br>
make sure to be in the directory of requirements.txt<br>
Before installing make sure to uninstall the previous version first to avoid conflict<br>
<br>
After every pull run the following command lines (This will generates all the tables required)<br>
manage.py makemigrations<br>
manage.py migrate<br>
<br>
To run the server use the command<br>
manage.py runserver<br>
localhost:8000/sites/home is the homepage of the sites<br>
<br>
To create a superuseraccount run the command<br>
manage.py createsuperuser<br>
This account can be used to login to admin page<br>
<br>
Places for html, static images,css,js files should be within<br>
(app_name)/templates/(app_name)/<br>
For examples of login page within accounts<br>
accounts/templates/accounts/login.html<br>
accounts/templates/accounts/scripts/login.js for javascript<br>
accounts/templates/accounts/styles/login.css for css<br>
accounts/templates/accounts/images/login_background.jpg for images<br>
