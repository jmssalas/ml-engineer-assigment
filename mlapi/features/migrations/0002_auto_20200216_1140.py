# Generated by Django 2.2.10 on 2020-02-16 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('features', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feature',
            name='aff_type',
            field=models.CharField(blank=True, max_length=1000),
        ),
        migrations.AlterField(
            model_name='feature',
            name='country_segment',
            field=models.CharField(blank=True, max_length=1000),
        ),
        migrations.AlterField(
            model_name='feature',
            name='credit_card_level',
            field=models.CharField(blank=True, max_length=1000),
        ),
        migrations.AlterField(
            model_name='feature',
            name='hidden',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='feature',
            name='is_cancelled',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='feature',
            name='is_lp',
            field=models.IntegerField(null=True),
        ),
    ]