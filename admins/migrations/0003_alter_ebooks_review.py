# Generated by Django 4.0.5 on 2022-11-26 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admins', '0002_alter_ebooks_review'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ebooks',
            name='review',
            field=models.CharField(choices=[('*', 'one star'), ('**', 'two star'), ('***', 'three star'), ('****', 'four star'), ('*****', 'five star')], max_length=50),
        ),
    ]
