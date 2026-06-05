from django.contrib import admin
from .models import Profile, Project, Skill, SocialLink, Resume, ContactMessage

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'location', 'updated_at']
    search_fields = ['name', 'email']

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'featured', 'created_date']
    list_filter = ['category', 'featured', 'created_date']
    search_fields = ['title', 'description', 'tech_stack']
    ordering = ['-created_date']

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'icon']
    list_filter = ['category']
    search_fields = ['name']

@admin.register(SocialLink)
class SocialLinkAdmin(admin.ModelAdmin):
    list_display = ['platform_name', 'url', 'order']
    ordering = ['order']

@admin.register(Resume)
class ResumeAdmin(admin.ModelAdmin):
    list_display = ['uploaded_date', 'is_active']
    list_filter = ['is_active']

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'created_date', 'is_read']
    list_filter = ['is_read', 'created_date']
    search_fields = ['name', 'email', 'message']
    readonly_fields = ['name', 'email', 'message', 'created_date']