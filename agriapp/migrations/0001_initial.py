# Generated by Django 4.0.4 on 2023-03-08 17:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ColumnName',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('field_name', models.CharField(max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='ContactDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=255, unique=True)),
                ('mail', models.EmailField(max_length=254, unique=True)),
                ('message', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('status', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Devise',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('serial_no', models.CharField(max_length=255, unique=True)),
                ('devise_id', models.CharField(max_length=255, unique=True)),
                ('chipset_no', models.CharField(max_length=255, unique=True)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=255)),
                ('address1', models.CharField(max_length=255)),
                ('address2', models.CharField(max_length=255)),
                ('purchase_date', models.DateField()),
                ('time_of_sale', models.TimeField()),
                ('warrenty', models.DateField()),
                ('amount_paid', models.FloatField()),
                ('balance_amount', models.FloatField(default=0)),
                ('land', models.FloatField(default=0.0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='DeviseLocation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitude', models.FloatField(default=0)),
                ('longitude', models.FloatField(default=0)),
                ('status', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('devise', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='agriapp.devise', unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='DeviseApis',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('area_name', models.CharField(max_length=255)),
                ('devise_id', models.CharField(max_length=255)),
                ('serial_no', models.CharField(max_length=255)),
                ('electrical_conduction', models.FloatField(default=0.0)),
                ('nitrogen', models.FloatField(default=0.0)),
                ('phosphorous', models.FloatField(default=0.0)),
                ('potassium', models.FloatField(default=0.0)),
                ('calcium', models.FloatField(default=0.0)),
                ('magnesium', models.FloatField(default=0.0)),
                ('sulphur', models.FloatField(default=0.0)),
                ('zinc', models.FloatField(default=0.0)),
                ('manganese', models.FloatField(default=0.0)),
                ('iron', models.FloatField(default=0.0)),
                ('copper', models.FloatField(default=0.0)),
                ('boron', models.FloatField(default=0.0)),
                ('molybdenum', models.FloatField(default=0.0)),
                ('chlorine', models.FloatField(default=0.0)),
                ('nickel', models.FloatField(default=0.0)),
                ('organic_carboa', models.FloatField(default=0.0)),
                ('crop_type', models.FloatField(default=0.0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('device', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='agriapp.devise')),
            ],
        ),
        migrations.CreateModel(
            name='ColumnData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('field_value', models.FloatField(default=0.0)),
                ('api', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='agriapp.deviseapis', unique=True)),
                ('field', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='agriapp.columnname')),
            ],
        ),
        migrations.CreateModel(
            name='APICountThreshold',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('red', models.IntegerField()),
                ('orange', models.IntegerField()),
                ('blue', models.IntegerField()),
                ('green', models.IntegerField()),
                ('devise', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='agriapp.devise', unique=True)),
            ],
        ),
    ]
