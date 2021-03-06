# Generated by Django 4.0.2 on 2022-02-21 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Invite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('branch', models.CharField(max_length=500)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other'), ('?', 'Unknown')], default='?', max_length=1)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('race', models.CharField(choices=[('ASIAN', 'Asian'), ('BLACK', 'Black'), ('LATINO', 'Latino'), ('WHITE', 'White'), ('OTHER', 'Other'), ('?', 'Unknown')], default='?', max_length=10)),
                ('notes', models.TextField(blank=True)),
            ],
        ),
    ]
