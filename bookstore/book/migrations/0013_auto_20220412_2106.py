# Generated by Django 3.0 on 2022-04-12 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0012_auto_20220412_1347'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='Edition',
        ),
        migrations.RemoveField(
            model_name='order',
            name='category',
        ),
        migrations.AddField(
            model_name='book',
            name='Category',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
