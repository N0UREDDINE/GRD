from django.contrib import admin
from .models import User, Zone, Category, Agency
# Register your models here.
admin.site.register(User)
admin.site.register(Zone)
admin.site.register(Category)
admin.site.register(Agency)