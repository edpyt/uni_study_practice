from django import forms
from django.core.validators import RegexValidator


class UserNameForm(forms.Form):
    username = forms.CharField(
        label="Введите Ваше имя",
        max_length=50,
        required=True,
        validators=[
            RegexValidator(
                regex="^[а-яА-Я\s]+$",
                message="Разрешены только пробелы и русские буквы",
            )
        ],
    )
