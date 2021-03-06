# Generated by Django 4.0.4 on 2022-06-09 08:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('touristspots', '0002_favoritespot'),
    ]

    operations = [
        migrations.AlterField(
            model_name='favoritespot',
            name='mytouristspot',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='favoritespots_spot', to='touristspots.touristspot'),
        ),
        migrations.AlterField(
            model_name='favoritespot',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='favoritespots_user', to=settings.AUTH_USER_MODEL),
        ),
    ]
