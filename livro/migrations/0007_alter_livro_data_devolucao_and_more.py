# Generated by Django 4.0.3 on 2022-03-16 23:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('livro', '0006_alter_livro_data_cadastro'),
    ]

    operations = [
        migrations.AlterField(
            model_name='livro',
            name='data_devolucao',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='livro',
            name='data_emprestimo',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='livro',
            name='nome_emprestado',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='livro',
            name='tempo_duracao',
            field=models.DateField(blank=True, null=True),
        ),
    ]
