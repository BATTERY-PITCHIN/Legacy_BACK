# Generated by Django 3.2.9 on 2021-11-28 10:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20211128_0228'),
    ]

    operations = [
        migrations.AddField(
            model_name='factory_introd',
            name='keyword1',
            field=models.CharField(blank=True, help_text='Keyword1', max_length=10),
        ),
        migrations.AddField(
            model_name='factory_introd',
            name='keyword2',
            field=models.CharField(blank=True, help_text='Keyword2', max_length=10),
        ),
        migrations.AddField(
            model_name='factory_introd',
            name='keyword3',
            field=models.CharField(blank=True, help_text='Keyword3', max_length=10),
        ),
        migrations.AddField(
            model_name='founder_est',
            name='keyword1',
            field=models.CharField(blank=True, help_text='Keyword1', max_length=10),
        ),
        migrations.AddField(
            model_name='founder_est',
            name='keyword2',
            field=models.CharField(blank=True, help_text='Keyword2', max_length=10),
        ),
        migrations.AddField(
            model_name='founder_est',
            name='keyword3',
            field=models.CharField(blank=True, help_text='Keyword3', max_length=10),
        ),
        migrations.AlterField(
            model_name='factory',
            name='name',
            field=models.CharField(help_text='Factory Name', max_length=20),
        ),
        migrations.AlterField(
            model_name='factory_introd',
            name='contents',
            field=models.TextField(help_text='Introduction Contents'),
        ),
        migrations.AlterField(
            model_name='factory_introd',
            name='factory_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='factory_introd', to='app.factory'),
        ),
        migrations.AlterField(
            model_name='factory_introd',
            name='title',
            field=models.CharField(help_text='Introduction Title', max_length=200),
        ),
        migrations.AlterField(
            model_name='founder',
            name='name',
            field=models.CharField(help_text='Founder Name', max_length=20),
        ),
        migrations.AlterField(
            model_name='founder_est',
            name='contents',
            field=models.TextField(help_text='Estimate Contents'),
        ),
        migrations.AlterField(
            model_name='founder_est',
            name='founder_id',
            field=models.ForeignKey(db_column='founder_id', on_delete=django.db.models.deletion.CASCADE, related_name='founder_est', to='app.founder'),
        ),
        migrations.AlterField(
            model_name='founder_est',
            name='title',
            field=models.CharField(help_text='Estimate Title', max_length=200),
        ),
    ]