from django.shortcuts import render

# Create your views here.

def post_list(request):
    return render(request, 'blog/Pickme.html', {})

def edit(request):
    return render(request, 'blog/edit.html', {})
