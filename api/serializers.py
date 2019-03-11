# snippets/serializers
from rest_framework import serializers
from cms.models import Course

class CourseSerializer(serializers.ModelSerializer):
    chapter = serializers.StringRelatedField(many=True)

    class Meta:
        model = Course
        fields = ('id', 'author', 'name', 'category',
                  'chapter', 'cover', 'description', 'created_date')