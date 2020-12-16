from django.urls import path

from salesman.api.v1.views import CreateSalesmanView

app_name = "salesman"

urlpatterns = [
    path("create-salesman/", CreateSalesmanView.as_view(), name="create-salesman"),
]
