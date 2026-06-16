from django.contrib import admin

from .models import Certificate, ContactMessage, Experience, Profile, Project, Resume, Skill


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['profile_image']
    fields = ['profile_image']

    def has_add_permission(self, request):
        return not Profile.objects.exists()


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ['title', 'order']
    list_editable = ['order']
    fields = ['title', 'description', 'image', 'image_url', 'icon', 'order']


@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    list_display = ['title', 'order']
    list_editable = ['order']
    fields = ['title', 'description', 'image', 'image_url', 'icon', 'download_url', 'order']


@admin.register(Resume)
class ResumeAdmin(admin.ModelAdmin):
    list_display = ['title', 'is_active', 'uploaded_at']
    list_filter = ['is_active']
    list_editable = ['is_active']
    readonly_fields = ['uploaded_at']
    fields = ['title', 'file', 'is_active', 'uploaded_at']

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        if obj.is_active:
            Resume.objects.exclude(pk=obj.pk).update(is_active=False)


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ['role', 'company', 'start_date', 'end_date', 'is_current', 'order']
    list_editable = ['order', 'is_current']
    list_filter = ['is_current']


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'status', 'order']
    list_editable = ['order', 'status']
    list_filter = ['status']


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject', 'created_at', 'is_read']
    list_filter = ['is_read', 'created_at']
    readonly_fields = ['created_at']
