from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import (UserRegisterForm,
                    UserUpdateForm,
                    ProfileUpdateForm,
                    ContactForm
                    )

from django.core.mail import EmailMessage
from django.template.loader import get_template


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            # username = form.cleaned_data.get('username')
            messages.success(request,
                             f'Your account has been created! Now you are able to login.')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'users/profile.html', context)


def contact(request):
    form_class = ContactForm()
    if request.method == 'POST':
        form = form_class(data=request.POST)

        if form.is_valid():
            name = form.cleaned_data.get('Name', '')
            email = form.cleaned_data.get('Email', '')
            message = form.cleaned_data.get('Message', '')

            template = get_template('users/contact_template.txt')
            context = {
                'contact_name': name,
                'contact_email': email,
                'form_content': message
            }
            content = template.render(context)

            email = EmailMessage(
                "New contact form submission",
                content,
                "athisiiekhe.com" + '',
                ['daiho.mca18.du@gmail.com'],
                headers={'Reply-To': email}
            )

            email.send()
            messages.success(request, f'Your contact form has been sent!')
            return redirect('contact')

    return render(request, 'users/contact.html', {'form': form_class})
