# Generated by Django 3.0.2 on 2021-03-13 04:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hospital',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to='images/hospital'),
        ),
    ]
