# Generated by Django 4.2 on 2024-07-27 03:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0002_comment_unique_email_handout_comment'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='comment',
            name='unique_email_handout_comment',
        ),
    ]
