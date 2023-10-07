from django.shortcuts import render,redirect
from django.contrib import auth


from apps.usuarios.forms import LoginForm

# Create your views here.
def login(request):

    formulario = LoginForm()

    if request.method == 'POST':
        formulario = LoginForm(request.POST)
        if formulario.is_valid():
            nome = formulario['nome_login'].value()
            senha = formulario['senha'].value()

        usuario = auth.authenticate(
            request,
            username = nome,
            password = senha
        )

        if usuario is not None:
            auth.login(request, usuario)
            return redirect('index')
        
        else:
            return redirect('login')
        
    return render(request,'usuarios/login.html',{'form':formulario})


