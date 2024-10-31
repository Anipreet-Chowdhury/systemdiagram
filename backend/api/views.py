# backend/api/views.py
from rest_framework import viewsets
from rest_framework.response import Response
from .models import Node, Edge
from .serializers import NodeSerializer, EdgeSerializer

class NodeViewSet(viewsets.ModelViewSet):
    queryset = Node.objects.all()
    serializer_class = NodeSerializer

class EdgeViewSet(viewsets.ModelViewSet):
    queryset = Edge.objects.all()
    serializer_class = EdgeSerializer
