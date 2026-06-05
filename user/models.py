from django.db import models
from django.utils import timezone

class Profile(models.Model):
    name = models.CharField(max_length=100)
    role_titles = models.JSONField(default=list, help_text="List of role titles for animation")
    bio = models.TextField()
    profile_image = models.ImageField(upload_to='profile/', blank=True, null=True)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True)
    location = models.CharField(max_length=100, blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'

class Project(models.Model):
    CATEGORY_CHOICES = [
        ('web', 'Web Development'),
        ('ml', 'Machine Learning'),
        ('mobile', 'Mobile App'),
        ('other', 'Other'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()
    tech_stack = models.CharField(max_length=500, help_text="Comma-separated technologies")
    image = models.ImageField(upload_to='projects/', blank=True, null=True)
    github_link = models.URLField(blank=True)
    live_link = models.URLField(blank=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='web')
    featured = models.BooleanField(default=False)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_date']

class Skill(models.Model):
    CATEGORY_CHOICES = [
        ('frontend', 'Frontend'),
        ('backend', 'Backend'),
        ('database', 'Database'),
        ('ai_ml', 'AI/ML'),
        ('tools', 'Tools & Others'),
    ]

    name = models.CharField(max_length=100)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    icon = models.CharField(max_length=50, blank=True, help_text="FontAwesome icon class")

    def __str__(self):
        return f"{self.name} ({self.category})"

    class Meta:
        ordering = ['category', 'name']

class SocialLink(models.Model):
    platform_name = models.CharField(max_length=50)
    url = models.URLField()
    icon = models.CharField(max_length=50, blank=True, help_text="FontAwesome icon class")
    order = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.platform_name

    class Meta:
        ordering = ['order']

class Resume(models.Model):
    resume_file = models.FileField(upload_to='resumes/')
    uploaded_date = models.DateTimeField(default=timezone.now)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return f"Resume uploaded on {self.uploaded_date}"

    class Meta:
        ordering = ['-uploaded_date']

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f"Message from {self.name}"

    class Meta:
        ordering = ['-created_date']