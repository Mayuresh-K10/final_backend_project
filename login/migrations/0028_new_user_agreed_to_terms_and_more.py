# Generated by Django 5.1.5 on 2025-02-04 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0027_alter_universityincharge_agreed_to_terms'),
    ]

    operations = [
        migrations.AddField(
            model_name='new_user',
            name='agreed_to_terms',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='companyincharge',
            name='agreed_to_terms',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='consultant',
            name='agreed_to_terms',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='jobseeker',
            name='agreed_to_terms',
            field=models.BooleanField(default=True),
        ),
    ]
