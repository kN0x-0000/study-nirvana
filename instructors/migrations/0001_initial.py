# Generated by Django 3.0 on 2019-12-06 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Instructor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('image', models.ImageField(default='default.jpg', upload_to='instruct')),
                ('url', models.CharField(default='#', max_length=255)),
            ],
        ),
    ]
