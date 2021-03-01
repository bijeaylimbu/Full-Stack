from django.db.models import Q
from django.http import HttpResponseRedirect, Http404, JsonResponse
from django.shortcuts import render

# Create your views here.
from django.views import generic
from django_filters.rest_framework import DjangoFilterBackend, FilterSet
from rest_framework import filters
from rest_framework import viewsets, status, permissions, generics
from rest_framework.authentication import TokenAuthentication, SessionAuthentication, BasicAuthentication
from rest_framework.generics import RetrieveAPIView, get_object_or_404
from rest_framework.parsers import FileUploadParser, MultiPartParser, FormParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST
from rest_framework.views import APIView


from  . import  models
import django_filters
from . import serializers
from .models import PostAdd_Car, PostAdd_Bikes, PostAdd_Computer, PostAdd_Fashion, PostAdd_LandHouse, PostAdd_Phones, \
    PostAdvertise
from .serializers import AddPostSerializer, ItemDetailSerializer, CarDetailSerializer, AddBikesPostSerializer, AddComputerPostSerializer, AddFashionPostSerializer, AddLandPostSerializer, AddPhonesPostSerializer, BikesDetailSerializer,FashionDetailSerializer, PhonesDetailSerializer, ComputerDetailSerializer, LandDetailSerializer


class Filter(django_filters.FilterSet):
    # username=django_filters.CharFilter()

    class Meta:
        models=PostAdd_Car
        fields={

            'name':['icontains','iexact','gte','lte']
        }


class FilterBikes(django_filters.FilterSet):
    # username=django_filters.CharFilter()

    class Meta:
        models=PostAdd_Bikes
        fields={

            'name':['icontains','iexact','gte','lte']
        }

class FilterComputer(django_filters.FilterSet):
    # username=django_filters.CharFilter()

    class Meta:
        models=PostAdd_Computer
        fields={

            'name':['icontains','iexact','gte','lte']
        }

class FilterPhones(django_filters.FilterSet):
    # username=django_filters.CharFilter()

    class Meta:
        models=PostAdd_Phones
        fields={

            'name':['icontains','iexact','gte','lte']
        }


class FilterLand(django_filters.FilterSet):
    # username=django_filters.CharFilter()

    class Meta:
        models=PostAdd_LandHouse
        fields={

            'name':['icontains','iexact','gte','lte']
        }

class FilterFashion(django_filters.FilterSet):
    # username=django_filters.CharFilter()

    class Meta:
        models=PostAdd_Fashion
        fields={

            'name':['icontains','iexact','gte','lte']
        }






class PostAddViewset(viewsets.ModelViewSet):
    # authentication_classes = (SessionAuthentication, BasicAuthentication, TokenAuthentication)
    parser_classes = (MultiPartParser, FormParser,)

    queryset = PostAdd_Car.objects.all()
    serializer_class = serializers.AddPostSerializer
    # permission_classes = (
    #     permissions.IsAuthenticatedOrReadOnly,
    # )
    # permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)

    # permission_classes = [IsAuthenticated]
    permission_classes = (AllowAny,)
    filter_backends = [filters.SearchFilter]
    search_fields = ['$name']
    filterset_class=Filter





    def post(self, request,pk):
        serializer = AddPostSerializer(data=request.data)
        for file_entry in request.FILES.getlist('files'):
            uploaded_file_name = file_entry.name
            uploaded_file_content = file_entry.read()
            uploaded_file_content.save()
            return uploaded_file_name
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

    def delete(self, request, pk, format=None):
        event = self.get_object(pk)
        event.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    # def view(request):
    #     query = request.GET.get("query", None)
    #     car = PostAdd_Car.objects.all()
    #     phone = PostAdd_Phones.objects.all()
    #     computer = PostAdd_Computer.objects.all()
    #     fashion = PostAdd_Fashion.objects.all()
    #     bikes = PostAdd_Bikes.objects.all()
    #     land = PostAdd_LandHouse.objects.all()
    #
    #     if query:
    #         car = car.filter(name__icontains=query)
    #         phone = phone.filter(name__icontains=query)
    #         computer = computer.filter(name__icontains=query)
    #         fashion = fashion.filter(name__icontains=query)
    #         bikes = bikes.filter(name__icontains=query)
    #         land = land.filter(name__icontains=query)
    #
    #         return JsonResponse({"car": AddPostSerializer(instances=car, many=True).data,
    #                              "bikes": AddBikesPostSerializer(instances=bikes, many=True).data,
    #                              "phone": AddPhonesPostSerializer(instances=phone, many=True).data,
    #                              "computer": AddComputerPostSerializer(instances=computer, many=True).data,
    #                              "fashion": AddFashionPostSerializer(instances=fashion, many=True).data,
    #                              "land": AddLandPostSerializer(instances=land, many=True).data
    #
    #                              }
    #
    #                             )






class ItemDetailView(RetrieveAPIView):
        permission_classes = (AllowAny,)
        serializer_class = ItemDetailSerializer
        queryset = PostAdd_Car.objects.all()


    # def post(self, request, *args, **kwargs):
    #     posts_serializer = AddPostSerializer(data=request.data)
    #     if posts_serializer.is_valid():
    #         posts_serializer.save()
    #         return Response(posts_serializer.data, status=status.HTTP_201_CREATED)
    #     else:
    #         print('error', posts_serializer.errors)
    #         return Response(posts_serializer.errors, status=status.HTTP_400_BAD_REQUEST)









class AddToCartView(APIView):
    def post(self, request, *args, **kwargs):
        slug = request.data.get('slug', None)
        variations = request.data.get('variations', [])
        if slug is None:
            return Response({"message": "Invalid request"}, status=HTTP_400_BAD_REQUEST)







class PostAddViewsetBikes(viewsets.ModelViewSet):
    # authentication_classes = (SessionAuthentication, BasicAuthentication, TokenAuthentication)
    parser_classes = (MultiPartParser, FormParser,)

    queryset = PostAdd_Bikes.objects.all()
    serializer_class = serializers.AddBikesPostSerializer
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
    )
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)

    permission_classes = [IsAuthenticated]
    permission_classes = (AllowAny,)
    filter_backends = [filters.SearchFilter]
    search_fields = ['$name']
    filterset_class = FilterBikes


    def post(self, request, pk):
        serializer = AddBikesPostSerializer(data=request.data)
        for file_entry in request.FILES.getlist('files'):
            uploaded_file_name = file_entry.name
            uploaded_file_content = file_entry.read()
            uploaded_file_content.save()
            return uploaded_file_name
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)


class PostAddViewsetComputer(viewsets.ModelViewSet):
    # authentication_classes = (SessionAuthentication, BasicAuthentication, TokenAuthentication)
    parser_classes = (MultiPartParser, FormParser,)

    queryset = PostAdd_Computer.objects.all()
    serializer_class = serializers.AddComputerPostSerializer
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
    )
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)

    permission_classes = [IsAuthenticated]
    permission_classes = (AllowAny,)
    filter_backends = [filters.SearchFilter]
    search_fields = ['$name']
    filterset_class = FilterComputer

    def post(self, request, pk):
        serializer = AddComputerPostSerializer(data=request.data)
        for file_entry in request.FILES.getlist('files'):
            uploaded_file_name = file_entry.name
            uploaded_file_content = file_entry.read()
            uploaded_file_content.save()
            return uploaded_file_name
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)


class PostAddViewsetPhones(viewsets.ModelViewSet):
    # authentication_classes = (SessionAuthentication, BasicAuthentication, TokenAuthentication)
    parser_classes = (MultiPartParser, FormParser,)

    queryset = PostAdd_Phones.objects.all()
    serializer_class = serializers.AddPhonesPostSerializer
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
    )
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)

    permission_classes = [IsAuthenticated]
    permission_classes = (AllowAny,)
    filter_backends = [filters.SearchFilter]
    search_fields = ['$name']
    filterset_class = FilterPhones

    def post(self, request, pk):
        serializer = AddPhonesPostSerializer(data=request.data)
        for file_entry in request.FILES.getlist('files'):
            uploaded_file_name = file_entry.name
            uploaded_file_content = file_entry.read()
            uploaded_file_content.save()
            return uploaded_file_name
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)


class PostAddViewsetLand(viewsets.ModelViewSet):
    # authentication_classes = (SessionAuthentication, BasicAuthentication, TokenAuthentication)
    parser_classes = (MultiPartParser, FormParser,)

    queryset = PostAdd_LandHouse.objects.all()
    serializer_class = serializers.AddLandPostSerializer
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
    )
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)

    permission_classes = [IsAuthenticated]
    permission_classes = (AllowAny,)
    filter_backends = [filters.SearchFilter]
    search_fields = ['$name']
    filterset_class = FilterLand

    def post(self, request, pk):
        serializer = AddLandPostSerializer(data=request.data)
        for file_entry in request.FILES.getlist('files'):
            uploaded_file_name = file_entry.name
            uploaded_file_content = file_entry.read()
            uploaded_file_content.save()
            return uploaded_file_name
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)


class PostAddViewsetFashion(viewsets.ModelViewSet):
    # authentication_classes = (SessionAuthentication, BasicAuthentication, TokenAuthentication)
    parser_classes = (MultiPartParser, FormParser,)

    queryset = PostAdd_Fashion.objects.all()
    serializer_class = serializers.AddFashionPostSerializer
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
    )
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)

    permission_classes = [IsAuthenticated]
    permission_classes = (AllowAny,)
    filter_backends = [filters.SearchFilter]
    search_fields = ['$name']
    filterset_class = FilterFashion

    def post(self, request, pk):
        serializer = AddFashionPostSerializer(data=request.data)
        for file_entry in request.FILES.getlist('files'):
            uploaded_file_name = file_entry.name
            uploaded_file_content = file_entry.read()
            uploaded_file_content.save()
            return uploaded_file_name
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)


class ItemDetailViewCar(RetrieveAPIView):
    permission_classes = (AllowAny,)
    serializer_class = CarDetailSerializer
    queryset = PostAdd_Car.objects.all()


class ItemDetailViewBikes(RetrieveAPIView):
    permission_classes = (AllowAny,)
    serializer_class = BikesDetailSerializer
    queryset = PostAdd_Bikes.objects.all()


class ItemDetailViewLand(RetrieveAPIView):
    permission_classes = (AllowAny,)
    serializer_class = LandDetailSerializer
    queryset = PostAdd_LandHouse.objects.all()


class ItemDetailViewPhone(RetrieveAPIView):
    permission_classes = (AllowAny,)
    serializer_class = PhonesDetailSerializer
    queryset = PostAdd_Phones.objects.all()


class ItemDetailViewComputer(RetrieveAPIView):
    permission_classes = (AllowAny,)
    serializer_class = ComputerDetailSerializer
    queryset = PostAdd_Computer.objects.all()


class ItemDetailViewFashion(RetrieveAPIView):
    permission_classes = (AllowAny,)
    serializer_class = FashionDetailSerializer
    queryset = PostAdd_Fashion.objects.all()



class AddList(generics.ListAPIView):

    serializer_class = AddPostSerializer
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
    )
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)

    permission_classes = [IsAuthenticated]
    permission_classes = (AllowAny,)

    def get_queryset(self):
        return PostAdd_Car.objects.filter(username=self.kwargs['username'])



class AddList_bikes(generics.ListAPIView):

    serializer_class = AddBikesPostSerializer
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
    )
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)

    permission_classes = [IsAuthenticated]
    permission_classes = (AllowAny,)

    def get_queryset(self):
        return PostAdd_Bikes.objects.filter(username=self.kwargs['username'])



class AddList_fashion(generics.ListAPIView):

    serializer_class = AddFashionPostSerializer
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
    )
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)

    permission_classes = [IsAuthenticated]
    permission_classes = (AllowAny,)

    def get_queryset(self):
        return PostAdd_Fashion.objects.filter(username=self.kwargs['username'])



class AddList_computer(generics.ListAPIView):

    serializer_class = AddComputerPostSerializer
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
    )
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)

    permission_classes = [IsAuthenticated]
    permission_classes = (AllowAny,)

    def get_queryset(self):
        return PostAdd_Computer.objects.filter(username=self.kwargs['username'])


class AddList_phones(generics.ListAPIView):

    serializer_class = AddPhonesPostSerializer
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
    )
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)

    permission_classes = [IsAuthenticated]
    permission_classes = (AllowAny,)

    def get_queryset(self):
        return PostAdd_Phones.objects.filter(username=self.kwargs['username'])


class AddList_land(generics.ListAPIView):

    serializer_class = AddLandPostSerializer
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
    )
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)

    permission_classes = [IsAuthenticated]
    permission_classes = (AllowAny,)

    def get_queryset(self):
        return PostAdd_LandHouse.objects.filter(username=self.kwargs['username'])
#


# class UserListView(generics.ListAPIView):
#     queryset = PostAdd_Car.objects.all()
#     serializer_class = AddPostSerializer
#     filter_backends = [DjangoFilterBackend]
#     search_fields = ('color')


    # def get_queryse(self):
    #    return PostAdd_Car.objects.filter(color='')




    # def get_queryset(self, request, *args, **kwargs):
    #     queryset = PostAdd_Car.objects.all()
    #     keywords = self.request.query_params.get('search')
    #     if keywords:
    #         queryset = queryset.filter(image_keyword__in=keywords.split(','))
    #     return queryset


#
# class ArticleFilterSet(FilterSet):
#     class Meta:
#         model = PostAdd_Car
#         fields = ('color', )

# class SearchPost(generics.ListAPIView):
#         serializer_class = AddPostSerializer
#         model = serializer_class.Meta.model
#         paginate_by = 100
#
#         def get_queryset(self):
#             query = self.kwargs.get('q')
#             if query:
#                 return self.model.objects.filter(
#                     Q(name_icontains=query)
#
#
#                 ).distinct()
#             return None


class PostAdvertise(viewsets.ModelViewSet):

    parser_classes = (MultiPartParser, FormParser,)

    queryset = PostAdvertise.objects.all()
    serializer_class = serializers.PostAdvertise
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
    )
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)

    permission_classes = [IsAuthenticated]
    permission_classes = (AllowAny,)

    def post(self, request, pk):
        serializer = PostAdvertise(data=request.data)
        for file_entry in request.FILES.getlist('files'):
            uploaded_file_name = file_entry.name
            uploaded_file_content = file_entry.read()
            uploaded_file_content.save()
            return uploaded_file_name
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)