from django.contrib import admin
from . models import Demandeurs, DemandeursAdmin, DemandeursMoral, DemandeursMoralAdmin
# Register your models here.
admin.site.register(Demandeurs, DemandeursAdmin)

admin.site.register(DemandeursMoral, DemandeursMoralAdmin)
