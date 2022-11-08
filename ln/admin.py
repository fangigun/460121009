from django.contrib import admin
from ln.models import Price
# Register your models here.

class PriceAdmin(admin.ModelAdmin):
    list_display= ['title','price']
    list_filter= ['title']
    list_display_links=['title']



class Meta:


    model=Price



    admin.site.register(Price,PriceAdmin)










