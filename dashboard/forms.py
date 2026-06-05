from django import forms
from user.models import Profile, Project, Skill, SocialLink, Resume

class ProfileForm(forms.ModelForm):
    role_titles = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 3, 'placeholder': 'Enter role titles separated by commas'}),
        help_text="Enter role titles separated by commas (e.g., Full Stack Developer, Django Developer)"
    )

    class Meta:
        model = Profile
        fields = ['name', 'role_titles', 'bio', 'profile_image', 'email', 'phone', 'location']
        widgets = {
            'bio': forms.Textarea(attrs={'rows': 4}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance and self.instance.role_titles:
            roles = self.instance.role_titles
            if isinstance(roles, list):
                self.fields['role_titles'].initial = ', '.join(str(r) for r in roles)
            else:
                self.fields['role_titles'].initial = str(roles)
                
        for name, field in self.fields.items():
            if not isinstance(field.widget, forms.CheckboxInput):
                field.widget.attrs.update({'class': 'form-control'})

    def clean_role_titles(self):
        role_titles = self.cleaned_data.get('role_titles', '')
        # Clean up any accidental brackets or quotes the user might type
        role_titles = role_titles.replace('[', '').replace(']', '').replace('"', '').replace("'", "")
        return [title.strip() for title in role_titles.split(',') if title.strip()]

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'description', 'tech_stack', 'image', 'github_link', 'live_link', 'category', 'featured']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
            'tech_stack': forms.TextInput(attrs={'placeholder': 'e.g., Python, Django, React'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            if isinstance(field.widget, forms.CheckboxInput):
                field.widget.attrs.update({'class': 'form-check-input'})
            elif isinstance(field.widget, forms.Select):
                field.widget.attrs.update({'class': 'form-select'})
            else:
                field.widget.attrs.update({'class': 'form-control'})

class SkillForm(forms.ModelForm):
    class Meta:
        model = Skill
        fields = ['name', 'category', 'icon']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            if isinstance(field.widget, forms.Select):
                field.widget.attrs.update({'class': 'form-select'})
            else:
                field.widget.attrs.update({'class': 'form-control'})

class SocialLinkForm(forms.ModelForm):
    class Meta:
        model = SocialLink
        fields = ['platform_name', 'url', 'icon', 'order']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            if isinstance(field.widget, forms.Select):
                field.widget.attrs.update({'class': 'form-select'})
            else:
                field.widget.attrs.update({'class': 'form-control'})

class ResumeForm(forms.ModelForm):
    class Meta:
        model = Resume
        fields = ['resume_file', 'is_active']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            if isinstance(field.widget, forms.CheckboxInput):
                field.widget.attrs.update({'class': 'form-check-input'})
            else:
                field.widget.attrs.update({'class': 'form-control'})