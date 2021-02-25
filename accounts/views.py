from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages

#djangosuper1/adminadmin
# Create your views here.
def admindisplay(request):

    #qs=User.objects.filter.all()
    qs = User.objects.values()
    #print(all_users)
    #print(all_users[0]['username'])
    #username=uname,password=pwd1,email=email,first_name=fname,last_name=lname    
    #context = {'qs':qs}
    print("Inside Views Display all Method")
    #return render(request, 'studapp/studresults.html',context)
    return render(request, 'accounts/adminresult.html',{'qs':qs})

def logout(request):
    auth.logout(request)
    return redirect("/travel")

def login(request):
    if request.method == "POST":
        uname = request.POST["username"]
        pwd1 = request.POST['pwd']
        
        user = auth.authenticate(username=uname,password=pwd1)
        if user is not None:
            auth.login(request,user)
            return redirect('/travel')
        else:
            
            messages.error(request,"Invalid Credentials")

            
            return redirect('login')
    
    else:
        return render(request, 'accounts/login.html')

def register(request):
    if request.method == "POST":
        fname = request.POST["fname"]
        lname = request.POST["lname"]
        uname = request.POST["username"]
        pwd1 = request.POST['pwd1']
        pwd2 = request.POST['pwd2']
        email = request.POST['email']

        if pwd1 == pwd2:
            if User.objects.filter(username=uname).exists():
                messages.error(request,"Username Aready in Use")

            elif User.objects.filter(email=email).exists():
                messages.error(request,"Email ID Aready in Use")
            else:
                user = User.objects.create_user(username=uname,password=pwd1,email=email,first_name=fname,last_name=lname)
                user.save()
                messages.info(request,"User Registered")
                return redirect("/travel")


        else:
            messages.error(request,"Both Password and Confirm password are not matching")
        return render(request, 'accounts/index.html')
    else:
        return render(request, 'accounts/index.html')
