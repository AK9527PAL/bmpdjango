# Generated by Django 5.0.2 on 2024-02-12 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_remove_contact_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admission_form',
            name='dob',
            field=models.DateField(),
        ),
    ]