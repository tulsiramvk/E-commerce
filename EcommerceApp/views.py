from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from . models import Profile
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

def signup(request):
	if request.method == 'POST':
		fname = request.POST['fname']
		lname = request.POST['lname']
		mobile = request.POST['mobile']
		email = request.POST['email']
		uname = request.POST['username']
		passwd = request.POST['password']
		role = request.POST['role']
		profile_pic = request.FILES.get('profile_pic') or False
		u = User(username=uname,password=make_password(passwd),first_name=fname,last_name=lname,email=email)
		u.save()
		p = Profile(user=u, profile_pic=profile_pic, mobile=mobile, role=role)
		p.save()
		return redirect('/login/')



	return render(request,'signup.html')

def login_call(request):
	if request.method == "POST":
		uname = request.POST['username']
		passwd = request.POST['password']
		currentUser = authenticate(username=uname, password=passwd)
		if currentUser:
			login(request,currentUser)
			
			u = Profile.objects.get(user__username=request.user)
			if u.role == "buyer":
				return redirect('/buyer/home/')
			if u.role == "seller":
				return redirect('/seller/home/')
			return HttpResponse("<h1>Login Hogya...!</h1>")
		else:
			return HttpResponse("<h1>Wrong Credential</h1>")

	return render(request,'login.html')

@login_required
def logout_call(request):
	logout(request)
	return redirect('/login/')