# Generated by Django 4.0.3 on 2022-03-19 02:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('livro', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='livro',
            name='sinopse',
            field=models.TextField(default='Sinopse'),
        ),
    ]
