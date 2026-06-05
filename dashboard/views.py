from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse
from user.models import Profile, Project, Skill, SocialLink, Resume, ContactMessage
from .forms import ProfileForm, ProjectForm, SkillForm, SocialLinkForm, ResumeForm

@login_required
def dashboard_home(request):
    """Dashboard home page"""
    context = {
        'total_projects': Project.objects.count(),
        'total_skills': Skill.objects.count(),
        'total_messages': ContactMessage.objects.count(),
        'unread_messages': ContactMessage.objects.filter(is_read=False).count(),
    }
    return render(request, 'dashboard/dashboard.html', context)

@login_required
def manage_profile(request):
    """Manage profile information"""
    profile, created = Profile.objects.get_or_create(pk=1, defaults={'name': 'mahendra pulikallu'})

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully!')
            return redirect('dashboard:profile')
    else:
        form = ProfileForm(instance=profile)

    return render(request, 'dashboard/profile.html', {'form': form, 'profile': profile})

@login_required
def manage_projects(request):
    """List all projects"""
    projects = Project.objects.all()
    return render(request, 'dashboard/projects.html', {'projects': projects})

@login_required
def add_project(request):
    """Add new project"""
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Project added successfully!')
            return redirect('dashboard:projects')
    else:
        form = ProjectForm()

    return render(request, 'dashboard/project_form.html', {'form': form, 'title': 'Add Project'})

@login_required
def edit_project(request, pk):
    """Edit existing project"""
    project = get_object_or_404(Project, pk=pk)

    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            messages.success(request, 'Project updated successfully!')
            return redirect('dashboard:projects')
    else:
        form = ProjectForm(instance=project)

    return render(request, 'dashboard/project_form.html', {'form': form, 'title': 'Edit Project'})

@login_required
def delete_project(request, pk):
    """Delete project"""
    project = get_object_or_404(Project, pk=pk)
    if request.method == 'POST':
        project.delete()
        messages.success(request, 'Project deleted successfully!')
        return redirect('dashboard:projects')

    return render(request, 'dashboard/project_confirm_delete.html', {'project': project})

@login_required
def manage_skills(request):
    """List all skills"""
    skills = Skill.objects.all()
    return render(request, 'dashboard/skills.html', {'skills': skills})

@login_required
def add_skill(request):
    """Add new skill"""
    if request.method == 'POST':
        form = SkillForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Skill added successfully!')
            return redirect('dashboard:skills')
    else:
        form = SkillForm()

    return render(request, 'dashboard/skill_form.html', {'form': form, 'title': 'Add Skill'})

@login_required
def edit_skill(request, pk):
    """Edit existing skill"""
    skill = get_object_or_404(Skill, pk=pk)

    if request.method == 'POST':
        form = SkillForm(request.POST, instance=skill)
        if form.is_valid():
            form.save()
            messages.success(request, 'Skill updated successfully!')
            return redirect('dashboard:skills')
    else:
        form = SkillForm(instance=skill)

    return render(request, 'dashboard/skill_form.html', {'form': form, 'title': 'Edit Skill'})

@login_required
def delete_skill(request, pk):
    """Delete skill"""
    skill = get_object_or_404(Skill, pk=pk)
    if request.method == 'POST':
        skill.delete()
        messages.success(request, 'Skill deleted successfully!')
        return redirect('dashboard:skills')

    return render(request, 'dashboard/skill_confirm_delete.html', {'skill': skill})

@login_required
def manage_social_links(request):
    """List all social links"""
    social_links = SocialLink.objects.all()
    return render(request, 'dashboard/social_links.html', {'social_links': social_links})

@login_required
def add_social_link(request):
    """Add new social link"""
    if request.method == 'POST':
        form = SocialLinkForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Social link added successfully!')
            return redirect('dashboard:social_links')
    else:
        form = SocialLinkForm()

    return render(request, 'dashboard/social_link_form.html', {'form': form, 'title': 'Add Social Link'})

@login_required
def edit_social_link(request, pk):
    """Edit existing social link"""
    social_link = get_object_or_404(SocialLink, pk=pk)

    if request.method == 'POST':
        form = SocialLinkForm(request.POST, instance=social_link)
        if form.is_valid():
            form.save()
            messages.success(request, 'Social link updated successfully!')
            return redirect('dashboard:social_links')
    else:
        form = SocialLinkForm(instance=social_link)

    return render(request, 'dashboard/social_link_form.html', {'form': form, 'title': 'Edit Social Link'})

@login_required
def delete_social_link(request, pk):
    """Delete social link"""
    social_link = get_object_or_404(SocialLink, pk=pk)
    if request.method == 'POST':
        social_link.delete()
        messages.success(request, 'Social link deleted successfully!')
        return redirect('dashboard:social_links')

    return render(request, 'dashboard/social_link_confirm_delete.html', {'social_link': social_link})

@login_required
def manage_resumes(request):
    """List all resumes"""
    resumes = Resume.objects.all()
    return render(request, 'dashboard/resumes.html', {'resumes': resumes})

@login_required
def add_resume(request):
    """Add new resume"""
    if request.method == 'POST':
        form = ResumeForm(request.POST, request.FILES)
        if form.is_valid():
            # If this resume is active, deactivate others
            if form.cleaned_data['is_active']:
                Resume.objects.filter(is_active=True).update(is_active=False)
            form.save()
            messages.success(request, 'Resume added successfully!')
            return redirect('dashboard:resumes')
    else:
        form = ResumeForm()

    return render(request, 'dashboard/resume_form.html', {'form': form, 'title': 'Add Resume'})

@login_required
def delete_resume(request, pk):
    """Delete resume"""
    resume = get_object_or_404(Resume, pk=pk)
    if request.method == 'POST':
        resume.delete()
        messages.success(request, 'Resume deleted successfully!')
        return redirect('dashboard:resumes')

    return render(request, 'dashboard/resume_confirm_delete.html', {'resume': resume})

@login_required
def manage_messages(request):
    """List all contact messages"""
    messages_list = ContactMessage.objects.all()
    return render(request, 'dashboard/messages.html', {'messages': messages_list})

@login_required
def view_message(request, pk):
    """View individual message"""
    message = get_object_or_404(ContactMessage, pk=pk)
    if not message.is_read:
        message.is_read = True
        message.save()

    return render(request, 'dashboard/message_detail.html', {'message': message})

@login_required
def delete_message(request, pk):
    """Delete message"""
    message = get_object_or_404(ContactMessage, pk=pk)
    if request.method == 'POST':
        message.delete()
        messages.success(request, 'Message deleted successfully!')
        return redirect('dashboard:messages')

    return render(request, 'dashboard/message_confirm_delete.html', {'message': message})