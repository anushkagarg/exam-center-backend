from rest_framework.serializers import ModelSerializer, CharField
from django.contrib.auth import get_user_model

User = get_user_model()



class UserSerializer(ModelSerializer):
    user_type = CharField(source='get_user_type_display')

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'user_type')
        extra_kwargs = {
            'password': {'write_only': True, 'style': {
                'input_type': 'password'
            }}
        }

    def create(self, validated_data):
        user = User(
            username=validated_data['username'], email=validated_data['email'])
        user.set_password(validated_data['password'])
        user.save()

        return user