
# Register your models here.
# mainapp/admin.py
from django.contrib import admin
from .models import Project, ContactMessage, Skill


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'subtitle', 'github_url', 'live_url')
    search_fields = ('title', 'description')
    # Génère automatiquement le slug à partir du champ 'title' dans l'admin
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Skill)
admin.site.register(ContactMessage)