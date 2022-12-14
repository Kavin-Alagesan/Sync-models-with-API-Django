# Generated by Django 4.0.6 on 2022-07-13 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='details',
            name='contact',
            field=models.PositiveIntegerField(default='123456789'),
        ),
        migrations.AddField(
            model_name='details',
            name='dob',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='details',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=None),
        ),
        migrations.AlterField(
            model_name='details',
            name='qualification',
            field=models.CharField(choices=[('No formal education', 'No formal education'), ('Primary education', 'Primary education'), ('Secondary education', 'Secondary education'), ('GED', 'GED'), ('Vocational qualification', 'Vocational qualification'), ("Bachelor's degree", "Bachelor's degree"), ("Master's degree", "Master's degree"), ('Doctorate or higher', 'Doctorate or higher')], default='No formal education', max_length=30),
        ),
    ]
