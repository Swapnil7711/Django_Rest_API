from rest_framework import serializers
from .models import AppUsers


class usersSerializer(serializers.ModelSerializer):

    class Meta:

        model = AppUsers

        fields = '__all__'