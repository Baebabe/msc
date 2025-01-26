# from django.contrib import admin
# from .models import Student,CommonFields, Coordinator, Budget

# # from proposal.models import notice

# # Register your models here.

# admin.site.register(Student)
# # admin.site.register(CommonFields)
# admin.site.register(Coordinator)
# admin.site.register(Budget)

from django.contrib.admin import ModelAdmin
from .models import Student, CommonFields, Coordinator, Budget
from college.admin import admin_site  # Import the custom admin site

# Create admin classes for better control
class StudentAdmin(ModelAdmin):
    pass

class CoordinatorAdmin(ModelAdmin):
    pass

class BudgetAdmin(ModelAdmin):
    pass

# Register with custom admin site
admin_site.register(Student, StudentAdmin)
admin_site.register(Coordinator, CoordinatorAdmin)
admin_site.register(Budget, BudgetAdmin)