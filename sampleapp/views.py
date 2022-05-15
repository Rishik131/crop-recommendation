from django.shortcuts import render
from django.http import HttpResponse
from .forms import cropdetails, snippetform

def contact(request):
    if request.method == 'POST':
        form = cropdetails(request.POST)
        if form.is_valid():
            district = form.cleaned_data['district']
            pH = form.cleaned_data['pH']
            moisture = form.cleaned_data['moisture']
            nitrogen = form.cleaned_data['nitrogen']
            phosphorus = form.cleaned_data['phosphorus']
            zinc = form.cleaned_data['zinc']
            potassium = form.cleaned_data['potassium']
            iron = form.cleaned_data['iron']
            copper = form.cleaned_data['copper']
            print(district,pH)
    form = cropdetails()
    return render(request, 'form.html',{'form':form})

def snippetdetail(request):
    if request.method == 'POST':
        form = snippetform(request.POST)
        if form.is_valid():
            form.save()
    form = snippetform()
    return render(request, 'form.html',{'form':form})