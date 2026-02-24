from django.http import HttpResponse
from django.shortcuts import render, redirect
from markdown2 import markdown

from . import util

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, title):
     
  
    entries = util.list_entries()
    for entry in entries:
        
        if entry.lower() == title.lower():
            content = util.get_entry(entry)
            content_mk = markdown(content)
            print(content_mk)
            return render(request, "encyclopedia/entry.html", {
                "title": entry,
                "content": content_mk
            })
        
    return render(request, "encyclopedia/error.html")

def search(request):

    query = request.GET.get('q')
    entries = util.list_entries()

    for entry in entries:
        print(entry)

        if query.lower() == entry.lower():
            return redirect('')


    #print(f"Data received: {query}")
    #print(f"GET Completo: {request.GET}")

    #search recebe os dados do form
        #SE a consulta corresponder com os dados da entrada, usuário será redirecionado para a página da entrada
        
        #SENÃO o usuário deve ser enviado a uma página de resultados que exibe todas as entradas que contém a consuylta como substring.


    return HttpResponse("Teste")