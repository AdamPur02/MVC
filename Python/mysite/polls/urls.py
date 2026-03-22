from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
<<<<<<< HEAD
]
=======
    path("<int:question_id>/", views.detail, name="detail"),
>>>>>>> main
