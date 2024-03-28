from django.db import models
from User.models import user_m
# Create your models here.

class list_m(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50, null=True, blank=True)
    description = models.CharField(max_length=255, null=True, blank=True)
    user_id = models.ForeignKey(user_m, on_delete = models.CASCADE)
    board_id = models.ForeignKey('Board.board_m', on_delete =models.CASCADE)