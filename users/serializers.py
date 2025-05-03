from rest_framework import serializers
from .models import CustomUser

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'  # Yaha fields ko specify kar sakte ho, jaise 'username', 'email', etc.
        
    # Agar password ko exclude karna hai
    password = serializers.CharField(write_only=True, required=False, allow_blank=True)

    def update(self, instance, validated_data):
        # Password ko update request se remove karna (Agar password field ko nahi update karna)
        validated_data.pop('password', None)
        
        # Update remaining fields
        return super().update(instance, validated_data)
