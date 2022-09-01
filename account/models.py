from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Relation(models.Model):
    to_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name= 'following')
    from_user = models.ForeignKey(User, on_delete= models.CASCADE, related_name= 'followers')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.to_user} >> {self.from_user}'


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete= models.CASCADE)
    age = models.PositiveSmallIntegerField(default= 0)
    bio = models.TextField(blank=True, null=True)

    




# def create_profile(sender, **kwargs):
#     if kwargs['created']:
#         Profile.objects.create(user= kwargs['instance'])

# post_save.connect(receiver= create_profile, sender= User)

