from home.views import message
from home.forms.update_create_form import UpdateForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user
from django.contrib import auth
from home.models import DataUser

@login_required(login_url="home:home")
def update(request):
    user = get_user(request)
    datauser = DataUser.objects.get(owner=user)
    phone = datauser.phone     
    if request.method == 'POST':
        form = UpdateForm(data=request.POST, instance=request.user)
        phone = request.POST.get('phone', '')

        context = {
        'title': 'Update',
        'form': form,
        'phone': phone,
        }
        if form.is_valid():
            datauser.phone = phone
            datauser.save()     
            form.save()
            message(request, 'Atualizado com sucesso', sucesss=True)
            if request.POST.get('is_active', '') == 'off':
                auth.logout(request)
            return redirect('home:home')
        else:
            message(request, 'Erro ao atualizar', error=True)
            url = 'home/update.html'
            return render(request, url, context=context)

    form = UpdateForm(instance=request.user, phone=phone)
    context = {
        'title': 'Update',
        'form': form,
        'phone': phone,
    }
    url = 'home/update.html'
    return render(request, url, context=context)
