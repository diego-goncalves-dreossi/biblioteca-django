# Generated by Django 4.0.3 on 2022-03-16 22:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('livro', '0004_alter_livro_data_cadastro'),
    ]

    operations = [
        migrations.AlterField(
            model_name='livro',
            name='data_cadastro',
            field=models.DateField(auto_now_add=True),
        ),
    ]
