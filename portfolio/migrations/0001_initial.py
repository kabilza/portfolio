# Generated by Django 2.2.5 on 2021-01-20 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactMe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.TextField(default='NOT SET', verbose_name='Email')),
                ('subject', models.TextField(default='NOT SET', verbose_name='Subject')),
                ('message', models.TextField(default='NOT SET', verbose_name='Message')),
            ],
        ),
        migrations.CreateModel(
            name='Info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(max_length=1, verbose_name='Gender (F or M)')),
                ('birthday', models.DateField(blank=True, null=True)),
                ('brief_info', models.TextField(default='NOT SET', verbose_name='Background Infomation')),
                ('phone_num', models.CharField(default='NOT SET', max_length=10, verbose_name='Phone Number')),
                ('twitter', models.TextField(default='NOT SET', verbose_name='Twitter')),
            ],
        ),
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.TextField(default='NOT SET', verbose_name='Project Name')),
                ('project_info', models.TextField(default='NOT SET', verbose_name='Project Info')),
                ('date_created', models.TextField(default='NOT SET', verbose_name='Date')),
            ],
        ),
    ]
