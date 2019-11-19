# Generated by Django 2.2.7 on 2019-11-19 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_auto_20191119_1012'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='question',
            options={'verbose_name': 'Question'},
        ),
        migrations.AlterField(
            model_name='question',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='created'),
        ),
        migrations.AlterField(
            model_name='question',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='is_active'),
        ),
        migrations.AlterField(
            model_name='question',
            name='level',
            field=models.CharField(blank=True, choices=[('easy', 'easy'), ('normal', 'normal'), ('hard', 'hard')], max_length=50, null=True, verbose_name='level'),
        ),
        migrations.AlterField(
            model_name='question',
            name='modified',
            field=models.DateTimeField(auto_now=True, verbose_name='modified'),
        ),
        migrations.AlterField(
            model_name='question',
            name='question_image',
            field=models.ImageField(blank=True, null=True, upload_to='questionimages/%Y/%m/%d', verbose_name='question_image'),
        ),
        migrations.AlterField(
            model_name='question',
            name='question_text',
            field=models.CharField(max_length=300, verbose_name='question text'),
        ),
    ]
