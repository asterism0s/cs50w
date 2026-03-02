from django import forms
from django.http import HttpResponse
from django.shortcuts import render, redirect
from markdown2 import markdown

from . import util

class NewEntryForm(forms.Form):
    new_entry_title = forms.CharField(label="New Entry Title")
    new_entry_body = forms.CharField(label="New Entry Body", widget=forms.Textarea)


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
            
            return render(request, "encyclopedia/entry.html", {
                "title": entry,
                "content": content_mk
            })
        
    return render(request, "encyclopedia/error.html")

def search(request):

    query = request.GET.get('q')
    entries = util.list_entries()

    results = []

    for entry in entries:

        if query.lower() == entry.lower():
            return redirect('title', query)
        
        elif query.lower() in entry.lower():
            results.append(entry)

    return render(request, "encyclopedia/results.html", {
                "title": entry,
                "query": query,
                "results": results
            })


def create(request):

    if request.method == "POST":
        form = NewEntryForm(request.POST)
        if form.is_valid():
            new_entry = form.cleaned_data["new_entry"]
            request.session
        #recebe o formulário do usuário
        #pega os dados, processa e salvE a
        #redireciona
    else:
        #mostra o formulário vazio (get)

    return render(request, 'create.html')

#usuário clica em "create new page" -> e com isso vai para uma url dedicada
#nessa url precisa ver um formulario (com título e textarea) => GET
#usuario preenche e envia -> dados vão para o servidor => POST
#django processa: checa se existe, salva ou mostra erro