from django.contrib import admin
from .forms import StockCreateForm
# Register your models here.
from .models import Stock

class StackCreateAdmin(admin.ModelAdmin):
    list_display = ['category','item_name','quantity','issue_by']
    form = StockCreateForm
    search_fields = ['category','item_name']
    list_filter = ['category']

admin.site.register(Stock,StackCreateAdmin)