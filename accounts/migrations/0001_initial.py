# Generated by Django 2.2.9 on 2021-09-04 14:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('username', models.CharField(max_length=50, unique=True)),
                ('email', models.EmailField(max_length=100, unique=True)),
                ('phone_number', models.CharField(max_length=50)),
                ('date_joined', models.DateTimeField(auto_now_add=True)),
                ('last_login', models.DateTimeField(auto_now_add=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=False)),
                ('is_superadmin', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cpf', models.CharField(max_length=11)),
                ('endereco_completo', models.CharField(max_length=255)),
                ('cep', models.CharField(max_length=8)),
                ('cidade', models.CharField(max_length=255)),
                ('estado', models.CharField(max_length=255)),
                ('criacao', models.DateTimeField(auto_now_add=True)),
                ('atualizado', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Perfil',
                'verbose_name_plural': 'Perfis',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Plano',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plano', models.CharField(choices=[('Pessoal', 'Pessoal'), ('Empresarial', 'Empresarial')], default='Pessoal', max_length=255)),
                ('periodo', models.CharField(choices=[('Trimestral', '3 meses'), ('Semestral', '6 meses'), ('anual', '1 ano')], default='Trimestral', max_length=255)),
                ('limite_redes_iot', models.IntegerField(default=3)),
                ('limite_dispositivos_iot', models.IntegerField(default=30)),
                ('ativo', models.BooleanField(default=False)),
                ('perfil', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.UserProfile')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Plano',
                'verbose_name_plural': 'Planos',
                'ordering': ['id'],
            },
        ),
    ]
