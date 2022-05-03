# Generated by Django 4.0.4 on 2022-05-03 00:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserData',
            fields=[
                ('email', models.CharField(max_length=64, primary_key=True, serialize=False)),
                ('password', models.CharField(default='None', max_length=64)),
                ('firstName', models.CharField(max_length=32)),
                ('lastName', models.CharField(max_length=32)),
                ('birthday', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Bubl',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('note', models.CharField(max_length=32)),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('length', models.IntegerField()),
                ('moved', models.IntegerField(default=0)),
                ('dead', models.BooleanField(default=False)),
                ('done', models.BooleanField(default=False)),
                ('email', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.userdata')),
            ],
        ),
    ]