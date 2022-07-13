from django.db import models
from User.models import User 

class UserTitle(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.PROTECT)
    id = models.IntegerField('id', primary_key=True)
    title = models.CharField('title' , max_length=50)
    complete = models.BooleanField('complete')

