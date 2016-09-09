from django.shortcuts import render
from django.core.mail import send_mail
from .forms import info_form_form

def home(request):
    title = 'Heya Sucker !'
    form = info_form_form(request.POST or None)
    if form.is_valid():
        email = form.cleaned_data['email']
        cc_myself = form.cleaned_data['cc_myself']
        Reg = form.cleaned_data['Reg']
        full_name = form.cleaned_data['full_name']
        instance = form.save(commit=False)
        recipient_l = ['mrinalwahal@gmail.com']
        if cc_myself == True:
            recipient_l.append(email)
        #send_mail(full_name, Reg, email, recipient_l)
        instance.save()
    context = {
    'title' : title,
    'form' : form
    }
    return render(request, 'home.html', context)
