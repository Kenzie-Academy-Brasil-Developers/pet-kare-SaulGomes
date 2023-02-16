from rest_framework import serializers


class GroupsSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    created_at = serializers.DateTimeField(read_only=True)
    scientific_name = serializers.CharField(max_lenght=50)
