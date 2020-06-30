from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django.forms import HiddenInput
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


class GameUserUpdateForm(UserChangeForm):
    class Meta:
        model = GameUser
        fields = ('username', 'password', 'email', 'first_name', 'last_name', 'age', 'avatar')
        # fields = ('username', 'password1', 'password2', 'email', 'first_name', 'last_name')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field_name == 'password':
                field.widget = HiddenInput()
            else:
                field.widget.attrs['class'] = f'form-control {field_name}'
                field.help_text = ''


