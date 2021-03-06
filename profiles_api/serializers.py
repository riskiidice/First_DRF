from rest_framework import serializers

from . import models

class HelloSerializer(serializers.Serializer):
    """Serializes a name field for testing out APIView"""

    name = serializers.CharField(max_length=10)

class UserProfileSerializer(serializers.ModelSerializer):
    """Serialzer for user Profile"""

    class Meta:
        model = models.UserProfile
        fields = ['id','name','email','password']
        extra_kwargs = {'password' : { 'write_only' : True}}

    def create(self, validated_data):
        """ Created and return new user"""

        user = models.UserProfile(
            email = validated_data['email'],
            name = validated_data['name']
        )

        user.set_password(validated_data['password'])
        user.save()

        return user

class ProfileFeedItemSerializer(serializers.ModelSerializer):
    """docstring for ProfileFeedItemSerializer."""
    class Meta:
        model = models.ProfileFeedItem
        fields = ['id','user_profile','status_text','created_on']
        extra_kwargs = {'user_profile' : { 'read_only' : True}}
