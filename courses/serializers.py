from rest_framework import serializers
from .models import Course

class CouseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Course
        fields = ['url','id','name','language','price']
