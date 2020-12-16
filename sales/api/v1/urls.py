from django.urls import path

from sales.api.v1.views import CreateSalesView, ListSalesView, ListAccumulatedCashback

app_name = "sales"

urlpatterns = [
    path("create-sale", CreateSalesView.as_view(), name="create-sale"),
    path("list-sales", ListSalesView.as_view(), name="list-sales"),
    path(
        "list-accumulated-cashback",
        ListAccumulatedCashback.as_view(),
        name="list-accumulated-cashback",
    ),
]
