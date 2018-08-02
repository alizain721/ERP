# Generated by Django 2.0.7 on 2018-08-02 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=30)),
                ('profile_pic', models.CharField(blank=True, max_length=1000)),
                ('contact_info', models.CharField(blank=True, max_length=30)),
            ],
        ),
    ]
