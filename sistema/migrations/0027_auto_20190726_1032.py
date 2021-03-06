# Generated by Django 2.2.3 on 2019-07-26 10:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sistema', '0026_auto_20190726_1025'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Registro',
            new_name='DataSaida',
        ),
        migrations.RemoveField(
            model_name='dataentrada',
            name='data_entrada',
        ),
        migrations.AddField(
            model_name='dataentrada',
            name='veiculo',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='sistema.Veiculo'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='veiculo',
            name='data_entrada',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
