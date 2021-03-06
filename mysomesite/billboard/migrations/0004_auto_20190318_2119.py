# Generated by Django 2.1.7 on 2019-03-18 18:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('billboard', '0003_auto_20190318_1721'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rubric',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=30, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Рубрика',
                'verbose_name_plural': 'Рубрики',
                'ordering': ['name'],
            },
        ),
        migrations.AlterModelOptions(
            name='advertisement',
            options={'ordering': ['-published'], 'verbose_name': 'Объявление', 'verbose_name_plural': 'Объявления'},
        ),
        migrations.AlterField(
            model_name='advertisement',
            name='content',
            field=models.TextField(blank=True, null=True, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='advertisement',
            name='price',
            field=models.FloatField(blank=True, null=True, verbose_name='Цена'),
        ),
        migrations.AlterField(
            model_name='advertisement',
            name='published',
            field=models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Опубликовано'),
        ),
        migrations.AlterField(
            model_name='advertisement',
            name='title',
            field=models.CharField(max_length=50, verbose_name='Товар'),
        ),
        migrations.AddField(
            model_name='advertisement',
            name='rubric',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='billboard.Rubric', verbose_name='Рубрика'),
        ),
    ]
