from rest_framework import serializers
from allauthuserapp import models


class UserProfileSerializer(serializers.ModelSerializer):
    """Serializes a User Profile Object"""

    class Meta:
        model = models.UserProfile
        fields = ['id','email','name','password','mobile_no']
        extra_kwargs = {
            'password':{
                'write_only':True,
                'style':{'input_type':'password'}
            }
        }

    def create(self, validated_data):
        """Create and Return New user"""

        user = models.UserProfile.objects.create_user(
            email = validated_data['email'],
            name = validated_data['name'],
            mobile_no = validated_data['mobile_no'],
            password = validated_data['password']
        )

        return user

    def update(self, instance, validated_data):
        """Handle Updating User Account"""

        if 'password' in validated_data:
            password = validated_data.pop('password')
            instance.set_password(password)

        return super().update(instance, validated_data)
