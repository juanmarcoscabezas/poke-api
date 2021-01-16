from django.db import models

class Pokemon(models.Model):
    name = models.CharField(max_length=200)
    height = models.CharField(max_length=50)
    weight = models.CharField(max_length=50)
    image = models.CharField(max_length=1024, default='')
    # Stats
    hp = models.IntegerField()
    attack = models.IntegerField()
    defense = models.IntegerField()
    special_attack = models.IntegerField()
    special_defense = models.IntegerField()
    speed = models.IntegerField()
    # Parent
    evolves_from = models.ForeignKey("self",
        blank=True,
        null=True, on_delete=models.DO_NOTHING
    )
    