from django.views.generic.list import User
from django.core.mail import send_mail
from django.conf import settings
from .models import Bulletin, Response
from .forms import BulletinForm, ResponseForm
from django.shortcuts import render, redirect, get_object_or_404





def register_user(request):
    if request.method == 'POST':
        # Получение данных формы регистрации из POST-запроса
        email = request.POST.get('email')

        # Генерация кода подтверждения регистрации
        confirmation_code = generate_confirmation_code()

        # Создание объекта пользователя
        user = User(email=email, confirmation_code=confirmation_code)
        user.save()

        # Отправка письма с кодом подтверждения на электронную почту пользователя

        return render(request, 'registration_success.html')
    else:
        return render(request, 'register_user.html')

def create_bulletin(request):
    if request.method == 'POST':
        form = BulletinForm(request.POST)
        if form.is_valid():
            bulletin = form.save(commit=False)
            bulletin.user = request.user
            bulletin.save()
            return redirect('bulletin_detail', bulletin_id=bulletin.id)
    else:
        form = BulletinForm()
    return render(request, 'create_bulletin.html', {'form': form})

def edit_bulletin(request, bulletin_id):
    bulletin = get_object_or_404(Bulletin, id=bulletin_id)
    if request.method == 'POST':
        form = BulletinForm(request.POST, instance=bulletin)
        if form.is_valid():
            bulletin = form.save()
            return redirect('bulletin_detail', bulletin_id=bulletin.id)
    else:
        form = BulletinForm(instance=bulletin)
    return render(request, 'edit_bulletin.html', {'form': form, 'bulletin': bulletin})

def bulletin_detail(request, bulletin_id):
    bulletin = get_object_or_404(Bulletin, id=bulletin_id)
    return render(request, 'bulletin_detail.html', {'bulletin': bulletin})

def create_bulletin(request):
    if request.method == 'POST':
        form = BulletinForm(request.POST)
        if form.is_valid():
            bulletin = form.save(commit=False)
            bulletin.user = request.user
            bulletin.save()
            return redirect('bulletin_detail', bulletin_id=bulletin.id)
    else:
        form = BulletinForm()
    return render(request, 'create_bulletin.html', {'form': form})


def generate_confirmation_code():
    pass


def bulletin_detail(request, bulletin_id):
    bulletin = get_object_or_404(Bulletin, id=bulletin_id)
    responses = Response.objects.filter(bulletin=bulletin)
    if request.method == 'POST':
        form = ResponseForm(request.POST)
        if form.is_valid():
            response = form.save(commit=False)
            response.user = request.user
            response.bulletin = bulletin
            response.save()
            send_notification_email(response)
            return redirect('bulletin_detail', bulletin_id=bulletin.id)
    else:
        form = ResponseForm()
    return render(request, 'bulletin_detail.html', {'bulletin': bulletin, 'responses': responses, 'form': form})

def send_notification_email(response):
    subject = 'Новый отклик на ваше объявление!'
    message = f'Пользователь {response.user.username} оставил отклик на ваше объявление: {response.bulletin.title}'
    send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [response.bulletin.user.email])


def user_responses(request):
    user = request.user
    responses = Response.objects.filter(user=user)
    bulletins = Bulletin.objects.filter(response__in=responses)
    return render(request, 'user_responses.html', {'bulletins': bulletins})


