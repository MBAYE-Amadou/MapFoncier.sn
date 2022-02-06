from django.urls import path
from .views import HomePageView

urlpatterns = [
	path('application/', HomePageView.as_view(), name = 'application'),

]
