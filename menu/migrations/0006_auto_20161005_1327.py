# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import menu.fields


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('menu', '0005_file_image_text_video'),
    ]

    operations = [
        migrations.CreateModel(
            name='ItemContent',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('itemid', models.PositiveIntegerField()),
                ('orderview', menu.fields.OrderField(blank=True)),
                ('itemtype', models.ForeignKey(to='contenttypes.ContentType')),
            ],
            options={
                'ordering': ['orderview'],
            },
        ),
        migrations.AlterModelOptions(
            name='menudetail',
            options={'ordering': ['orderview']},
        ),
        migrations.AlterField(
            model_name='menudetail',
            name='orderview',
            field=menu.fields.OrderField(blank=True),
        ),
        migrations.AddField(
            model_name='itemcontent',
            name='menudetail',
            field=models.ForeignKey(to='menu.MenuDetail', related_name='rel_itemcontents_menudetails'),
        ),
    ]
