from django.urls import  path
from . import views
urlpatterns = [
    path('login/', views.login_view, name='login-auth'),
    path('adminchoice/', views.infogestion_view, name='admin_choice'),
    path('demande/', views.admindemande_view, name='demande'),
    path('demandebis/', views.admindemandebis_view, name='demandebis'),
    path('supprimer_demande/<str:pk>', views.deletedemande_view, name='supprimer_demande'),
    path('update_demande/<str:pk>', views.updatedemande_view, name='update_demande'),
    path('update_demandebis/<str:pk>', views.updatedemandebis_view, name='update_demandebis'),
    path('supprimer_demandebis/<str:pk>', views.deletedemandebis_view, name='supprimer_demandebis'),
    
]
