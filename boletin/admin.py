from django.contrib import admin

# Register your models here.
from .forms import RegModelForm
from .models import Registrado

class adminRegistrado(admin.ModelAdmin):
    list_display = ["__str__", "nombre", "timestamp"]
    form = RegModelForm 
    #list_display_links = ["nombre"]
    list_filter = ["timestamp"]
    list_editable = ["nombre"]
    search_fields =  ["__str__", "nombre"]

    #class Meta:
        #model = Registrado

admin.site.register(Registrado, adminRegistrado)


