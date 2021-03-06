# Generated by Django 2.1.7 on 2019-03-20 13:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=15, unique=True, verbose_name='unique number')),
                ('name', models.CharField(max_length=255, verbose_name='name')),
                ('balance', models.DecimalField(decimal_places=2, max_digits=15, verbose_name='balance')),
                ('blocked_amount', models.DecimalField(decimal_places=2, max_digits=15, verbose_name='blocked amount')),
            ],
            options={
                'verbose_name_plural': 'accounts',
                'verbose_name': 'account',
            },
        ),
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=3, unique=True, verbose_name='ISO code')),
            ],
            options={
                'verbose_name_plural': 'currencies',
                'verbose_name': 'currency',
            },
        ),
        migrations.AddField(
            model_name='account',
            name='currency',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='django_capitalist.Currency', verbose_name='currency'),
        ),
    ]
