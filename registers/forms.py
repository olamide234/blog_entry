from django import forms
# from .models import Register
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, password_validation
from django.core.exceptions import ValidationError

class RegisterForm(UserCreationForm):
    email = forms.EmailField(max_length=64, required=True)

    class Meta:
        model = User
        # widget = {
        #     'password': forms.PasswordInput(),
        # }
        fields = ['email', 'password1']
        
    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        del self.fields['password2']
        self.fields['password1'].help_text = None

    def _post_clean(self):
        super(RegisterForm, self)._post_clean()
        password = self.cleaned_data.get('password1')
        if password:
            try:
                password_validation.validate_password(password, self.instance)
            except ValidationError as error:
                self.add_error('password1', error)

    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

class AuthenticateLoginForm(AuthenticationForm):
    email = forms.EmailField(max_length=64, required=True)

    # class Meta:
    #     # model = User
    #     fields = ['email', 'password']

    def __init__(self, request=None, *args, **kwargs):
        # self.request = request
        # self.user_cache = None
        super(AuthenticateLoginForm, self).__init__(*args, **kwargs)
        del self.fields['username']

    def clean(self):
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')
        if email is not None and password:
            self.user_cache = authenticate(self.request, email=email, password=password)
            if self.user_cache is None:
                return self.get_invalid_login_error()
            else:
                self.confirm_login_allowed(self.user_cache)

        return self.cleaned_data

