from rest_framework import serializers
from team_person.models import Team, Person


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ['id', 'title']


class PersonSerializer(serializers.ModelSerializer):
    team = serializers.SlugRelatedField(slug_field='title', queryset=Team.objects.all(), many=True)

    class Meta:
        model = Person
        fields = ['id', 'first_name', 'last_name', 'email', 'team']
