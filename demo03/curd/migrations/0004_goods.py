# Generated by Django 2.2 on 2019-04-19 09:05

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('curd', '0003_bookinfo_heroinfo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Goods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
            managers=[
                ('mange', django.db.models.manager.Manager()),
            ],
        ),
    ]