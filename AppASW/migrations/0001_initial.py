# Generated by Django 5.0.2 on 2024-04-12 07:15

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Magazine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('title', models.CharField(max_length=50)),
                ('description', models.CharField(blank=True, max_length=10000, null=True)),
                ('rules', models.CharField(blank=True, max_length=10000, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.TextField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Thread',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField(null=True)),
                ('title', models.CharField(max_length=255)),
                ('body', models.CharField(blank=True, max_length=35000, null=True)),
                ('magazine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='threads', to='AppASW.magazine')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='threads', to='AppASW.usuario')),
                ('downvotes', models.ManyToManyField(blank=True, related_name='downvoted_comments', to='AppASW.usuario')),
                ('upvotes', models.ManyToManyField(blank=True, related_name='upvoted_comments', to='AppASW.usuario')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=50000)),
                ('created', models.DateTimeField()),
                ('thread', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='AppASW.thread')),
                ('downvotes', models.ManyToManyField(blank=True, related_name='downvoted_users', to='AppASW.usuario')),
                ('upvotes', models.ManyToManyField(blank=True, related_name='upvoted_users', to='AppASW.usuario')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='AppASW.usuario')),
            ],
        ),
    ]