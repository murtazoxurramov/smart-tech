from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import (ProductCategory, Product, ProductImage, User, UserImage, City)

admin.site.register(ProductCategory)
admin.site.register(Product)
admin.site.register(ProductImage)
admin.site.register(User)
admin.site.register(City)
admin.site.register(UserImage)
