# Generated by Django 5.0.1 on 2024-01-20 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BbsModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_created=True)),
                ('title', models.CharField(max_length=100)),
                ('content', models.CharField(max_length=1000)),
            ],
        ),
    ]
