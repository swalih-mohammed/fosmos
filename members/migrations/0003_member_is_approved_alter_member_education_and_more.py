# Generated by Django 4.1.2 on 2023-01-02 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0002_member_address_member_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='is_approved',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='member',
            name='education',
            field=models.CharField(blank=True, choices=[('SSLC', 'SSLC'), ('+2', '+2'), ('GRADUATION', 'GRADUATION'), ('PG', 'PG'), ('DOCTRATE', 'DOCTRATE')], max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='profession',
            field=models.CharField(blank=True, choices=[('SSLC', 'SSLC'), ('+2', '+2'), ('GRADUATION', 'GRADUATION'), ('PG', 'PG'), ('DOCTRATE', 'DOCTRATE')], max_length=250, null=True),
        ),
    ]
