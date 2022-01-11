# Generated by Django 3.2.7 on 2021-11-25 12:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('devicesapi', '0003_auto_20211012_1326'),
        ('accounts', '0004_account_network_limit_creation'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rede',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criacao', models.DateTimeField(auto_now_add=True)),
                ('atualizacao', models.DateTimeField(auto_now_add=True)),
                ('ativo', models.BooleanField(default=True)),
                ('limite_dispositivos_rede', models.IntegerField(default=10)),
                ('qtd_dispositivos_rede', models.IntegerField(default=0)),
                ('identificador', models.CharField(max_length=255)),
                ('dispositivos', models.ManyToManyField(blank=True, to='devicesapi.Dispositivo')),
                ('plano', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.plano')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]