from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from .models import Project, Skill, ContactMessage

def index(request):
    projects = Project.objects.prefetch_related('skills').all()
    skills = Skill.objects.all()
    
    context = {
        'projects': projects,
        'skills': skills,
    }
    return render(request, 'mainapp/index.html', context)


@require_POST
def contact_ajax(request):
    name = request.POST.get('name', '').strip()
    email = request.POST.get('email', '').strip()
    subject = request.POST.get('subject', '').strip()
    message = request.POST.get('message', '').strip()

    # Vérification des champs requis
    if name and email and message:
        try:
            ContactMessage.objects.create(
                name=name,
                email=email,
                subject=subject,
                message=message
            )
            return JsonResponse({
                'status': 'success',
                'message': 'Message envoyé avec succès !'
            })
        except Exception as e:
            return JsonResponse({
                'status': 'error',
                'message': 'Une erreur est survenue lors de l\'enregistrement de votre message.'
            }, status=500)
    
    return JsonResponse({
        'status': 'error',
        'message': 'Veuillez remplir tous les champs obligatoires.'
    }, status=400)

#Project detail view
def project_detail(request, pk):
    # Récupère le projet ou renvoie une erreur 404
    project = get_object_or_404(Project.objects.prefetch_related('skills'), pk=pk)
    
    # Récupère 2 autres projets pour la section "Projets similaires / Autres projets"
    other_projects = Project.objects.exclude(pk=pk)[:2]
    
    context = {
        'project': project,
        'other_projects': other_projects,
    }
    return render(request, 'mainapp/project_detail.html', context)