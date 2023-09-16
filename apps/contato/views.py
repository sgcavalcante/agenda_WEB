from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.






def index(requisicao):
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

    #return HttpResponse('<h1>Minha primeira página em Django</h1>')
    return render(requisicao,'home.html',{"contatos":dados})

