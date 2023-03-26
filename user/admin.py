from django.contrib import admin

# Register your models here.
from . models import *

class productAdmin(admin.ModelAdmin):
    list_display = ('id','category','subcategory','name','price','disprice','color','size','description','date','ppic')
admin.site.register(product,productAdmin)

class subcategoryAdmin(admin.ModelAdmin):
    list_display = ('id','name','date')
admin.site.register(subcategory,subcategoryAdmin)

admin.site.register(contactinfo)
admin.site.register(order)
admin.site.register(signup)
