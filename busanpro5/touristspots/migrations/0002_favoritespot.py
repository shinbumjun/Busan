# Generated by Django 4.0.4 on 2022-06-09 07:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('touristspots', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FavoriteSpot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mytouristspot', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='favoritespots', to='touristspots.touristspot')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='favoritespots', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]