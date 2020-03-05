from django.shortcuts import render
from django.views.generic import TemplateView
from django.core.files.storage import FileSystemStorage

# Create your views here.
def home(request):
    return render(request, 'blog/Pickme.html', {})

def how_to_use(request):
    return render(request, 'blog/how_to_use.html', {})

def team(request):
    return render(request, 'blog/team.html', {})

def edit(request):
    if request.method =='POST':
        uploaded_file = request.FILES['document']
        print(uploaded_file.name)
        print(uploaded_file.size)
        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name, uploaded_file)
        url = fs.url(name)
        print(url)
    return render(request, 'blog/edit.html', {})
