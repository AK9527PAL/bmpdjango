# Generated by Django 4.2.4 on 2023-08-16 15:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_admission_form'),
    ]

    operations = [
        migrations.RenameField(
            model_name='admission_form',
            old_name='address',
            new_name='Address',
        ),
        migrations.RenameField(
            model_name='admission_form',
            old_name='branch',
            new_name='Branch',
        ),
        migrations.RenameField(
            model_name='admission_form',
            old_name='dob',
            new_name='DOB',
        ),
        migrations.RenameField(
            model_name='admission_form',
            old_name='email',
            new_name='Email',
        ),
        migrations.RenameField(
            model_name='admission_form',
            old_name='fname',
            new_name='Fathername',
        ),
        migrations.RenameField(
            model_name='admission_form',
            old_name='gender',
            new_name='Gender',
        ),
        migrations.RenameField(
            model_name='admission_form',
            old_name='mname',
            new_name='Mothername',
        ),
        migrations.RenameField(
            model_name='admission_form',
            old_name='name',
            new_name='Name',
        ),
        migrations.RenameField(
            model_name='admission_form',
            old_name='phone',
            new_name='Phone',
        ),
    ]
