# Generated by Django 3.2.25 on 2025-01-11 19:37

from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0002_auto_20250105_2120'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),  # noqa: E501 (Fix flake 8 line too long)
                ('order_number', models.CharField(editable=False, max_length=32)),  # noqa: E501 (Fix flake 8 line too long)
                ('full_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(max_length=20)),
                ('country', django_countries.fields.CountryField(max_length=2)),  # noqa: E501 (Fix flake 8 line too long)
                ('postcode', models.CharField(blank=True, max_length=20, null=True)),  # noqa: E501 (Fix flake 8 line too long)
                ('town_or_city', models.CharField(max_length=40)),
                ('street_address1', models.CharField(max_length=80)),
                ('street_address2', models.CharField(blank=True, max_length=80, null=True)),  # noqa: E501 (Fix flake 8 line too long)
                ('county', models.CharField(blank=True, max_length=80, null=True)),  # noqa: E501 (Fix flake 8 line too long)
                ('date', models.DateTimeField(auto_now_add=True)),
                ('delivery_cost', models.DecimalField(decimal_places=2, default=0, max_digits=6)),  # noqa: E501 (Fix flake 8 line too long)
                ('order_total', models.DecimalField(decimal_places=2, default=0, max_digits=10)),  # noqa: E501 (Fix flake 8 line too long)
                ('grand_total', models.DecimalField(decimal_places=2, default=0, max_digits=10)),  # noqa: E501 (Fix flake 8 line too long)
            ],
        ),
        migrations.CreateModel(
            name='OrderLineItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),  # noqa: E501 (Fix flake 8 line too long)
                ('quantity', models.IntegerField(default=0)),
                ('lineitem_total', models.DecimalField(decimal_places=2, editable=False, max_digits=6)),  # noqa: E501 (Fix flake 8 line too long)
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lineitems', to='checkout.order')),  # noqa: E501 (Fix flake 8 line too long)
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product')),  # noqa: E501 (Fix flake 8 line too long)
            ],
        ),
    ]
