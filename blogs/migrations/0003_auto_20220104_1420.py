# Generated by Django 3.2.6 on 2022-01-04 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0002_auto_20220104_1300'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='text',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Entry',
        ),
    ]