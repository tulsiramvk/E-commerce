from django.shortcuts import render,redirect
from EcommerceApp.models import Profile,User
from . models import Category,Products,Photo
from django.utils.datastructures import MultiValueDictKeyError
# Create your views here.
def home(request):
	pobj = Profile.objects.get(user__username = request.user)
	return render(request,'welcomeSeller.html',{'data':pobj})

def add_product(request):
	catobjs = Category.objects.all()

	if request.method == "POST":
		pname = request.POST['pname']
		price = request.POST['price']
		qty = request.POST['qty']
		desc = request.POST['desc']
		pic = request.FILES['pic']
		cat = request.POST['category']
		catobj = Category.objects.get(id=cat)
		uobj = Profile.objects.get(user__username=request.user)

		p = Products(pname=pname,price=price,qty=qty,desc=desc,pic=pic,added_by=uobj,category=catobj)
		p.save()
		return redirect('/seller/add_product/')

	return render(request,'add_product.html', {'cats': catobjs})

def my_profile(request):
	pobj = Profile.objects.get(user__username=request.user)
	uobj = User.objects.get(username=request.user)

	if request.method == 'POST':
		fname = request.POST['fname']
		lname = request.POST['lname']
		profile_pic = request.FILES.get('profile_pic') or pobj.profile_pic
		P = Profile.objects.filter(user__username=request.user)
		U = User.objects.filter(username=request.user)
		U.update(first_name=fname,last_name=lname)
		P.update(profile_pic=profile_pic,)
		return redirect('/seller/my_profile/')

	return render(request,'my_profile.html',{'data':uobj,'data1': pobj})

def images(request):
	if request.method == 'POST':
		pic = request.FILES.getlist('image')
		print(pic)
		for file in pic:
			instance = Photo(
				pics=file
				)
			instance.save()

	return render(request,'imgupload.html')