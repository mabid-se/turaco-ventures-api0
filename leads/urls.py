from django.urls import path
from .views import LeadsListCreate, LeadsRetrieveUpdateDelete

urlpatterns = [
    path("leads/", LeadsListCreate.as_view(), name="leads-list-create"),
    path(
        "leads/<int:pk>/",
        LeadsRetrieveUpdateDelete.as_view(),
        name="lead-detail",
    ),
]
