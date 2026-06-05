// Portfolio JavaScript functionality

document.addEventListener('DOMContentLoaded', function() {
    // Generic page interactions and smooth scrolling are handled in the page-specific script.

    // Smooth scrolling for navigation links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                const headerOffset = 70;
                const elementPosition = target.offsetTop;
                const offsetPosition = elementPosition - headerOffset;

                window.scrollTo({
                    top: offsetPosition,
                    behavior: 'smooth'
                });
            }
        });
    });

    // Navbar background change on scroll
    const navbar = document.querySelector('.navbar');
    if (navbar) {
        window.addEventListener('scroll', function() {
            if (window.scrollY > 50) {
                navbar.style.backgroundColor = 'rgba(0, 0, 0, 0.95)';
            } else {
                navbar.style.backgroundColor = 'rgba(0, 0, 0, 0.9)';
            }
        });
    }

    // Contact form validation
    const contactForm = document.querySelector('form[action*="contact"]');
    if (contactForm) {
        contactForm.addEventListener('submit', function(e) {
            const name = document.getElementById('id_name');
            const email = document.getElementById('id_email');
            const message = document.getElementById('id_message');

            if (name && name.value.trim() === '') {
                alert('Please enter your name');
                e.preventDefault();
                return;
            }

            if (email && email.value.trim() === '') {
                alert('Please enter your email');
                e.preventDefault();
                return;
            }

            if (message && message.value.trim() === '') {
                alert('Please enter your message');
                e.preventDefault();
                return;
            }

            // Basic email validation
            const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
            if (email && !emailRegex.test(email.value)) {
                alert('Please enter a valid email address');
                e.preventDefault();
                return;
            }
        });
    }

    // Project card hover effects
    const projectCards = document.querySelectorAll('.project-card');
    projectCards.forEach(card => {
        card.addEventListener('mouseenter', function() {
            this.style.transform = 'translateY(-10px)';
        });

        card.addEventListener('mouseleave', function() {
            this.style.transform = 'translateY(0)';
        });
    });

    // Skill category tabs (if implemented)
    const skillTabs = document.querySelectorAll('.skill-tab');
    skillTabs.forEach(tab => {
        tab.addEventListener('click', function() {
            // Remove active class from all tabs
            skillTabs.forEach(t => t.classList.remove('active'));
            // Add active class to clicked tab
            this.classList.add('active');

            // Hide all skill categories
            document.querySelectorAll('.skill-category').forEach(cat => {
                cat.style.display = 'none';
            });

            // Show selected category
            const categoryId = this.getAttribute('data-category');
            document.getElementById(categoryId).style.display = 'block';
        });
    });

    // Initialize tooltips if Bootstrap tooltips are used
    const tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
    if (typeof bootstrap !== 'undefined') {
        tooltipTriggerList.map(function (tooltipTriggerEl) {
            return new bootstrap.Tooltip(tooltipTriggerEl);
        });
    }
});

// Utility functions
function showAlert(message, type = 'info') {
    const alertDiv = document.createElement('div');
    alertDiv.className = `alert alert-${type} alert-dismissible fade show position-fixed`;
    alertDiv.style.cssText = 'top: 20px; right: 20px; z-index: 9999; min-width: 300px;';
    alertDiv.innerHTML = `
        ${message}
        <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
    `;

    document.body.appendChild(alertDiv);

    // Auto remove after 5 seconds
    setTimeout(() => {
        if (alertDiv.parentNode) {
            alertDiv.remove();
        }
    }, 5000);
}

// Copy to clipboard functionality
function copyToClipboard(text) {
    navigator.clipboard.writeText(text).then(function() {
        showAlert('Copied to clipboard!', 'success');
    }, function(err) {
        console.error('Could not copy text: ', err);
        showAlert('Failed to copy to clipboard', 'error');
    });
}