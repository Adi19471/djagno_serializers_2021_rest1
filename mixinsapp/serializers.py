from  rest_framework import  serializers

from .models import NewLaptope,LaptopDetailes

class NewLaptopeSerializers(serializers.ModelSerializer):
    class Meta:
        model = NewLaptope
        fields = '__all__'


class LaptopDetailesSerializers(serializers.ModelSerializer):
    class Meta:
        model = LaptopDetailes
        fields = '__all__'