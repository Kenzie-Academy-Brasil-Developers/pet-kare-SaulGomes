from rest_framework import serializers
from ..groups import GroupsSerializer
from ..traits import TraitsSerializer
from .models import PetChoices


class PetsSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_lenght=50)
    age = serializers.IntegerField()
    weight = serializers.FloatField()
    sex = serializers.ChoiceField(choices=PetChoices.choices, default=PetChoices.DEFAULT)
    group = GroupsSerializer()
    traits = TraitsSerializer(many=True)
