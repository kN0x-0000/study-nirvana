# Generated by Django 3.0 on 2019-12-06 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('ui', models.CharField(choices=[('y', 'Yes'), ('n', 'No')], max_length=30, verbose_name='Did you like UI of our website')),
                ('sug', models.TextField(default='', verbose_name='Suggest some changes in the website')),
                ('satisfy', models.CharField(choices=[('y', 'Yes'), ('n', 'No')], max_length=30, verbose_name='Are you satisfied with course content')),
                ('sugg', models.TextField(default='', verbose_name='Suggest some changes in course content or any additions')),
                ('rating', models.CharField(choices=[('a', '1'), ('b', '2'), ('c', '3'), ('d', '4'), ('e', '5')], max_length=10, verbose_name='Rate your experience')),
            ],
        ),
    ]
