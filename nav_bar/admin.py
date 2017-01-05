from django.contrib import admin
from nav_bar.models import NavButton, NavLogo

admin.site.register(NavButton)

class NavLogoAdmin(admin.ModelAdmin):
     def has_add_permission(self, request):
		add_button = bool
		query_set = NavLogo.objects.all()
		if query_set.count() == 0:
			add_button = True
		else:
			add_button = False
		return add_button 
admin.site.register(NavLogo, NavLogoAdmin)
