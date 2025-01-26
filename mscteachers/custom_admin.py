from django.contrib.admin import AdminSite

class CustomAdminSite(AdminSite):
    site_header = "MSc Teachers & Experts Database"
    site_title = "MSc Thesis Document Generation"
    index_title = "Welcome!"

# Create a single instance to be used project-wide
custom_admin_site = CustomAdminSite(name='custom_admin')