# Generated by Django 3.0.8 on 2020-09-10 21:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_product_code_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductFilters',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=100)),
            ],
        ),
    ]
