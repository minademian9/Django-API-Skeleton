from rest_framework import serializers

from character.models import Character


class characterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Character
        fields = "__all__"
