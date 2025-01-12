from django.db.models import Count
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone

from courses.models import Group
from users.models import Subscription


@receiver(post_save, sender=Subscription)
def post_save_subscription(sender, instance: Subscription, created, **kwargs):
    """
    Распределение нового студента в группу курса.

    """

    if created:
        user = instance.user
        course = instance.course
        groups = Group.objects.filter(course=course)

        for group in groups:
            if user not in group.users.all():
                group.users.add(user)
                group.save()
