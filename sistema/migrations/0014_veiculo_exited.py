# Generated by Django 2.2.3 on 2019-07-25 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sistema', '0013_auto_20190724_2213'),
    ]

    operations = [
        migrations.AddField(
            model_name='veiculo',
            name='exited',
            field=models.BooleanField(default=False),
        ),
    ]
