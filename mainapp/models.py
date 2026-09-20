from django.db import models

# Create your models here.

class Skill(models.Model):
    CATEGORY_CHOICES = [
        ('FRONTEND', 'Frontend'),
        ('BACKEND', 'Backend'),
        ('DATABASE', 'Base de données & Cloud'),
        ('TOOLS', 'Outils & Méthodologies'),
    ]

    name = models.CharField(max_length=50)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    order = models.IntegerField(default=0, help_text="Ordre d'affichage")

    class Meta:
        ordering = ['order', 'name']

    def __str__(self):
        return f"{self.name} ({self.get_category_display()})"


class Project(models.Model):
    title = models.CharField(max_length=120)
    slug = models.SlugField(unique=True)
    subtitle = models.CharField(max_length=255, help_text="Ex: PWA de gestion / SPA E-commerce")
    description = models.TextField(help_text="Problème résolu et valeur ajoutée du projet")
    architecture_details = models.TextField(blank=True, help_text="Détails techniques (Ex: Auth JWT, PWA offline, REST API)")
    
    image = models.ImageField(upload_to='projects/', blank=True, null=True)
    skills = models.ManyToManyField(Skill, related_name='projects')
    
    github_url = models.URLField(blank=True, null=True)
    live_url = models.URLField(blank=True, null=True)
    
    is_featured = models.BooleanField(default=False, help_text="Afficher en premier")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-is_featured', '-created_at']

    def __str__(self):
        return self.title


class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message de {self.name} - {self.subject}"