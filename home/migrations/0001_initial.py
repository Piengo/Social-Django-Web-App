# Generated by Django 2.2 on 2020-05-18 09:34

from django.conf import settings
import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_birth', models.DateField(verbose_name='Date of birth')),
                ('Gender', models.CharField(choices=[('m', 'male'), ('f', 'female'), ('o', 'other')], max_length=3, verbose_name='Gender')),
                ('Preference', models.CharField(choices=[('m', 'male'), ('f', 'female'), ('bi', 'both')], max_length=3, verbose_name='Attracted to?')),
                ('The_type_of_relationship_you_are_looking_for', models.CharField(choices=[('sr', 'A serious relationship.'), ('fr', 'Friend'), ('st', 'Someone to talk to.'), ('hk', 'A hook-up.')], max_length=3, verbose_name='You are looking for a...')),
                ('profile_picture', models.ImageField(upload_to='images/')),
                ('Bio', models.TextField(verbose_name='Bio (Express what makes you tick, this will be visible for others to view.)')),
                ('location', django.contrib.gis.db.models.fields.PointField(blank=True, srid=4326)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]