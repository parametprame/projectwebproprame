# Generated by Django 3.0.3 on 2020-03-10 21:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=255)),
                ('description', models.CharField(default='', max_length=255)),
                ('developer', models.CharField(default='', max_length=255)),
                ('rating', models.CharField(default='', max_length=255)),
                ('release_date', models.DateTimeField()),
                ('price', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Game_type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_name', models.CharField(default='', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Regis',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(default='', max_length=250)),
                ('lname', models.CharField(default='', max_length=250)),
                ('username', models.CharField(default='', max_length=50)),
                ('password', models.CharField(default='', max_length=50)),
                ('email', models.CharField(default='', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='User_Game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('purchased_date', models.DateTimeField()),
                ('serial', models.CharField(default='', max_length=255)),
                ('game_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nonregister.Game')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='nonregister.Regis')),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img_url', models.ImageField(upload_to='static/static_dirs/images/')),
                ('game_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nonregister.Game')),
            ],
        ),
        migrations.AddField(
            model_name='game',
            name='game_type_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='nonregister.Game_type'),
        ),
    ]
