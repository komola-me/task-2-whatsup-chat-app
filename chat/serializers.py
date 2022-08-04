from rest_framework import serializers
from common.models import User
from chat.models import Chat, Message


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name']


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = "__all__"


class ChatListSerializer(serializers.ModelSerializer):
    last_message_date = serializers.DateTimeField()
    last_message = serializers.StringRelatedField()
    profile_image = serializers.StringRelatedField()
    profile_title = serializers.StringRelatedField()
    is_unmuted = serializers.BooleanField()
    is_pinned = serializers.BooleanField()

    class Meta:
        model = Chat
        fields = ('id', 'last_message', 'last_message_date',
                  "profile_image", 'profile_title','is_unmuted', 'is_pinned')


class ChatDetailSerializer(serializers.ModelSerializer):
    #members = UserSerializer()
    class Meta:
        model = Message
        fields = ['from_user', 'text',]
        

