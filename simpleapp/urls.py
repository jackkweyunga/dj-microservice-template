from django.urls import path
import simpleapp.views as views

urlpatterns = [
    path("hello/", views.SimpleAppView.as_view())
]
