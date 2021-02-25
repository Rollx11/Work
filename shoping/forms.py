from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms



class RegisterForm(UserCreationForm):
   username = forms.CharField(max_length=254,)
   # поле почты проходит валидацию иначе чем CharField

   # пароль также проходит валидацию и по умолчанию к нему применяются довольно строгие правила
   # но тут указывается тип поля уже с помощью аргумента widget
   password1 = forms.CharField(widget=forms.PasswordInput, max_length=254, help_text='')
   password2 = forms.CharField(widget=forms.PasswordInput, max_length=254, help_text='')

   class Meta:
        model = User
        fields = ('username', 'password1', 'password2',)



class LoginForm(forms.Form):
   login = forms.CharField(max_length=254,
                           help_text='')
   password = forms.CharField(widget=forms.PasswordInput)

class SearchForm(forms.Form):
      search = forms.CharField(required=False,
                               label='wwww', )