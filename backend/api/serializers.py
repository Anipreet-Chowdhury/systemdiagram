# backend/api/serializers.py
from rest_framework import serializers
from .models import Node, Edge

class NodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Node
        fields = ['id', 'label', 'description', 'impact', 'risk_level', 
                 'current_status', 'date_of_completion', 'owner',  
                 'x_position', 'y_position']

class EdgeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Edge
        fields = ['id', 'source', 'target']