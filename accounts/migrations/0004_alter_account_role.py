# Generated by Django 4.0.6 on 2022-07-26 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_account_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='Role',
            field=models.CharField(choices=[('student', 'student'), ('staff', 'staff'), ('editor', 'editor')], default=None, max_length=200),
        ),
    ]
