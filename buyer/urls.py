from django.urls import path
from . import views

app_name = 'buyer'


urlpatterns = [
	path('home/',views.home),
	#path('my_profile/',views.my_profile),
	path('cart/<int:id>/', views.cart, name="cart"),
	path('cartdetail/',views.cartdetails),
	path('profile/',views.profile),
	path('cartcalculate/',views.cartcalculate),
	path('cartdelete/<int:id>/',views.cartdelete, name="delpro"),
	
]