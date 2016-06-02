from django.db import models
from django.conf import settings

# Create your models here.
class Casier(models.Model):
		# id = models.AutoField(primary_key=True)
		user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
		email = models.EmailField(help_text = u"L'email de confirmation sera envoyé à cette adresse, également utilisé comme identifiant.",verbose_name = "Courriel")
		pseudo = models.CharField(max_length=20)
		libre = models.BooleanField(default=True)
		objet = models.CharField(max_length=100, blank=True)
		date = models.DateTimeField(verbose_name='Date de demande',
                                	auto_now_add=True)

		def __unicode__(self):
			return self.nom_casier

