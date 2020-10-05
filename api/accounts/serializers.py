from rest_framework.serializers import ModelSerializer, CharField, SerializerMethodField
from django.contrib.auth import get_user_model

User = get_user_model()



class UserSerializer(ModelSerializer):
    first_name = SerializerMethodField(read_only=True)
    last_name = SerializerMethodField(read_only=True)
    name = SerializerMethodField(read_only=True)


    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'user_type', 'first_name', 'last_name', 'name', 'organization')
        extra_kwargs = {
            'password': {'write_only': True, 'style': {
                'input_type': 'password'
            }},
            'organization': {'read_only': True},
            'user_type': {'read_only': True}
        }

    def get_first_name(self, obj):
        try:
            return obj.profile.first_name
        except:
            return ''

    def get_last_name(self, obj):
        try:
            return obj.profile.last_name
        except:
            return ''

    def get_name(self, obj):
        try:
            return obj.profile.name
        except:
            return ''

    def create(self, validated_data):
        user = User(
            username=validated_data['username'], email=validated_data['email'], user_type='O')
        user.set_password(validated_data['password'])
        user.save()

        return user

    def to_representation(self, obj):
        # get the original representation
        ret = super(UserSerializer, self).to_representation(obj)

        if obj.user_type == 'O':
            ret.pop('first_name')
            ret.pop('last_name')
            ret.pop('organization')
        else:
            ret.pop('name')
        return ret