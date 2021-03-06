# Generated by Django 3.0 on 2019-12-06 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField(default='insert')),
                ('logo', models.ImageField(blank=True, default='default.jpg', upload_to='course')),
                ('video', models.FileField(blank=True, null=True, upload_to='course')),
                ('pdf', models.FileField(blank=True, null=True, upload_to='course')),
                ('url', models.CharField(default='#', max_length=255)),
                ('instructor', models.CharField(max_length=100)),
            ],
        ),
    ]
