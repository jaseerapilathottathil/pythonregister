# Generated by Django 4.2.7 on 2023-12-09 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newprojectapp1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Fullname', models.CharField(max_length=250)),
                ('Image', models.ImageField(upload_to='pics')),
                ('qual', models.CharField(max_length=250)),
                ('desc', models.TextField()),
            ],
        ),
    ]
