from django import forms
from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect
from markdown2 import markdown

from . import util

class EntryForm(forms.Form):
    entry_title = forms.CharField(label="New Entry Title")
    entry_body = forms.CharField(label="New Entry Body", widget=forms.Textarea)


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

    entries = util.list_entries()
    entries_lower = [entry.lower() for entry in entries]   

    if request.method == "POST":
        
        form = EntryForm(request.POST)

        if form.is_valid():
            
            entry_title = form.cleaned_data["entry_title"]
            entry_body = form.cleaned_data["entry_body"]

            entry_title_lower = entry_title.lower()

            
            if entry_title_lower not in entries_lower:
                util.save_entry(entry_title, entry_body)
                return redirect('title', entry_title)
                
            else:
                form.add_error("entry_title", "Sorry this entry already exists")
                return render(request, "encyclopedia/create.html", {
                    "form": form,
                    
            })

    return render(request, "encyclopedia/create.html", {
        "form": EntryForm()
    })

def edit (request, title):

    if request.method == "GET":

        entry_content = util.get_entry(title) 

        form = EntryForm(initial = {
            "entry_title": title,
            "entry_body": entry_content
        })

        form.fields["entry_title"].disabled = True

        return render(request, "encyclopedia/edit.html", {
            "form": form,
            "title": title
        })
    
    if request.method == "POST":

        form = EntryForm(request.POST)

        if form.is_valid():

            entry_title = form.cleaned_data["entry_title"]
            entry_body = form.cleaned_data["entry_body"]

            util.save_entry(entry_title, entry_body)

            return redirect ("title", entry_title)

    return 