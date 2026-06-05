from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from .models import Profile, Project, Skill, SocialLink, Resume, ContactMessage
from .forms import ContactForm

def index(request):
    """Main portfolio page"""
    # Use the same profile record managed by the dashboard (pk=1) if it exists.
    profile = Profile.objects.filter(pk=1).first() or Profile.objects.first()

    projects = Project.objects.filter(featured=True)
    skills = Skill.objects.all()
    social_links = SocialLink.objects.all()
    active_resume = Resume.objects.filter(is_active=True).first()

    # Group skills by category
    skills_by_category = {}
    for skill in skills:
        if skill.category not in skills_by_category:
            skills_by_category[skill.category] = []
        skills_by_category[skill.category].append(skill)

    context = {
        'profile': profile,
        'projects': projects,
        'skills_by_category': skills_by_category,
        'social_links': social_links,
        'active_resume': active_resume,
        'contact_form': ContactForm(),
    }

    return render(request, 'user/index.html', context)

def project_detail(request, pk):
    """Individual project detail page"""
    project = get_object_or_404(Project, pk=pk)
    tech_list = [t.strip() for t in project.tech_stack.split(',')] if project.tech_stack else []
    return render(request, 'user/project_detail.html', {'project': project, 'tech_list': tech_list})

def contact(request):
    """Handle contact form submission"""
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact_message = form.save()
            messages.success(request, 'Thank you for your message! I will get back to you soon.')

            # Optional: Send email notification
            # send_mail(
            #     f'New Contact Message from {contact_message.name}',
            #     contact_message.message,
            #     contact_message.email,
            #     [settings.DEFAULT_FROM_EMAIL],
            #     fail_silently=True,
            # )

            return render(request, 'user/contact_success.html')
    else:
        form = ContactForm()

    return render(request, 'user/contact.html', {'form': form})

def download_resume(request):
    """Download the active resume"""
    resume = get_object_or_404(Resume, is_active=True)
    response = HttpResponse(resume.resume_file, content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="{resume.resume_file.name.split("/")[-1]}"'
    return response