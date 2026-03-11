from django.db import models

class Chantier(models.Model):
    nom = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    date_debut = models.DateField()
    date_fin = models.DateField(blank=True, null=True)
    
    def __str__(self):
        return self.nom
