# Generated by Django 4.0.5 on 2022-07-19 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apptp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='empleado',
            name='empresa_trabajo',
            field=models.CharField(default=False, max_length=250),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='producto',
            name='producto_empresa',
            field=models.CharField(default=True, max_length=250),
            preserve_default=False,
        ),
    ]
