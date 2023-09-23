from django.shortcuts import render,redirect
from django.http import HttpResponse

# Create your views here.


from apps.contato.models import Contato
from apps.contato.forms import ContatoForms


def index(requisicao):
    '''
    dados = {
            1:{
                "nome":"Weskley Bezerra",
                "fone":"99675-3679",
                "email":"weskley@xpto.com" 
            },

            2:{
                "nome":"Filipe Oliveira",
                "fone":"98787-5972",
                "email":"filipe@xpto.com" 

            },
            3:{
                "nome":"Ivad Etnaclavac ",
                "fone":"98888-8888",
                "email":"ivad@gmail.com" 

            }


        }    
    '''    
    dados = Contato.objects.all()
    #return HttpResponse('<h1>Minha primeira página em Django</h1>')
    return render(requisicao,'index.html',{"contatos":dados})

def form(requisicao):
    form = ContatoForms()
    if requisicao.method == 'POST':
        form = ContatoForms(requisicao.POST)
        if form['nome'].value() != '' and form['fone'].value() != '':
            nome_form = form['nome'].value()
            fone_form = form['fone'].value()

            contato = Contato(nome=nome_form,fone=fone_form)
            contato.save()

            return redirect('index')




    return render(requisicao,'form.html',{"form":form})


