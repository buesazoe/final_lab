# Generated by Django 5.0 on 2023-12-20 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('final_app', '0002_alter_mymodel_age'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mymodel',
            name='salary',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
    ]
