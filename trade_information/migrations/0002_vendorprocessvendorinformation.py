# Generated by Django 3.0.3 on 2020-03-06 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trade_information', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='VendorProcessVendorInformation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vendor_id', models.CharField(max_length=20)),
                ('account_id', models.IntegerField(blank=True, null=True)),
                ('company_name', models.CharField(max_length=100)),
                ('vendor_type', models.CharField(max_length=25)),
                ('company_door_street', models.CharField(max_length=100)),
                ('company_locality', models.CharField(max_length=50)),
                ('company_state', models.CharField(max_length=50)),
                ('company_pincode', models.IntegerField()),
                ('company_email', models.CharField(max_length=254)),
                ('proprietordirectorname', models.CharField(db_column='proprietorDirectorName', max_length=100)),
                ('proprietordirectorcontact', models.BigIntegerField(db_column='proprietorDirectorContact')),
                ('local_contact_name', models.CharField(max_length=100)),
                ('local_contact_no', models.BigIntegerField(blank=True, null=True)),
                ('gstin', models.CharField(max_length=10)),
                ('uin', models.CharField(max_length=10)),
                ('pan', models.CharField(max_length=10)),
                ('account_no', models.BigIntegerField()),
                ('account_name', models.CharField(max_length=30)),
                ('account_type', models.CharField(max_length=10)),
                ('bank_name', models.CharField(max_length=15)),
                ('branch', models.CharField(max_length=50)),
                ('ifsc_code', models.CharField(max_length=11)),
                ('insurance_no', models.CharField(max_length=30)),
                ('insurance_name', models.CharField(max_length=30)),
                ('expiry_date', models.DateField()),
                ('status', models.CharField(blank=True, max_length=9, null=True)),
                ('created_date', models.DateTimeField()),
                ('updated_date', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'vendor_process_vendor_information',
                'managed': False,
            },
        ),
    ]
