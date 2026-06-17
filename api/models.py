from django.db import models

from .validators import cv_file_validator, logo_file_validator


class Profile(models.Model):
    profile_image = models.ImageField(upload_to='profile/', blank=True, null=True)

    class Meta:
        verbose_name = 'Profile Picture'
        verbose_name_plural = 'Profile Picture'

    def __str__(self):
        return 'Profile Picture'


class Skill(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    icon = models.CharField(max_length=50, blank=True)
    image = models.FileField(
        upload_to='skills/',
        blank=True,
        validators=[logo_file_validator],
    )
    image_url = models.URLField(blank=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title


class Certificate(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField(blank=True)
    icon = models.CharField(max_length=50, blank=True)
    image = models.FileField(
        upload_to='certificates/',
        blank=True,
        validators=[logo_file_validator],
    )
    image_url = models.URLField(blank=True)
    download_url = models.URLField(blank=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title


class Experience(models.Model):
    role = models.CharField(max_length=150)
    company = models.CharField(max_length=150)
    location = models.CharField(max_length=100, blank=True)
    start_date = models.CharField(max_length=50)
    end_date = models.CharField(max_length=50, blank=True)
    is_current = models.BooleanField(default=False)
    description = models.TextField()
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']
        verbose_name_plural = 'experiences'

    def __str__(self):
        return f'{self.role} at {self.company}'


class Project(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    image_url = models.URLField(blank=True)
    project_url = models.URLField(blank=True)
    github_url = models.URLField(blank=True)
    status = models.CharField(
        max_length=20,
        choices=[('completed', 'Completed'), ('pending', 'Under Development')],
        default='completed',
    )
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title


class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.name} - {self.subject}'


class Resume(models.Model):
    title = models.CharField(max_length=100, default='Resume')
    file = models.FileField(upload_to='cv/', validators=[cv_file_validator])
    is_active = models.BooleanField(default=False)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-uploaded_at']

    def __str__(self):
        status = 'Active' if self.is_active else 'Inactive'
        return f'{self.title} ({status})'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.is_active:
            Resume.objects.exclude(pk=self.pk).update(is_active=False)
