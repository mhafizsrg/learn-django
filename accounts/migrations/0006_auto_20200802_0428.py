# Generated by Django 3.0.8 on 2020-08-02 04:28

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('accounts', '0005_auto_20200801_1015'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='note',
            field=models.CharField(max_length=1020, null=True),
        ),
        migrations.AlterField(
            model_name='products',
            name='description',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
