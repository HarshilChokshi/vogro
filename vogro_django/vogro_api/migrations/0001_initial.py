# Generated by Django 3.0.5 on 2020-05-03 22:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ClientUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=30)),
                ('phone_number', models.CharField(max_length=15)),
                ('total_orders', models.IntegerField(default=0)),
                ('is_allowed_to_use_app', models.BooleanField(default=True)),
                ('strikes', models.IntegerField(default=0)),
                ('profile_image_ref', models.CharField(default='', max_length=50)),
                ('address', models.TextField()),
                ('address_name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='VolunteerUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=30)),
                ('phone_number', models.CharField(max_length=15)),
                ('total_deliveries', models.IntegerField(default=0)),
                ('is_allowed_to_use_app', models.BooleanField(default=True)),
                ('strikes', models.IntegerField(default=0)),
                ('profile_image_ref', models.CharField(default='', max_length=100)),
                ('address', models.TextField()),
                ('preferred_grocery_stores', models.TextField()),
                ('get_store_notifications', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='LiveGroceryPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grocery_store_address', models.TextField()),
                ('grocery_store_address_name', models.CharField(max_length=50)),
                ('grocery_store_name', models.CharField(max_length=30)),
                ('grocery_item_list', models.TextField()),
                ('earliest_time', models.DateTimeField()),
                ('latest_time', models.DateTimeField()),
                ('receipt_image_ref', models.CharField(default='', max_length=100)),
                ('grocery_total_amount', models.DecimalField(decimal_places=2, max_digits=6)),
                ('state_of_volunteer', models.CharField(max_length=20)),
                ('client_user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vogro_api.ClientUser')),
                ('volunteer_user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vogro_api.VolunteerUser')),
            ],
        ),
        migrations.CreateModel(
            name='CompletedGroceryPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grocery_store_address', models.TextField()),
                ('grocery_store_address_name', models.CharField(max_length=50)),
                ('grocery_store_name', models.CharField(max_length=30)),
                ('grocery_item_list', models.TextField()),
                ('earliest_time', models.DateTimeField()),
                ('latest_time', models.DateTimeField()),
                ('receipt_image_ref', models.CharField(default='', max_length=100)),
                ('grocery_total_amount', models.DecimalField(decimal_places=2, max_digits=6)),
                ('client_user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vogro_api.ClientUser')),
                ('volunteer_user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vogro_api.VolunteerUser')),
            ],
        ),
        migrations.CreateModel(
            name='Complaints',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_complainer_volunteer', models.BooleanField()),
                ('complaint_details', models.TextField(max_length=500)),
                ('client_user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vogro_api.ClientUser')),
                ('completed_grocery_post_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vogro_api.CompletedGroceryPost')),
                ('volunteer_user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vogro_api.VolunteerUser')),
            ],
        ),
        migrations.CreateModel(
            name='ClientGroceryPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grocery_store_address', models.TextField()),
                ('grocery_store_address_name', models.CharField(max_length=50)),
                ('grocery_store_name', models.CharField(max_length=30)),
                ('grocery_item_list', models.TextField()),
                ('earliest_time', models.DateTimeField()),
                ('latest_time', models.DateTimeField()),
                ('time_of_post', models.DateTimeField()),
                ('client_user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vogro_api.ClientUser')),
            ],
        ),
    ]
