# Generated by Django 3.1.1 on 2020-09-28 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('fname', models.CharField(max_length=250)),
                ('lname', models.CharField(max_length=250)),
                ('password', models.CharField(max_length=250)),
                ('password2', models.CharField(max_length=250)),
                ('mobile', models.CharField(max_length=15)),
                ('telephone', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('confirm_email', models.EmailField(max_length=254, unique=True)),
                ('company', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('address1', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('postalZip', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
