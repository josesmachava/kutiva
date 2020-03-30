# snippets/serializers
from rest_framework import serializers
from cms.models import Course
# from conference.models import Talk


class CourseSerializer(serializers.ModelSerializer):
    chapter = serializers.StringRelatedField(many=True)

    class Meta:
        model = Course
        fields = '__all__'


# class TalkSerializer(serializers.ModelSerializer):
#     # author = serializers.StringRelatedField(many=True)

#     class Meta:
#         model = Talk
#         fields = '__all__'
