from rest_framework.serializers import ModelSerializer

from tip.models import Tip


class TipSerializer(ModelSerializer):
    # usagedata = serializers.SerializerMethodField()

    class Meta:
        model = Tip
        fields = '__all__'