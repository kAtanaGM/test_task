# Generated by Django 4.2.10 on 2024-08-17 16:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('courses', '0002_course_price_group_course_group_name_group_users_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='course',
            field=models.ForeignKey(help_text='Связана с моделью Course', on_delete=django.db.models.deletion.CASCADE, related_name='course_groups', to='courses.course'),
        ),
        migrations.AlterField(
            model_name='group',
            name='users',
            field=models.ManyToManyField(help_text='Участники группы', related_name='users_groups', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='course',
            field=models.ForeignKey(help_text='Связана с моделью Course', on_delete=django.db.models.deletion.CASCADE, related_name='lessons', to='courses.course'),
        ),
    ]
