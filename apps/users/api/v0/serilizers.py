from rest_framework import serializers

from django.contrib.auth import get_user_model

User = get_user_model()



class UserCreateSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(max_length=20, write_only=True)

    class Meta:
        model = User
        fields = ('username', 'password', 'password2')

        extra_kwargs = {
            'password' : {'write_only': True}
        }

    def validate(self, attrs):
        password = attrs.get('password')
        password2 = attrs.pop('password2')
        if password != password2:
            raise serializers.ValidationError("Passwords does not  must match")
        return attrs


    # def create(self, validated_data):
    #     return User.objects.create_user(**validated_data)



    def create(self, validated_data):
        print(validated_data)
        user = User(
            username=validated_data['username'],

        )
        user.set_password(validated_data['password'])
        user.save()
        return user





class UsersListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username')
        extra_kwargs = {
            'id' : {'read_only': True},
            'username' : {'read_only': True},

        }

