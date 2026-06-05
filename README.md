# MahicodeX Portfolio - Django Dynamic Portfolio System

A comprehensive, dynamic personal portfolio website built with Django that allows admin users to manage content through a dedicated dashboard while providing a beautiful, responsive public interface for visitors.

## 🚀 Features

### Public Portfolio
- **Hero Section** with animated typing roles
- **About Section** with profile information
- **Skills Section** organized by categories (Frontend, Backend, Database, AI/ML)
- **Projects Section** showcasing featured work
- **Social Links** integration
- **Contact Form** for visitor messages
- **Resume Download** functionality
- Fully responsive design

### Admin Dashboard
- **Profile Management** - Update personal information and role titles
- **Project Management** - Add, edit, delete, and feature projects
- **Skills Management** - Organize skills by categories
- **Social Links Management** - Manage social media presence
- **Resume Management** - Upload and manage resume files
- **Contact Messages** - View and manage visitor inquiries
- Secure authentication required

## 🛠 Tech Stack

- **Backend**: Django 4.2, Python
- **Database**: SQLite (development) / PostgreSQL (production)
- **Frontend**: HTML5, CSS3, JavaScript, Bootstrap 5
- **Icons**: Font Awesome
- **Media Handling**: Pillow

## 📁 Project Structure

```
mahicodeX_portfolio/
├── mahicodeX_portfolio/          # Main Django project
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── user/                         # Public portfolio app
│   ├── models.py                 # Database models
│   ├── views.py                  # Public views
│   ├── urls.py                   # URL routing
│   ├── forms.py                  # Contact forms
│   └── admin.py                  # Admin registration
├── dashboard/                    # Admin dashboard app
│   ├── views.py                  # Dashboard views
│   ├── urls.py                   # Dashboard URLs
│   ├── forms.py                  # Management forms
│   └── models.py                 # (Uses user models)
├── templates/                    # HTML templates
│   ├── base.html
│   └── user/
│       └── index.html
├── static/                       # Static files
│   ├── css/
│   ├── js/
│   └── images/
├── media/                        # User uploads
└── requirements.txt
```

## 🗄 Database Models

### Profile
- Personal information, bio, role titles for animation

### Project
- Title, description, tech stack, images, links, categories

### Skill
- Name, category, icon (organized by Frontend/Backend/Database/AI-ML)

### SocialLink
- Platform name, URL, icon, display order

### Resume
- File upload with active status management

### ContactMessage
- Visitor inquiries with read status

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- pip package manager

### Installation

1. **Clone and navigate to the project:**
   ```bash
   cd mahicodeX_portfolio
   ```

2. **Create virtual environment:**
   ```bash
   python -m venv venv
   venv\Scripts\activate  # Windows
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run migrations:**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Create superuser:**
   ```bash
   python manage.py createsuperuser
   ```

6. **Run development server:**
   ```bash
   python manage.py runserver
   ```

7. **Access the application:**
   - Public Portfolio: http://127.0.0.1:8000/
   - Admin Dashboard: http://127.0.0.1:8000/dashboard/
   - Django Admin: http://127.0.0.1:8000/admin/

## 🔐 Authentication

- **Default Admin Credentials:**
  - Username: `admin`
  - Password: `admin123`

- **Dashboard Access:** `/dashboard/login/`
- **Logout:** `/dashboard/logout/`

## 🎨 Customization

### Adding New Skills
1. Navigate to Dashboard → Skills
2. Add skills with appropriate categories and Font Awesome icons

### Managing Projects
1. Go to Dashboard → Projects
2. Upload project images to `media/projects/`
3. Mark projects as "featured" for homepage display

### Updating Profile
1. Access Dashboard → Profile
2. Update role titles (comma-separated for animation)
3. Upload profile image to `media/profile/`

### Social Links
1. Dashboard → Social Links
2. Use Font Awesome icon classes (e.g., `fab fa-github`)
3. Set display order for arrangement

## 📱 Responsive Design

The portfolio is fully responsive and optimized for:
- Desktop computers
- Tablets
- Mobile devices
- Different screen sizes

## 🔒 Security Features

- Admin-only dashboard access
- CSRF protection on forms
- Secure file uploads
- Input validation
- SQL injection prevention

## 🚀 Deployment

### For Production:

1. **Update settings.py:**
   ```python
   DEBUG = False
   SECRET_KEY = 'your-production-secret-key'
   ALLOWED_HOSTS = ['yourdomain.com']
   ```

2. **Use PostgreSQL:**
   ```python
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.postgresql',
           'NAME': 'your_db_name',
           'USER': 'your_db_user',
           'PASSWORD': 'your_db_password',
           'HOST': 'localhost',
           'PORT': '5432',
       }
   }
   ```

3. **Collect static files:**
   ```bash
   python manage.py collectstatic
   ```

4. **Use a production server:**
   - Gunicorn + Nginx
   - Apache + mod_wsgi
   - Docker deployment

## 🔄 Future Enhancements

- AI-powered resume analyzer
- Blog system integration
- Analytics dashboard
- GitHub API integration
- Dark/Light theme toggle
- Multi-language support
- SEO optimization
- Performance monitoring

## 📄 License

This project is open source and available under the MIT License.

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📞 Support

For questions or issues:
- Create an issue on GitHub
- Contact: contact@mahicodeX.dev

---

**Built with ❤️ by MahicodeX**