from .models import programs,ProgCategory,ProgSeries
from .serializers import programsSerializer,ProgCategorySerializer,ProgSeriesSerializer
from rest_framework.response import Response
from rest_framework import viewsets
#from rest_framework import generics
#from rest_framework import mixins
#from rest_framework.authentication import TokenAuthentication, BasicAuthentication
#from rest_framework.permissions import IsAuthenticated

class ProgCategoryviewsets(viewsets.ModelViewSet):
    serializer_class = ProgCategorySerializer

    def get_queryset(self):
        progCategory = ProgCategory.objects.all()
        return progCategory

class ProgSeriesviewsets(viewsets.ModelViewSet):
    serializer_class = ProgSeriesSerializer

    def get_queryset(self):
        progSeries = ProgSeries.objects.all()
        return progSeries

class programsviewsets(viewsets.ModelViewSet):
    serializer_class = programsSerializer

    def get_queryset(self):
        Programs = programs.objects.all()
        return Programs


'''
class GenericAPIView(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin,
                     mixins.UpdateModelMixin, mixins.RetrieveModelMixin,
                     mixins.DestroyModelMixin):
    serializer_class = programsSerializer
    queryset = programs.objects.all()
    lookup_field = 'id'

    #authentication_classes = [TokenAuthentication,BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, id = None):

        if id:
            return self.retrieve(request)

        else:
           return self.list(request)

    def post(self, request):
        return self.create(request)

    def put(self, request, id=None):
        return self.update(request, id)

    def delete(self, request, id):
        return self.destroy(request, id)
'''
