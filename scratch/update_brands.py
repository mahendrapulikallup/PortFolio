import os

dir_path = "templates/dashboard"
for filename in os.listdir(dir_path):
    if filename.endswith(".html"):
        filepath = os.path.join(dir_path, filename)
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Replace MahiCodeX Dashboard brand
        content = content.replace(
            'class="navbar-brand" href="{% url \'dashboard:home\' %}">MahiCodeX Dashboard</a>',
            'class="navbar-brand text-green neon-text-glow" href="{% url \'dashboard:home\' %}">CodeX Dashboard</a>'
        )
        # Replace generic Dashboard brand
        content = content.replace(
            'class="navbar-brand" href="{% url \'dashboard:home\' %}">Dashboard</a>',
            'class="navbar-brand text-green neon-text-glow" href="{% url \'dashboard:home\' %}">CodeX Dashboard</a>'
        )
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
print("Dashboard brands updated successfully!")
