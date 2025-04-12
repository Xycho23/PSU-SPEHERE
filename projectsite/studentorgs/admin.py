from django.contrib import admin
from .models import College, Program, Organization, Student, OrgMember  # Changed Organizations to Organization

admin.site.register(College)
admin.site.register(Program)
admin.site.register(Organization)

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ("student_id", "lastname",
                    "firstname", "middlename", "program")
    search_fields = ("lastname", "firstname",)

@admin.register(OrgMember)
class OrgMemberAdmin(admin.ModelAdmin):
    list_display = ['id', 'student', 'get_organization', 'date_joined']
    
    def get_organization(self, obj):
        return obj.organization.name
    get_organization.short_description = 'Organization'