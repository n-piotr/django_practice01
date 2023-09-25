# Generated by Django 4.2.5 on 2023-09-24 23:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('year', models.IntegerField()),
                ('power', models.IntegerField()),
                ('type', models.CharField(max_length=50)),
                ('kms', models.IntegerField()),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('image', models.ImageField(upload_to='car_images/')),
            ],
        ),
    ]
