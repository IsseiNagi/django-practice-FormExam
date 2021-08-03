from django import forms
from .models import Students
from django.core import validators


def check_grade(value):
    if not 0 < value < 4:
        raise validators.ValidationError('無効な入力です')


class StudentsModelForm(forms.ModelForm):
    name = forms.CharField(
        label='名前',
        max_length=10,
        min_length=3,
        widget=forms.TextInput(attrs={
            'placeholder': '名前を入力してください'
        })
    )
    age = forms.IntegerField(
        label='年齢',
        widget=forms.TextInput(attrs={
            'placeholder': '年齢を入力してください'
        })
    )
    grade = forms.IntegerField(
        label='学年',
        validators=[check_grade]
        )
    picture = forms.FileField(label='本人写真')

    class Meta:
        model = Students
        fields = '__all__'


class StudentsUpdateForm(forms.Form):
    name = forms.CharField(
        label='名前',
        max_length=10,
        min_length=3,
        widget=forms.TextInput(attrs={
            'placeholder': '名前を入力してください'
        })
    )
    age = forms.IntegerField(
        label='年齢',
        widget=forms.TextInput(attrs={
            'placeholder': '年齢を入力してください'
        })
    )
    grade = forms.IntegerField(
        label='学年',
        validators=[check_grade]
        )
    picture = forms.FileField(label='本人写真', required=False)

    class Meta:
        model = Students
        fields = '__all__'