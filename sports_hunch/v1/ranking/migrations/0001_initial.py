# Generated by Django 4.0 on 2022-06-10 00:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('championship', '0001_initial'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BetRanking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_points', models.IntegerField()),
                ('championship_table', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='championship.championshiptable')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.user')),
            ],
            options={
                'db_table': 'betranking',
            },
        ),
    ]
