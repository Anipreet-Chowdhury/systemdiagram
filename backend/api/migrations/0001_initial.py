# Generated by Django 5.1 on 2024-10-31 04:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Node',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True)),
                ('impact', models.CharField(choices=[('low', 'Low'), ('medium', 'Medium'), ('high', 'High')], max_length=50)),
                ('risk_level', models.CharField(choices=[('low', 'Low'), ('medium', 'Medium'), ('high', 'High')], max_length=50)),
                ('current_status', models.CharField(choices=[('not started', 'Not Started'), ('in progress', 'In Progress'), ('completed', 'Completed'), ('needs review', 'Needs Review')], max_length=50)),
                ('date_of_completion', models.DateField(blank=True, null=True)),
                ('owner', models.CharField(max_length=200)),
                ('x_position', models.FloatField()),
                ('y_position', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Edge',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='source_edges', to='api.node')),
                ('target', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='target_edges', to='api.node')),
            ],
            options={
                'unique_together': {('source', 'target')},
            },
        ),
    ]