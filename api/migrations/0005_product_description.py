# Generated by Django 4.1.2 on 2022-10-29 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_alter_userimage_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='description',
            field=models.TextField(default=0),
            preserve_default=False,
        ),
    ]
