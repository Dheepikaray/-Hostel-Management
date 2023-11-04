from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

# from .forms import OrderForm

def new(request):
    return render(request, 'index.html')

def base(request):
    return render(request,'base.html')

# def registerPage(request):
#     form = UserCreationForm()
#
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()

    context = {'form': form}
    return render(request,'register.html', context)
