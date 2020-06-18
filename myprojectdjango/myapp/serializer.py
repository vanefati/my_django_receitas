from rest_framework import serializers
from .models import Receitas

class ReceitasSerializer(serializers.ModelSerializer):

    class Meta:

        model = Receitas
        fields = '__all__'