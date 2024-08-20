# Generated by Django 4.2.10 on 2024-08-17 14:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Стоимость'),
        ),
        migrations.AddField(
            model_name='group',
            name='course',
            field=models.ForeignKey(default=None, help_text='Связана с моделью Course', on_delete=django.db.models.deletion.CASCADE, to='courses.course'),
        ),
        migrations.AddField(
            model_name='group',
            name='name',
            field=models.CharField(max_length=255, null=True, unique=True, verbose_name='Название'),
        ),
        migrations.AddField(
            model_name='group',
            name='users',
            field=models.ManyToManyField(help_text='Участники группы', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='lesson',
            name='course',
            field=models.ForeignKey(default=None, help_text='Связана с моделью Course', on_delete=django.db.models.deletion.CASCADE, to='courses.course'),
        ),
    ]