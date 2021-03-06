# Generated by Django 2.2.3 on 2019-07-24 02:40

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('sistema', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='veiculo',
            name='cor',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='veiculo',
            name='horario',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='veiculo',
            name='marca',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='veiculo',
            name='modelo',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='veiculo',
            name='placa',
            field=models.CharField(blank=True, max_length=14),
        ),
    ]
