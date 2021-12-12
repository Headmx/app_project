from rest_framework import serializers
from animals.models import Announcement, Comment

class AnnouncementDetailSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault()) #user определяется автоматически в create
    class Meta:
        model = Announcement
        fields = '__all__'

class CommentDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class CommentListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['author','text']

class AnnouncementLitSerializer(serializers.ModelSerializer):

    coments = CommentListSerializer(read_only=True, many=True)
    class Meta:
        model = Announcement
        fields = '__all__'





