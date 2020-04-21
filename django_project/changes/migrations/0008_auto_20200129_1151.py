# Generated by Django 2.2 on 2020-01-29 09:51

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('changes', '0007_sponsor_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sponsorshipperiod',
            name='currency',
            field=models.CharField(blank=True, default='EUR', help_text='The currency that is used for sustaining membership payment.', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='sponsorshipperiod',
            name='end_date',
            field=models.DateField(blank=True, help_text='End date of sustaining membership period', null=True, verbose_name='End date'),
        ),
        migrations.AlterField(
            model_name='sponsorshipperiod',
            name='sponsor',
            field=models.ForeignKey(help_text='Input the sustaining member name', on_delete=django.db.models.deletion.CASCADE, to='changes.Sponsor', verbose_name='Sustaining member'),
        ),
        migrations.AlterField(
            model_name='sponsorshipperiod',
            name='sponsorship_level',
            field=models.ForeignKey(help_text='This level take from Sustaining Membership Level, you can add it by using Sustaining Membership Level menu', on_delete=django.db.models.deletion.CASCADE, to='changes.SponsorshipLevel', verbose_name='Sustaining member level'),
        ),
        migrations.AlterField(
            model_name='sponsorshipperiod',
            name='start_date',
            field=models.DateField(default=django.utils.timezone.now, help_text='Start date of sustaining membership period', verbose_name='Start date'),
        ),
    ]
