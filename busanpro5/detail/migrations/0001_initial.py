# Generated by Django 3.2.3 on 2022-06-11 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='detail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Place', models.CharField(max_length=32, unique=True)),
                ('Theme', models.CharField(max_length=32)),
                ('Address', models.CharField(max_length=100)),
                ('Explanation', models.TextField(max_length=300)),
                ('Image_2', models.ImageField(blank=True, upload_to='images')),
            ],
        ),
    ]
