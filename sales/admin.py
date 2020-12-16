from django.contrib import admin

from sales.models import Sale


class SalesAdmin(admin.ModelAdmin):
    list_display = ("salesman", "status")
    search_fields = [
        "salesman__cpf",
    ]


admin.site.register(Sale, SalesAdmin)
