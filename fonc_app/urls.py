from django.urls import  path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('about/', views.about_view, name='about'),
    path('contact/', views.contact_view, name='contact'),
    path('information/', views.info_view, name='information'),
    path('formulaire/', views.demande_view, name='formulaire'),
    path('formulairebis/', views.demandebis_view, name='formulairebis'),
    path('search/', views.searchBar_view, name='search'),
    path('verification', views.show_demandeurs, name='verification'),
    path('verifications', views.show_demandeursbis, name='verifications'),
    path('<int:id>', views.generer, name="generer"),
    path('<int:id>/', views.generer_bis, name="generer_bis"), 
    path('download', views.download, name="download"), 
    path('telecharger', views.telecharger, name="telecharger"), 
    
]
    

