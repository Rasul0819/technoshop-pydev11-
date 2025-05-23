from django.urls import path
from  . import views

urlpatterns = [
    path('',views.HomePageView.as_view(),name='home'),
    path('contact/',views.contactus,name='contact'),
    path('registration/',views.registration,name='regis'),
    path('login/',views.sing_in,name='login'),
    path('searchresults/',views.product_search,name='product_search'),
    path('verify/<int:user_id>',views.verify_code,name='verify_code'),
    path('cart/',views.cart,name='cart'),
    path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),

]