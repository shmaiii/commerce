# Generated by Django 4.0.6 on 2022-07-27 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0007_auctionlisting_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='content',
            field=models.TextField(),
        ),
    ]