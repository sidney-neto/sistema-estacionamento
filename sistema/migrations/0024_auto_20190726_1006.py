# Generated by Django 2.2.3 on 2019-07-26 10:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sistema', '0023_auto_20190726_1002'),
    ]

    operations = [
        migrations.AlterField(
            model_name='veiculo',
            name='data_entrada',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='sistema.Data'),
        ),
    ]
