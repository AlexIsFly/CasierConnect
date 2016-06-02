from django.contrib import admin
from .models import Casier
# Register your models here.



class CasierAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'libre', 'objet', 'date')
    # list_filter = ('jour', 'heure', 'statut')
    # date_hierarchy = 'date'
    # ordering = ('date', )
    # search_fields = ('nom', 'commentaire', 'nom', 'prenom')
    # fieldsets = (
    #     ('Statut', {
    #        'fields': ('statut',)
    #     }),
    #     ('Infos Personelles', {
    #        'fields': ('nom', 'prenom', 'adresse', 'tel1', 'tel2', 'digicode', 'etage', 'appartement',)
    #     }),
    #     ('Commande', {
    #        'fields': ('jour', 'heure', 'lasagnes', 'tartiflette',
    #                   'burger', 'chili', 'rougail', 'pouletcurry',
    #                   'fondant', 'dessertliste', 'dejsucre', 'dejsale')
    #     }),
    #     ('Commentaire', {
    #         'classes': ['wide', 'pretty', ],
    #         'fields': ('commentaire',)
    #     }),
    # )

admin.site.register(Casier, CasierAdmin)
