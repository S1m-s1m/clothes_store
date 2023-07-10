from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.views.generic import ListView, DetailView

from main.forms import Review_form, User_form, Clothes_form
from main.models import Clothes, Season, Review, User


# Create your views here.

def main_page(request):
    reviews = Review.objects.all()
    form = User_form()
    new = Clothes.objects.last()
    if request.method == 'POST':
        name = request.POST.get('name')
        user = User(name=name)
        user.save()
        users = User.objects.all()
        return render(request, 'main/main_page.html', {'name': name, 'form':form, 'users': users, 'new':new, 'reviews': reviews})
    return render(request, 'main/main_page.html', {'name': User.objects.last().name if User.objects.exists() else None, 'users': User.objects.all(), 'form':form, 'new':new, 'reviews': reviews})

def contacts(request):
    reviews = Review.objects.all()
    return render(request, 'main/contacts.html',{'reviews': reviews})

class clothes_view(ListView):
    model = Clothes
    template_name = 'main/clothes.html'
    queryset = Clothes.objects.all()
    reviews = Review.objects.all()
    clothes_list = {'clothes_list':queryset, 'reviews': reviews}

def season_clothes(request, season):
    season_clothes = Clothes.objects.filter(seasons__url=season)
    reviews = Review.objects.all()
    return render(request, 'main/season_clothes.html', {'season_clothes':season_clothes, 'reviews': reviews})

def clothes_detail_view(request, url):
    cloth_url = get_object_or_404(Clothes, url=url)
    reviews = Review.objects.all()
    return render(request, 'main/clothes_detail.html', {'cloth_url':cloth_url, 'reviews':reviews})

def review_view(request):
    error = ''
    form = Review_form()
    print(request.POST)
    if request.method == 'POST':
        form = Review_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_review')
        else:
            error = 'Форма была неверной'
        if form.cleaned_data.get('reset'):
            # Выполните необходимые действия при нажатии на кнопку "Сбросить"
            # Например, сбросьте значения полей формы
            form.cleaned_data['name'] = ''
            form.cleaned_data['email'] = ''
            form.cleaned_data['text'] = ''
        else:
            form = Review_form()
    reviews = Review.objects.all()
    return render(request, 'main/review.html', {'form':form, "reviews":reviews, "error":error})


def add_cloth_view(request):
    reviews = Review.objects.all()
    error = ''
    if request.method == 'POST':
        form = Clothes_form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('main')# Замените 'success_page' на URL страницы, которую вы хотите отобразить после успешного сохранения формы
        else:
            error = 'Форма была неверной, возможно ваш url уже существует, попробуйте еще раз'
        if form.cleaned_data.get('reset'):
            form.cleaned_data['image'] = ''
            form.cleaned_data['name'] = ''
            form.cleaned_data['contacts'] = 'Отсутствуют'
            form.cleaned_data['cost'] = ''
            form.cleaned_data['url'] = ''
        else:
            form = Clothes_form()
    else:
        form = Clothes_form()
    return render(request, 'main/add_cloth.html', {'form': form, 'error':error, 'reviews': reviews})




