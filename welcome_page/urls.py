from django.urls import path
from . import views
urlpatterns = [
    path('', views.set_number),
    path('guess', views.set_guess),
    path('reset', views.reset_game)
]
