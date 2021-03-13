from django.shortcuts import redirect, render
from .forms import SignupForm, LoginForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages


def signup_view(request):
    if request.method == 'POST':
        signform = SignupForm(request.POST)
        if signform.is_valid():
            signform.save()

    else:
        signform = SignupForm()

    context={
        'signform_key': signform
    }

    return render(request, 'users/registration.html', context)

def loginView(request):
    if request.method == 'POST':
        form = LoginForm()
        uname = request.POST.get('username' )
        password = request.POST.get('password')

        user_data = authenticate(username=uname, password=password)
        print('udata is', user_data)
        if user_data is not None:
            login(request, user_data)
            return redirect('allclaimdata')
        else:
            messages.error(request, 'username and password is incorrect')
    else:
        form =LoginForm()

    return render(request, 'users/login.html', {'form_key': form})

def logout_view(request):
    logout(request)

    return redirect('index')
