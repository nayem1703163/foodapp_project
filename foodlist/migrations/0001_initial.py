# Generated by Django 3.0.8 on 2020-07-19 14:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('reslist', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Foodlist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('food_image', models.ImageField(upload_to='food_images/')),
                ('food_name', models.CharField(max_length=200)),
                ('price', models.IntegerField()),
                ('res_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='reslist.Res')),
            ],
        ),
    ]
