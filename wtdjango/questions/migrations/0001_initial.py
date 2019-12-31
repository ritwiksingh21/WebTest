# Generated by Django 2.1.5 on 2019-12-31 19:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MC_Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=255)),
                ('letter', models.CharField(max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=511)),
                ('multiple_choice', models.BooleanField()),
                ('lettered_parts', models.BooleanField()),
                ('mc_answers', models.ManyToManyField(to='questions.MC_Answer')),
                ('mc_correct', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='mc_answers', to='questions.MC_Answer')),
            ],
        ),
    ]
