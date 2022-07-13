from django.db import models

class User(models.Model):
    id = models.AutoField('id', primary_key=True)