# Generated by Django 3.2.9 on 2021-11-26 07:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Factory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Factory name', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Founder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Founder name', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='FactoryItrod',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Estimate title', max_length=200)),
                ('contents', models.TextField(help_text='Estimate contents')),
                ('factory_id', models.ForeignKey(db_column='factory_id', on_delete=django.db.models.deletion.CASCADE, related_name='factory', to='app.factory')),
            ],
        ),
        migrations.CreateModel(
            name='FounderEst',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Estimate title', max_length=200)),
                ('contents', models.TextField(help_text='Estimate contents')),
                ('founder_id', models.ForeignKey(db_column='founder_id', on_delete=django.db.models.deletion.CASCADE, related_name='founder', to='app.founder')),
            ],
        ),
    ]
