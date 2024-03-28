from django.db import models

# Create your models here.
class Board_m (models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField( max_length=50, null=True, blank=True)
    description = models.TextField(max_length=1200, null=True, blank=True)
    project_id = models.ForeignKey('Ticket.project_m', on_delete = models.CASCADE)


class Label_m(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50, null=True, blank=True)
    board_id = models.ForeignKey(Board_m, on_delete=models.CASCADE)