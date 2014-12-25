from rest_framework import serializers, viewsets
from app.models import DataSet, Resource, Tag, DataSetExtra, Group

class TaggedField(serializers.StringRelatedField):
    # Handles deduplication of tags
    def to_internal_value(self, data):
        try:
            return Tag.objects.get(name=data)
        except Tag.DoesNotExist:
            tag = Tag(name=data)
            tag.save()
            
            return tag

class RatingsAvgField(serializers.Field):
     def to_representation(self, ratings):
        avg = 0
        count = 0

        for rating in ratings:
            avg += rating.rating
            count += 1

        if count == 0:
            return 0;
        else:
            return "%f" % (avg/count);

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('name', )

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('uuid', 'name')

class ResourceSerializer(serializers.ModelSerializer):
    group = GroupSerializer(read_only=True, required=False, allow_null=True)

    class Meta:
        model = Resource
        fields = ('uuid', 'url', 'name', 'desc', 'group')

class DataSetExtraSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataSetExtra
        fields = ('name', 'content')

class DataSetSerializer(serializers.HyperlinkedModelSerializer):
    tags = TaggedField(many=True)
    resources = ResourceSerializer(many=True, read_only=True)
    extras = DataSetExtraSerializer(
        many=True, source='datasetextra_set', 
        read_only=True
    )

    rating_avg = RatingsAvgField(
        source='datasetrating_set.all', 
        read_only=True
    )
    rating_count = serializers.IntegerField(
        source='datasetrating_set.count', 
        read_only=True
    )

    resource = serializers.HyperlinkedIdentityField(
        view_name='dataset-resource-list', format='html')
    extra = serializers.HyperlinkedIdentityField(
        view_name='dataset-extra-list', format='html')

    class Meta:
        model = DataSet
        fields = (  'uuid', 'title', 'url_name', 'version', 'url', 
                    'notes', 'set_type', 'is_private', 'is_open', 
                    'activity_state', 'tags', 'resources', 'extras',
                    'rating_avg', 'rating_count', 'resource', 'extra'
                    )


class DataSetViewSet(viewsets.ModelViewSet):
    queryset = DataSet.objects.all()
    serializer_class = DataSetSerializer

class ResourceViewSet(viewsets.ModelViewSet):
    queryset = Resource.objects.all()
    serializer_class = ResourceSerializer


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer