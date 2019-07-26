# Generated by Django 2.2.3 on 2019-07-26 09:55

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('sistema', '0019_auto_20190726_0950'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='horario',
            name='horario_saida',
        ),
        migrations.AddField(
            model_name='registro',
            name='horario_saida',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]