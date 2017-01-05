from django.contrib import admin
from company.models import Contact, Service, Position, Employee, Company

admin.site.register(Position)
admin.site.register(Employee)
admin.site.register(Service)
admin.site.register(Contact)

class CompanyAdmin(admin.ModelAdmin):
     def has_add_permission(self, request):
		add_button = bool
		query_set = Company.objects.all()
		if query_set.count() == 0:
			add_button = True
		else:
			add_button = False
		return add_button 
admin.site.register(Company, CompanyAdmin)
