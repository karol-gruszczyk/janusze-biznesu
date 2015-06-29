from rest_framework import generics, serializers

from .models import Share, ShareRecord


class ShareRecordSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ShareRecord
        fields = ('date', 'open', 'close', 'low', 'high', 'volume')


class ShareSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Share
        fields = ('name', 'verbose_name', 'updated_daily')


class ShareListAPIView(generics.ListAPIView):
    serializer_class = ShareSerializer
    queryset = Share.objects.all()


class ShareRecordListAPIView(generics.ListAPIView):
    serializer_class = ShareRecordSerializer

    def get_queryset(self):
        return ShareRecord.objects.filter(share__pk=self.kwargs['pk'])
