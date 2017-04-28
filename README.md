# sites-ratereview
## Django University Project
#### Running for First Time Instruction

- This project was developed with Python version 3.6.0
- Install all library in requirements.txt using pip with the command line
  - pip install -r "requirements.txt" (make sure to be in the directory same as requirements.txt")
- Create folder named migrations with file \_\_init\_\_.py in it and place it within these folders
  - accounts (It should look like this /accounts/migrations/\_\_init\_\_.py)
- Run the following command lines (This will generates all the tables required)
  - manage.py makemigrations
  - manage.py migrate
- To run the server use the command
  - manage.py runserver (localhost:8000 is the homepage of the sites)
- To create a superuseraccount run the command
  - manage.py createsuperuser (This account can be used to login to admin page)


#### Developer Instruction

- Places for html and static images,css,js files should be within
  - (app_name)/templates/(app_name)/ or (app_name)/static/(app_name)/
  - For examples of login page within accounts
  - accounts/templates/accounts/login.html
  - accounts/static/accounts/scripts/login.js for javascript
  - accounts/static/accounts/styles/login.css for css
  - accounts/static/accounts/images/login_background.jpg for images
- Images stored by database should be in the media folder
  - media/(app_name)/
