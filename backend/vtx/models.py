from django.db import models

class OS(models.Model):
    name = models.CharField("nome",max_length=100)
    description = models.CharField("Descrição",max_length=500)
    create_at = models.DateTimeField(auto_now_add=True)
