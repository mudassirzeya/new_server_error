from django.shortcuts import render

# Create your views here.

def new_server_info_page(request):
    context = {}
    return render(request, 'index.html', context)