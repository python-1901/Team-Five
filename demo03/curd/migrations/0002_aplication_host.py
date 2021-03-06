# Generated by Django 2.2 on 2019-04-19 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('curd', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Host',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hostname', models.CharField(max_length=32)),
                ('ip', models.GenericIPAddressField(protocol='ipv4')),
                ('port', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Aplication',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('h', models.ManyToManyField(to='curd.Host')),
            ],
        ),
    ]
