# Generated by Django 5.0.6 on 2024-07-03 21:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('product_id', models.AutoField(primary_key=True, serialize=False)),
                ('product_name', models.CharField(max_length=50)),
                ('category', models.CharField(default='', max_length=50)),
                ('sub_category', models.CharField(default='', max_length=50)),
                ('price', models.IntegerField(default=0)),
                ('desc', models.CharField(default='No description available', max_length=300)),
                ('pub_date', models.DateField()),
                ('image', models.ImageField(default='', upload_to='foodapp/images')),
            ],
        ),
    ]
