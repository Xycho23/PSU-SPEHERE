from django.contrib import admin
from .models import College, Program, Organization, Student, OrgMember

# Customize the admin display for the College model
class CollegeAdmin(admin.ModelAdmin):
    list_display = ('college_name', 'created_at', 'updated_at')
    search_fields = ('college_name',)

# Customize the admin display for the Program model
class ProgramAdmin(admin.ModelAdmin):
    list_display = ('prog_name', 'college', 'created_at', 'updated_at')
    list_filter = ('college',)
    search_fields = ('prog_name',)

# Customize the admin display for the Organization model
class OrganizationAdmin(admin.ModelAdmin):
    list_display = ('name', 'college', 'created_at', 'updated_at')
    list_filter = ('college',)
    search_fields = ('name', 'description')

# Customize the admin display for the Student model
class StudentAdmin(admin.ModelAdmin):
    list_display = ('student_id', 'lastname', 'firstname', 'program', 'created_at', 'updated_at')
    list_filter = ('program',)
    search_fields = ('lastname', 'firstname', 'student_id')

# Customize the admin display for the OrgMember model
class OrgMemberAdmin(admin.ModelAdmin):
    list_display = ('student', 'organization', 'date_joined', 'created_at', 'updated_at')
    list_filter = ('organization', 'date_joined')
    search_fields = ('student__lastname', 'student__firstname', 'organization__name')

# Register the models with the admin site
admin.site.register(College, CollegeAdmin)
admin.site.register(Program, ProgramAdmin)
admin.site.register(Organization, OrganizationAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(OrgMember, OrgMemberAdmin)
