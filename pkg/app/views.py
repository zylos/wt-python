from django.shortcuts import render

from app.models import DataSet, Resource, Tag, DataSetExtra, Group
from app.models import DataSetResource
from app.serializers import DataSetSerializer, ResourceSerializer
from app.serializers import TagSerializer, DataSetExtraSerializer
from app.serializers import GroupSerializer

from rest_framework import generics, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.views import APIView


@api_view(('GET',))
def api_root(request, format=None):
    return Response({
        'datasets': reverse('dataset-list', request=request, format=format),
        'resources': reverse('resource-list', request=request, format=format),
        'groups': reverse('group-list', request=request, format=format),
        'tags': reverse('tag-list', request=request, format=format)
    })


###
# Generic APIViews
###
class DataSetList(generics.ListCreateAPIView):
    queryset = DataSet.objects.all()
    serializer_class = DataSetSerializer

class DataSetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = DataSet.objects.all()
    serializer_class = DataSetSerializer

class ResourceList(generics.ListCreateAPIView):
    queryset = Resource.objects.all()
    serializer_class = ResourceSerializer

class ResourceDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Resource.objects.all()
    serializer_class = ResourceSerializer

class GroupList(generics.ListCreateAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class GroupDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class TagList(generics.ListCreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer



###
# DataSet Resource Views
###
# Ehhh really not the best API, especially with the confusing 
# undocumented post methods to add a resource but I'll change it later
class DataSetResourceList(APIView):
    def get_object(self, pk):
        try:
            return DataSet.objects.get(pk=pk)
        except DataSet.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        dataset = self.get_object(pk)
        serializer = ResourceSerializer(dataset.resources, many=True)
        return Response(serializer.data)

class DataSetResourceDetail(APIView):
    def get_object(self, pk):
        try:
            return DataSet.objects.get(pk=pk)
        except DataSet.DoesNotExist:
            raise Http404

    def get_resource(self, pk):
        try:
            return Resource.objects.get(pk=pk)
        except Resource.DoesNotExist:
            raise Http404

    def get_dsr(self, pk, pk_res):
        try:
            return DataSetResource.objects.get(dataset=pk, resource=pk_res)
        except DataSetResource.DoesNotExist:
            raise Http404

    def post(self, request, pk, pk_res, format=None):
        dataset = self.get_object(pk)
        resource = self.get_resource(pk_res)
        resources = DataSetResource.objects.filter(dataset=dataset)

        dsr = DataSetResource(
            dataset=dataset, resource=resource, position=0)
        dsr.save()

        return Response(status=status.HTTP_201_CREATED)

    def delete(self, request, pk, pk_res, format=None):
        dataset = self.get_object(pk)
        resource = self.get_resource(pk_res)
        #dsr = self.get_dsr(pk, pk_res)
        #dsr_pos = dsr.position

        DataSetResource.objects.filter(
            dataset=dataset, resource=resource).delete()

        #TODO# For later I guess
        # Move all resources above down one
        #DataSetResource.objects.filter(position__gt=dsr_pos).update(
        #    position=F('position') - 1)

        return Response(status=status.HTTP_204_NO_CONTENT)



###
# DataSet Extra Views
###
class DataSetExtraList(APIView):
    def get_object(self, pk):
        try:
            return DataSet.objects.get(pk=pk)
        except DataSet.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        dataset = self.get_object(pk)
        serializer = DataSetExtraSerializer(dataset.datasetextra_set, many=True)
        return Response(serializer.data)

    def post(self, request, pk, format=None):
        dataset = self.get_object(pk)

        serializer = DataSetExtraSerializer(data=request.data)
        if serializer.is_valid():
            try:
                dataset.datasetextra_set.get(name=serializer.data['name'])
                return Response(
                    'Extra with name already exists. Use PUT', 
                    #Not really a good code but oh well. good enough for a test
                    status=status.HTTP_409_CONFLICT) 
            except DataSetExtra.DoesNotExist:
                serializer.save(dataset=dataset)

            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DataSetExtraDetail(APIView):
    def get_object(self, pk):
        try:
            return DataSet.objects.get(pk=pk)
        except DataSet.DoesNotExist:
            raise Http404

    def get_extra(self, pk, pk_extra):
        try:
            return self.get_object(pk).datasetextra_set.get(name=pk_extra)
        except Resource.DoesNotExist:
            raise Http404

    def put(self, request, pk, pk_extra, format=None):
        serializer = DataSetExtraSerializer(
            self.get_extra(pk, pk_extra), data=request.data)
        if serializer.is_valid():
            serializer.save(dataset=self.get_object(pk))
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, pk_extra, format=None):
        self.get_extra(pk, pk_extra).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)