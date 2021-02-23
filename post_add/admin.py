from django.contrib import admin

# Register your models here.
from .models import PostAdd_Car,PostAdd_Fashion, PostAdd_Computer, PostAdd_Phones, PostAdd_LandHouse, PostAdd_Bikes

admin.site.register(PostAdd_Car)

admin.site.register(PostAdd_Fashion)
admin.site.register(PostAdd_Computer)
admin.site.register(PostAdd_Phones)
admin.site.register(PostAdd_LandHouse)
admin.site.register(PostAdd_Bikes)
