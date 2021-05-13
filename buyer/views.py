from django.shortcuts import render,redirect
from seller.models import Products,Category
from EcommerceApp.models import Profile,User
from django.http import HttpResponse
from . models import Cart,Address


# Create your views here.
def home(request):
	pobjs = Products.objects.all()
	cobjs = Category.objects.all()
	ct = Cart.objects.count()
	return render(request,'WelcomeBuyer.html',{'data': pobjs , 'data1':cobjs, 'count':ct})
'''
def my_profile(request):
	pobj = Profile.objects.get(user__username=request.user)
	uobj = User.objects.get(username=request.user)
	ct = Cart.objects.count()
	if request.method == 'POST':
		fname = request.POST['fname']
		lname = request.POST['lname']
		add = request.POST['add']
		#profile_pic = request.FILES['profile_pic']
		P = Profile.objects.filter(user__username=request.user)
		U = User.objects.filter(username=request.user)
		U.update(first_name=fname,last_name=lname)
		P.update(address=add)
		return redirect('/buyer/my_profile/')

	return render(request,'my_profile.html',{'data':uobj,'data1': pobj, 'count': ct})'''

def cart(request,id):
	pobj = Products.objects.get(id=id)
	uobj = Profile.objects.get(user__username=request.user)
	url = '/buyer/home/'
	ct = Cart.objects.count()
	try:
		c = Cart(user= uobj,product = pobj)
		c.save()
		
	except:
		return HttpResponse('<script> alert("Product is already added in your cart.");\
		window.location="%s"</script>'%url)

	return HttpResponse('<script> alert("Product is Successfully added in your cart.");\
	window.location="%s"</script>'%url)
	
	return redirect('/buyer/home/', {'count': ct})

def cartdetails(request):
	pobj = Profile.objects.get(user__username=request.user)
	cartobj = Cart.objects.filter(user_id=pobj.id)
	ct = Cart.objects.count()
	proItems = []
	for i in cartobj:
		proItems.append(Products.objects.get(id=i.product_id))
	return render(request,'CartDetails.html',{'added_product': proItems , 'count': ct})


def profile(request):
	ct = Cart.objects.count()
	if request.method == 'POST':
		nm = request.POST['name']
		mob = request.POST['mobile']
		pincode = request.POST['pincode']
		loc = request.POST['locality']
		add = request.POST['address']
		city = request.POST['city']
		state = request.POST['state']
		landmark = request.POST['landmark']
		uobj = Profile.objects.get(user__username=request.user)
		a = Address(user=uobj,name=nm,mobile=mob,pincode=pincode,locality=loc,address=add,city=city,state=state,landmark=landmark)
		a.save()
		return redirect('/buyer/profile/', {'count':ct})

	return render(request,'buyerprofile.html', {'count':ct})

def cartcalculate(request):
	q = request.POST.getlist('productqty')
	price = request.POST.getlist('price')
	pid = request.POST.getlist('pid')
	ct = Cart.objects.count()
	sum = 0
	pobj = Profile.objects.get(user__username=request.user)
	for i in range(len(q)):
		amt = int(q[i])*float(price[i])
		sum = sum + amt
		#Update Stock
		updatePro = Products.objects.filter(id=pid[i])
		updatedqty = updatePro[0].qty - int(q[i])
		updatePro.update(qty = updatedqty)
	cartobj = Cart.objects.filter(user_id=pobj.id)
	cartobj.delete()
	
	return redirect('/buyer/cartdetail/', {'count':ct})

def cartdelete(request,id):
	ct = Cart.objects.count()
	pobj = Products.objects.get(id=id)
	uobj = Profile.objects.get(user__username=request.user)

	c = Cart.objects.get(user=uobj,product=pobj)
	c.delete()
	return redirect('/buyer/cartdetail/', {'count':ct})
