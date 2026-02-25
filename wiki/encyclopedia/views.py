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
