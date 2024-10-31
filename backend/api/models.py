# backend/api/models.py
from django.db import models

class Node(models.Model):
    label = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    impact = models.CharField(max_length=50, choices=[
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High')
    ])
    risk_level = models.CharField(max_length=50, choices=[
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High')
    ])
    current_status = models.CharField(max_length=50, choices=[
        ('not started', 'Not Started'),
        ('in progress', 'In Progress'),
        ('completed', 'Completed'),
        ('needs review', 'Needs Review')
    ])
    date_of_completion = models.DateField(null=True, blank=True)
    owner = models.CharField(max_length=200)
    x_position = models.FloatField()
    y_position = models.FloatField()

    def __str__(self):
        return self.label

class Edge(models.Model):
    source = models.ForeignKey(Node, on_delete=models.CASCADE, related_name='source_edges')
    target = models.ForeignKey(Node, on_delete=models.CASCADE, related_name='target_edges')

    class Meta:
        unique_together = ('source', 'target')

    def __str__(self):
        return f"{self.source.label} -> {self.target.label}"

