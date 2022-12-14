# Generated by Django 4.0.5 on 2022-11-26 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ebooks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_title', models.TextField(max_length=150)),
                ('author', models.TextField(max_length=150)),
                ('genres', models.CharField(choices=[('List of Fantasy', 'List of Fantasy'), ('Literary', 'Literary'), ('Mystery', 'Mystery'), ('Non-Fiction', 'Non-Fiction'), ('Science Fiction', 'Science Fiction'), ('Thriller', 'Thriller')], max_length=120)),
                ('review', models.CharField(choices=[('one star', 'one star'), ('two star', 'two star'), ('three star', 'three star'), ('four star', 'four star'), ('five star', 'five star')], max_length=50)),
                ('favorite', models.BooleanField(default=True)),
            ],
        ),
    ]
