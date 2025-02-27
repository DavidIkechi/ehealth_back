# Generated by Django 4.2.17 on 2024-12-19 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ehealth_app', '0004_areaofexpertise_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='KeyInitiatives',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('url', models.URLField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AddField(
            model_name='peopleinformation',
            name='key_initiatives',
            field=models.ManyToManyField(blank=True, to='ehealth_app.keyinitiatives'),
        ),
    ]
