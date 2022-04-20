# Generated by Django 4.0.3 on 2022-04-15 08:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('online_store', '0006_category_delete_sparepart'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='model_of_auto',
        ),
        migrations.RemoveField(
            model_name='category',
            name='name_of_part',
        ),
        migrations.CreateModel(
            name='SparePartSubCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_of_part', models.CharField(max_length=20)),
                ('model_of_auto', models.CharField(max_length=50)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='online_store.category')),
            ],
        ),
        migrations.CreateModel(
            name='SparePart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('part_number', models.CharField(max_length=20)),
                ('price', models.IntegerField()),
                ('discount', models.IntegerField()),
                ('active_status', models.BooleanField(default=True)),
                ('sold_status', models.BooleanField(default=False)),
                ('name_of_part', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='online_store.sparepartsubcategory')),
            ],
        ),
        migrations.CreateModel(
            name='PartImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default=None, upload_to='profile_pics')),
                ('id_of_part', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='online_store.sparepart')),
            ],
        ),
    ]
