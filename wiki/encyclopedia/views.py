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
            content = util.get_entry(entry)
            return HttpResponse(content)
        
    return HttpResponse("Entry not found")




    # return render (request, "wiki/entry.html", {
    #     content: title.lower()
    # })

        #content = util.get_entry(title)
    #entries = util.list_entries()