from djoser.serializers import UserCreateSerializer as BaseUserCreateSericalizer


class UserCreateSerializer(BaseUserCreateSericalizer):
    class Meta(BaseUserCreateSericalizer.Meta):
        fields = ['id', 'username', 'password', 'email', 'first_name', 'last_name']
        