# Generated by Django 4.2.4 on 2023-08-17 14:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_rename_address_admission_form_address_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='admission_form',
            old_name='Address',
            new_name='add',
        ),
        migrations.RenameField(
            model_name='admission_form',
            old_name='Branch',
            new_name='branch',
        ),
        migrations.RenameField(
            model_name='admission_form',
            old_name='DOB',
            new_name='dob',
        ),
        migrations.RenameField(
            model_name='admission_form',
            old_name='Email',
            new_name='email',
        ),
        migrations.RenameField(
            model_name='admission_form',
            old_name='Fathername',
            new_name='fname',
        ),
        migrations.RenameField(
            model_name='admission_form',
            old_name='Gender',
            new_name='gender',
        ),
        migrations.RenameField(
            model_name='admission_form',
            old_name='Mothername',
            new_name='mothername',
        ),
        migrations.RenameField(
            model_name='admission_form',
            old_name='Name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='admission_form',
            old_name='Phone',
            new_name='phone',
        ),
    ]