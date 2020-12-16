from django.contrib import admin

from salesman.models import Salesman


class SalesmanAdmin(admin.ModelAdmin):
    list_display = ("cpf",)
    search_fields = [
        "cpf",
    ]


admin.site.register(Salesman, SalesmanAdmin)
