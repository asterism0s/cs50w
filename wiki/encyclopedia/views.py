from django.http import HttpResponse
from django.shortcuts import render

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, title):
     

    entries = util.list_entries()

    for entry in entries:
        if entry.lower() == title.lower():
            show_title = entry

    #pegar o que foi escrito na url e converter pra lower
    #pegar a entry e converter pra lower
    #comparar as strings
    #mandar pra fora

    content = util.get_entry(title)
    
    return HttpResponse(show_title)

    # return render (request, "wiki/entry.html", {
    #     content: title.lower()
    # })