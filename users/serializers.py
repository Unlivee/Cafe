from rest_framework import serializers
from .models import User
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']
        extra_kwargs = {
            'password': {"write_only": True}
        }
        def create(self, validated_date):
            password = validated_date.pop('password', None)
            instance = self.Meta.model(**validated_date)
            if password is not None:
                instance.set_password()
            instance.save()
            return instance

