from django.contrib import admin
from .models import Member

admin.site.site_header = 'Fosmos - Administration'


# Register your models here.
class MemberAdmin(admin.ModelAdmin):
    list_display = [
        'first_name',  'last_name', 
    ]
    list_filter = ['education', ]
    search_fields = ['first_name', 'last_name', "phone_number"]


admin.site.register(Member, MemberAdmin)