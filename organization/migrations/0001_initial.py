# Generated by Django 4.2.3 on 2023-07-24 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('logo', models.ImageField(blank=True, null=True, upload_to='logos/')),
                ('business_type', models.CharField(choices=[('sole', 'Şahıs'), ('large', 'Büyük işletme'), ('sme', 'KOBİ'), ('ngo', 'STK')], max_length=10)),
                ('country', models.CharField(max_length=100)),
                ('website', models.URLField(blank=True, null=True)),
                ('employee_count', models.PositiveIntegerField()),
            ],
        ),
    ]
