# Generated by Django 3.0.8 on 2021-01-16 16:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pokemon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('height', models.CharField(max_length=50)),
                ('weight', models.CharField(max_length=50)),
                ('attack', models.IntegerField()),
                ('hp', models.IntegerField()),
                ('defense', models.IntegerField()),
                ('special_attack', models.IntegerField()),
                ('special_defense', models.IntegerField()),
                ('speed', models.IntegerField()),
                ('evolves_from', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='pokemon.Pokemon')),
            ],
        ),
    ]