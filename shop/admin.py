from django.contrib import admin
from .models import Category,Brand,Product,ContactUs,CustomUser
from django.contrib.auth.admin import UserAdmin
from .forms import RegistrationForm
# Register your models here.


admin.site.register(Category)
admin.site.register(Brand)
admin.site.register(Product)
admin.site.register(ContactUs)


class CustomUserAdmin(UserAdmin):
    add_form=RegistrationForm
    model = CustomUser
    list_display = ['username','email','phone_num']

admin.site.register(CustomUser,CustomUserAdmin)