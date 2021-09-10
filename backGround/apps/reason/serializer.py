from rest_framework.serializers import ModelSerializer

from reason.models import Reason


class ReasonSerializer(ModelSerializer):
    # usagedata = serializers.SerializerMethodField()

    class Meta:
        model = Reason
        fields = '__all__'