from api.serializers import Base64ImageField
from django.conf import settings
from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Usuario


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email')


class UsuarioSerializer(serializers.ModelSerializer):

    user = UserSerializer()
    avatar = serializers.SerializerMethodField()

    class Meta:
        model = Usuario
        exclude = ['proveedor']

    def get_avatar(self, obj):

        if obj.avatar:

            if hasattr(settings, 'IMAGE_URL'):

                return settings.IMAGE_URL.format(obj.avatar.url)

            return obj.avatar.url

    def update(self, instance, validated_data):

        serializer = UserSerializer(instance.user, data=validated_data.get('user'), partial=True)

        if serializer.is_valid():

            serializer.save()

        instance.telefono = validated_data.get('telefono', instance.telefono)
        instance.save()

        return instance


class AvatarSerializer(serializers.ModelSerializer):

    avatar = Base64ImageField(
        max_length=None,
        use_url=True
    )

    _avatar = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Usuario
        fields = ['avatar', '_avatar']

    def get__avatar(self, obj):

        if obj.avatar:

            if hasattr(settings, 'IMAGE_URL'):
                return settings.IMAGE_URL.format(obj.avatar.url)

        return obj.avatar.url
