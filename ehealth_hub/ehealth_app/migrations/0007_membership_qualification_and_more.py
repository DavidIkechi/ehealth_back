# Generated by Django 4.2.17 on 2024-12-19 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ehealth_app', '0006_keyresearcharea_peopleinformation_key_research_areas'),
    ]

    operations = [
        migrations.CreateModel(
            name='Membership',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=400)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Qualification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=400)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AddField(
            model_name='peopleinformation',
            name='memberships',
            field=models.ManyToManyField(blank=True, to='ehealth_app.membership'),
        ),
        migrations.AddField(
            model_name='peopleinformation',
            name='qualifications',
            field=models.ManyToManyField(blank=True, to='ehealth_app.qualification'),
        ),
    ]
