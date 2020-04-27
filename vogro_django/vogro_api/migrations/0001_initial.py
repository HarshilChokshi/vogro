# Generated by Django 3.0.5 on 2020-04-26 22:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='VolunteerUsers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=30)),
                ('phone_number', models.CharField(max_length=15)),
                ('total_deliveries', models.IntegerField(default=0)),
                ('is_allowed_to_use_app', models.BooleanField(default=True)),
                ('strikes', models.IntegerField(default=0)),
                ('profile_image_ref', models.CharField(max_length=50, null=True)),
                ('address', models.TextField()),
                ('preferred_grocery_stores', models.TextField()),
                ('get_store_notifications', models.BooleanField(default=True)),
            ],
        ),
    ]
