# Generated by Django 5.1.1 on 2024-09-16 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_remove_student_file'),
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_nmaer', models.CharField(max_length=100)),
                ('speed', models.IntegerField()),
            ],
        ),
    ]
