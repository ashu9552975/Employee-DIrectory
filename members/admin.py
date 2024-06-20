from django.contrib import admin
from .models import Department,Role,Member,Admin



class MemberAdmin(admin.ModelAdmin):
  list_display = ("name","employee_id","department", "role",)
  
admin.site.register(Department)
admin.site.register(Role)
admin.site.register(Admin)
admin.site.register(Member, MemberAdmin)