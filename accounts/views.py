from django.shortcuts import render
from .form import RegisterationForm
from django.shortcuts import render, redirect
from accounts.models import Account
from django.contrib import auth, messages


# Create your views here.
def register(request):
    if request.user.is_authenticated:
        return redirect('login')
    form = RegisterationForm()
    if request.method == 'POST':
        form = RegisterationForm(request.POST)
        if form.is_valid():
            Name = form.cleaned_data['Name']
            Mobile = form.cleaned_data['Mobile']
            Role = form.cleaned_data['Role']
            Country = form.cleaned_data['Country']
            Nationality = form.cleaned_data['Nationality']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = Account.objects.create_user(Name=Name,Role=Role,email=email,password=password,Mobile=Mobile,Nationality=Nationality,Country=Country)
            # user.save()
            messages.info(request,'you were registered then please verify phone number')
            return redirect('login')
        else:
            messages.error(request,'please enter a valid form')
    context ={
        'form':form
    }
    return render(request,'register.html',context)

 
def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        print(email)
        password = request.POST['password']
        print(password)
        user = auth.authenticate(email=email, password=password)
        print(user)
        if user is not None:
            if user.is_admin:
                auth.login(request, user)
                return render(request, 'admin.html')

            elif user.Role == "student" or user.is_admin:
                auth.login(request, user)
                return render(request, 'student.html')

            elif user.Role == "staff" or user.is_admin:
                auth.login(request, user)
                return render(request, 'staff.html')

            elif user.Role == "editor" or user.is_admin:
                auth.login(request, user)
                return render(request, 'editor.html')
        else:
                messages.error(request, 'Invalid credentials')
                return redirect('login')
    return render(request, 'login.html')
