# Generated by Django 2.2.9 on 2021-09-03 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_auto_20210903_1048'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plano',
            name='periodo',
            field=models.IntegerField(choices=[('Trimestral', '3_meses'), ('Semestral', '6_meses'), ('anual', '1_ano')], default='Trimestral'),
        ),
        migrations.AlterField(
            model_name='plano',
            name='plano',
            field=models.CharField(choices=[('Pessoal', 'Pessoal'), ('Empresarial', 'Empresarial')], default='Gratuito', max_length=255),
        ),
    ]