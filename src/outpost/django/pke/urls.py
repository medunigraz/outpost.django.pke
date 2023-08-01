from django.conf.urls import url

from . import views

app_name = "pke"

urlpatterns = [
    url(r"^xml$", views.XMLView.as_view(), name="xml"),
    url(r"^schema$", views.SchemaView.as_view(), name="schema"),
]
