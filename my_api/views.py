from rest_framework import viewsets
from rest_framework.serializers import ValidationError
from rest_framework import permissions
from my_api.models import User, Message
from my_api.serializers import UserSerializer, MessageSerializer


class IsSelfPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user == obj


class UserViewSet(viewsets.ModelViewSet):
    '''
    ViewSet related to the User model
    '''
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = (IsSelfPermission,)


class MessageViewSet(viewsets.ModelViewSet):
    '''
    ViewSet related to the Message model
    '''
    serializer_class = MessageSerializer
    queryset = Message.objects.all()

    def perform_create(self, serializer):
        '''
        Hook executed during the creation of a Message instance
        '''
        user = self.request.user

        if not user.is_authenticated(): 	# request sent by an anonymous user
            raise ValidationError({'detail':'You have to connect to send a message.'}, code=400)

        serializer.validated_data['user'] = user
        serializer.save()