from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path

from . import views

app_name = "aboutus"

urlpatterns = [
    path(
        "",
        views.aboutus,
    ),
    path("faq/", views.faq, name="faq"),
]
