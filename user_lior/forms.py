from django.contrib.auth.forms import AuthenticationForm

class SinginForm(AuthenticationForm):
    def confirm_login_allowed(self, user):
        pass
