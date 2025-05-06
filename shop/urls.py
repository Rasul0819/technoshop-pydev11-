from django.urls import path
from  . import views

urlpatterns = [
    path('',views.HomePageView.as_view(),name='home'),
    path('contact/',views.contactus,name='contact'),
    path('registration/',views.registration,name='regis'),
    path('login/',views.sing_in,name='login'),
    path('searchresults/',views.product_search,name='product_search')

]