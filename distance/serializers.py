from rest_framework import serializers
from .models import Result


class ResponseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Result
        fields = ('created', 'name', 'latitude', 'longitude',
                  'radius', 'calculation', )


class LocationSerializer(serializers.Serializer):
    lat = serializers.DecimalField(decimal_places=20, max_digits=50)
    lng = serializers.DecimalField(decimal_places=20, max_digits=50)


class ResultSerializer(serializers.Serializer):
    location = LocationSerializer()
    distance = serializers.DecimalField(decimal_places=20, max_digits=50)
    name = serializers.CharField()


class PlacesSerializer(serializers.Serializer):
    results = ResultSerializer
    radius = serializers.IntegerField
    status = serializers.CharField

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'])

        user.set_password(validated_data['password'])
        user.save()

        return user