from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'dashboard'

urlpatterns = [
    path('', views.dashboard_home, name='home'),
    path('login/', auth_views.LoginView.as_view(template_name='dashboard/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    # Profile management
    path('profile/', views.manage_profile, name='profile'),

    # Project management
    path('projects/', views.manage_projects, name='projects'),
    path('projects/add/', views.add_project, name='add_project'),
    path('projects/<int:pk>/edit/', views.edit_project, name='edit_project'),
    path('projects/<int:pk>/delete/', views.delete_project, name='delete_project'),

    # Skill management
    path('skills/', views.manage_skills, name='skills'),
    path('skills/add/', views.add_skill, name='add_skill'),
    path('skills/<int:pk>/edit/', views.edit_skill, name='edit_skill'),
    path('skills/<int:pk>/delete/', views.delete_skill, name='delete_skill'),

    # Social links management
    path('social-links/', views.manage_social_links, name='social_links'),
    path('social-links/add/', views.add_social_link, name='add_social_link'),
    path('social-links/<int:pk>/edit/', views.edit_social_link, name='edit_social_link'),
    path('social-links/<int:pk>/delete/', views.delete_social_link, name='delete_social_link'),

    # Resume management
    path('resumes/', views.manage_resumes, name='resumes'),
    path('resumes/add/', views.add_resume, name='add_resume'),
    path('resumes/<int:pk>/delete/', views.delete_resume, name='delete_resume'),

    # Contact messages
    path('messages/', views.manage_messages, name='messages'),
    path('messages/<int:pk>/', views.view_message, name='view_message'),
    path('messages/<int:pk>/delete/', views.delete_message, name='delete_message'),
]