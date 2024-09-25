from django.shortcuts import render , redirect
from django.http import HttpResponse
from .models import *
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate , login

# Create your views here.
def receipes(request):
    data=request.POST
    if request.method =="POST":
        data=request.POST
        recepie_name= data.get('recepie_name')
        recepie_description= data.get('recepie_description')
        recepie_image= request.FILES.get('recepie_image')
        
        print(recepie_description)
        print(recepie_name)
        print(recepie_image)
        Recepie.objects.create(
            recepie_name=recepie_name,
            recepie_description=recepie_description,
            recepie_image=recepie_image
        )
        return redirect('receipes')
    queryset = Recepie.objects.all()
    context = {'recipes': queryset} 
    return render(request, "receipes.html", context)
    

def login_page(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Check if the user exists
        if not User.objects.filter(username=username).exists():
            messages.error(request, "Username does not exist. Please register.")
            return redirect('login')
        
        # Authenticate the user
        user = authenticate(username=username, password=password)
        if user is None:
            messages.error(request, "Invalid password")
            return redirect('login')
        else:
            login(request, user)
            return redirect('receipes')

    return render(request, 'login.html')



def register_page(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')  # Changed user_name to username
        password = request.POST.get('password')

        user= User.objects.filter(username=username)
        if user.exists():
            messages.info(request, "same user exist")
            return redirect('register_page')
        
        

        user = User.objects.create(
            first_name=first_name,
            last_name=last_name,
            username=username  # Changed user_name to username
        )
        user.set_password(password)
        user.save()
        return redirect('register_page')
    return render(request, 'register.html')
# def delete_receip(request, id):
#     print(id)
#     queryset = Recepie.objects.get(id=id)
#     queryset.delete
    


    
#     return HttpResponse('a')
    

    return render(request, "receipes.html" ,context)