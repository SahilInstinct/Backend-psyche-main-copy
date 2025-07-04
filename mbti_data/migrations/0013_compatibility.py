# Generated by Django 5.2 on 2025-07-01 18:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mbti_data', '0012_delete_conclusionsection'),
    ]

    operations = [
        migrations.CreateModel(
            name='Compatibility',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('romance_matches', models.CharField(help_text='Comma-separated MBTI types', max_length=50)),
                ('friendship_matches', models.CharField(max_length=50)),
                ('career_matches', models.CharField(max_length=50)),
                ('personality', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='compatibility', to='mbti_data.personalitytype')),
            ],
        ),
    ]
