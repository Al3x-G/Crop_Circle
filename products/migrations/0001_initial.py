# Generated by Django 3.2.25 on 2025-01-03 13:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),  # noqa: E501 (Fix flake 8 line too long)
                ('name', models.CharField(max_length=250)),
                ('friendly_name', models.CharField(blank=True, max_length=250, null=True)),  # noqa: E501 (Fix flake 8 line too long)
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),  # noqa: E501 (Fix flake 8 line too long)
                ('sku', models.CharField(blank=True, max_length=250, null=True)),  # noqa: E501 (Fix flake 8 line too long)
                ('name', models.CharField(max_length=250)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=3)),
                ('rating', models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True)),  # noqa: E501 (Fix flake 8 line too long)
                ('image_url', models.URLField(blank=True, max_length=1025, null=True)),  # noqa: E501 (Fix flake 8 line too long)
                ('image', models.ImageField(blank=True, null=True, upload_to='')),  # noqa: E501 (Fix flake 8 line too long)
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.category')),  # noqa: E501 (Fix flake 8 line too long)
            ],
        ),
    ]
