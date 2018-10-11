# Generated by Django 2.1.2 on 2018-10-11 22:54

from django.db import migrations, models
import django.db.models.deletion
import main.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('openhumans', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OverlandUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('endpoint_token', models.CharField(default=main.models.generate_endpoint_token, max_length=10, unique=True)),
                ('oh_member', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='openhumans.OpenHumansMember')),
            ],
        ),
    ]