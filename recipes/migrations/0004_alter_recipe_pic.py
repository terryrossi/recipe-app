# Generated by Django 4.2.9 on 2024-03-05 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0003_alter_recipe_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='pic',
            field=models.ImageField(default='no_picture.png', upload_to='recipes'),
        ),
    ]
