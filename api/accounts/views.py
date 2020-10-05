from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import CreateAPIView
from .serializers import UserSerializer
from accounts.models import User
from rest_framework.permissions import AllowAny, IsAuthenticated


class UserViewSet(ModelViewSet):
    '''
    list: List All the Users
    create: Create a new user i.e. Register
    retrieve: Retrieve a single user instance based on username
    '''
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]
    http_method_names = ['get', 'head', 'put', 'patch', 'head']

    def get_serializer_class(self):
        return super(UserViewSet, self).get_serializer_class()

    def get_object(self):
        pk = self.kwargs.get('pk')

        if pk == 'me':
            return self.request.user

        return super(UserViewSet, self).get_object()


class CreateOrganizationView(CreateAPIView):
    serializer_class=UserSerializer
    permission_classes=[AllowAny]