from django import forms
from django.forms import TextInput, EmailInput, Textarea,ModelForm, CharField
from .models import Review, User, Clothes

class Review_form(forms.ModelForm):
    class Meta:
        model = Review
        fields = ["name", "email", "text"]
        widgets = {
            "name": TextInput(attrs={
                "class": "form-control",
                'placeholder': "Имя"
            }),
            "email": EmailInput(attrs={
                "class": "form-control",
                'placeholder': "Эл.почта"
            }),
            "text": Textarea(attrs={
                "class": "form-control",
                'placeholder': "Отзыв"
            }),
        }

class User_form(forms.ModelForm):
    class Meta:
        model = User
        fields = ["name"]
        widgets = {
            "name": TextInput(attrs={
                "class": "form-control",
                'placeholder': "Имя"
            }),
        }

class Clothes_form(forms.ModelForm):
    class Meta:
        model = Clothes
        fields = '__all__'
        widgets = {
            'image': forms.ClearableFileInput(attrs={'class': 'form-control','placeholder':'Добавьте фото товара'}),
            'name': forms.TextInput(attrs={'class': 'form-control','placeholder':'Добавьте имя товара'}),
            'contacts': forms.TextInput(attrs={'class': 'form-control','placeholder':'Добавьте ваши контакты'}),
            'sex': forms.TextInput(attrs={'class': 'form-control','placeholder':'Добавьте гендер'}),
            'cost': forms.NumberInput(attrs={'class': 'form-control','placeholder':'Добавьте цену товара'}),
            'seasons': forms.SelectMultiple(attrs={'class': 'form-control','placeholder':'Добавьте сезон для товара'}),
            'url': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите URL'}),
            'size': forms.SelectMultiple(attrs={'class': 'form-control','placeholder':'Добавьте размер'}),
            'availability': forms.SelectMultiple(attrs={'class': 'form-control','placeholder':'Добавьте состояние товара'}),
        }

    # def clean_url(self):
    #     url = self.cleaned_data.get('url')
    #     if Clothes.objects.filter(url=url).exists():
    #         raise forms.ValidationError('Url уже существует')
    #     return url
