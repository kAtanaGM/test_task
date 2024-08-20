# Generated by Django 4.2.10 on 2024-08-17 16:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_alter_group_course_alter_group_users_and_more'),
        ('users', '0002_balance_user_subscription_active_subscription_course_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='balance',
            name='user',
            field=models.OneToOneField(default=1000.0, on_delete=django.db.models.deletion.CASCADE, related_name='balance', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='subscription',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subscriptions', to='courses.course'),
        ),
        migrations.AlterField(
            model_name='subscription',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subscriptions', to=settings.AUTH_USER_MODEL),
        ),
    ]
