# Generated by Django 5.0.1 on 2024-06-13 19:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0003_alter_reportmodel_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='productmodel',
            name='Category',
            field=models.ForeignKey(default=0.0, on_delete=django.db.models.deletion.CASCADE, to='Product.category'),
            preserve_default=False,
        ),
    ]
