from django.contrib.auth.models import User
from re import match

class AccountValidator:
    
    def __init__(self, username, password1, password2, email):
        self.username = username
        self.password1 = password1
        self.password2 = password2
        self.email = email
        self.error_log = {'error': []}
        
        
    def get_error(self):
        return self.error_log
        
        
    def is_valid(self):
        if all([self._check_username_all(),
               self._check_password_all(),
               self._check_email(),
               ]):
            return True
        else:
            return False
        
        
    def _check_username_all(self):
        if all([self._check_space(self.username, "Username"),
            self._check_length(self.username, "Username"),
            self._check_username_availability(),
            ]):
            return True
        else:
            return False
        
    
    def _check_password_all(self):
        if all([self._check_space(self.password1, "Password"),
            self._check_length(self.password1, "Password"),
            self._check_password_same(),
            ]):
            return True
        else:
            return False
        
        
    def _check_email(self):
        found = match(r'^(([^<>()[\]\\.,;:\s@\"]+(\.[^<>()[\]\\.,;:\s@\"]+)*)|(\".+\"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$', self.email)
        if found:
            return True
        else:
            self.error_log['error'].append('Invalid e-mail address.')
            return False
    
    
    def _check_space(self, text, text_type):
        if " " in text:
            self.error_log['error'].append(text_type + ' can\'t have space.')
            return False
        return True
    
    
    def _check_length(self, text, text_type):
        if (len(text) < 8):
            self.error_log['error'].append(text_type + ' should be atleast 8 characters long.')
            return False
        else:
            return True
        
        
    def _check_username_availability(self):
        try:
            user = User.objects.get(username=self.username)
            self.error_log['error'].append('Username already exists.')
            return False
        except User.DoesNotExist:
            return True

        
    def _check_password_same(self):
        if (self.password1 == self.password2):
            return True
        else:
            self.error_log['error'].append('Confirmation Password doesn\'t match.')
            return False