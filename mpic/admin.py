from django.contrib import admin
from .models import Location, Image, categories

# Register your models here.
 
 class ImgAdmin(admin.ModelAdmin):
     filter_horizontal = ('categories',)

admin.site.register(Location)
admin.site.register(Image,ImgAdmin)
admin.site.register(categories)
