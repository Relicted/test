from django.db.models.signals import post_save
from django.dispatch import receiver

from apps.todo.models import Column
from apps.accounts.models import User


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:

        print('GOGO POWER RANGERS')
        Column.objects.bulk_create([
            Column(name='TODO', user=instance),
            Column(name='In Progress', user=instance),
            Column(name='Done', user=instance),
        ])
