# Generated by Django 3.0.2 on 2021-03-13 11:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('patient', '0004_auto_20210313_1643'),
        ('insurancecompany', '0001_initial'),
        ('hospital', '0003_auto_20210313_1008'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClaimStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('claim_status_code', models.CharField(max_length=8)),
                ('status_description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Claim',
            fields=[
                ('claim_number', models.IntegerField(primary_key=True, serialize=False)),
                ('details', models.TextField()),
                ('update_date', models.DateField()),
                ('claim_status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='claims.ClaimStatus')),
                ('hospital_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hospital.Hospital')),
                ('insurance_company_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='insurancecompany.Company')),
                ('patient_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patient.Patient')),
            ],
        ),
    ]
