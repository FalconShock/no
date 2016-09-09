from django.contrib import admin

from .models import info_form
from .forms import info_form_form

class info_form_admin(admin.ModelAdmin):
    list_display = ['__unicode__','Reg','email', 'cc_myself']
    form = info_form_form
#    class Meta: model = info_form

admin.site.register(info_form, info_form_admin)
