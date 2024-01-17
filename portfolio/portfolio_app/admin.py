from django.contrib import admin
from .models import Contact, Portfolio, Resume,Rate, Portfoliocategory, Resume_details,Resume_responsibility, About, Skills
# Register your models here.

class contact_admin(admin.ModelAdmin):
    list_display = ["name", 'email', 'subject', 'created']
    search_fields =  ["name", 'email', 'subject']
    list_per_page = 6

def approve_ref(modeladmin, request, queryset):
    queryset.update(approve=True)

class CommentAdmin(admin.ModelAdmin):
    actions = [approve_ref]

admin.site.register(Contact, contact_admin),
admin.site.register(Portfolio)
admin.site.register(Resume)
admin.site.register(Resume_details)
admin.site.register(Resume_responsibility)
admin.site.register(Portfoliocategory)
admin.site.register(Rate)  
admin.site.register(Skills)  
admin.site.register(About)  
 