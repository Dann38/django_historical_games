from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms import HiddenInput
from authapp.models import GameUser


class AdminGameUserCreateForm(UserCreationForm):
    class Meta:
        model = GameUser
        fields = ('username', 'password1', 'password2', 'email', 'first_name', 'last_name', 'is_superuser')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = f'form-control {field_name}'
            field.help_text = ''


class AdminGameUserUpdateForm(UserChangeForm):
    class Meta:
        model = GameUser
        fields = ('username', 'password', 'email', 'first_name', 'last_name', 'age', 'avatar', 'is_active', 'is_staff',
                  'is_superuser')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field_name == 'password':
                field.widget = HiddenInput()
            else:
                field.widget.attrs['class'] = f'form-control {field_name}'
                field.help_text = ''


