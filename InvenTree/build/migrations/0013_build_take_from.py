# Generated by Django 2.2 on 2019-05-10 08:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0015_stockitem_delete_on_deplete'),
        ('build', '0012_auto_20190508_2332'),
    ]

    operations = [
        migrations.AddField(
            model_name='build',
            name='take_from',
            field=models.ForeignKey(blank=True, help_text='Select location to take stock from for this build (leave blank to take from any stock location', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='sourcing_builds', to='stock.StockLocation'),
        ),
    ]