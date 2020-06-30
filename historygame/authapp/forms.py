from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from authapp.models import GameUser


class GameUserLoginForm(AuthenticationForm):
    class Meta:
        model = GameUser
        fields = ('username', 'password')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = f'form-control {field_name}'


class GameUserRegisterForm(UserCreationForm):
    class Meta:
        model = GameUser
        # fields = ('username', 'password1', 'password2', 'email', 'first_name', 'last_name', 'age', 'avatar')
        fields = ('username', 'password1', 'password2', 'email', 'first_name', 'last_name')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = f'form-control {field_name}'
            field.help_text = ''