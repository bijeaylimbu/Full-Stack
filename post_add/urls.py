from django.urls import path, include
from rest_framework import routers


from .views import PostAddViewset, ItemDetailView, PostAddViewsetBikes, PostAddViewsetFashion, PostAddViewsetComputer, PostAddViewsetLand, PostAddViewsetPhones, ItemDetailViewCar, ItemDetailViewBikes, ItemDetailViewComputer,ItemDetailViewFashion, ItemDetailViewLand, ItemDetailViewPhone, AddList,AddList_land,AddList_fashion,AddList_bikes,AddList_phones,AddList_computer,PostAdvertise

router_addpost=routers.DefaultRouter()
router_addpost.register('',PostAddViewset,'addpost')


router_addpost_bikes = routers.DefaultRouter()
router_addpost_bikes.register('', PostAddViewsetBikes,'addpost')

router_addpost_fashion = routers.DefaultRouter()
router_addpost_fashion.register('',PostAddViewsetFashion,'addpost')

router_addpost_computer = routers.DefaultRouter()
router_addpost_computer.register('',PostAddViewsetComputer,'addpost')

router_addpost_land = routers.DefaultRouter()
router_addpost_land.register('',PostAddViewsetLand,'addpost')

router_addpost_phones = routers.DefaultRouter()
router_addpost_phones.register('',PostAddViewsetPhones,'addpost')


router_advertise = routers.DefaultRouter()
router_advertise.register('', PostAdvertise,'addpost')

urlpatterns = [

    path('addpost/',include(router_addpost.urls),),

    path('cars/<username>', AddList.as_view()),
    path('computer/<username>', AddList_computer.as_view()),
    path('bikes/<username>', AddList_bikes.as_view()),
    path('phones/<username>', AddList_phones.as_view()),
    path('fashion/<username>', AddList_fashion.as_view()),
    path('land/<username>', AddList_land.as_view()),
    path('addpost/<pk>/', ItemDetailView.as_view(), name='product-detail'),
    path('advertise/', include(router_advertise.urls), ),
    path('addpost_bikes/', include(router_addpost_bikes.urls), ),
    path('addpost_fashion/', include(router_addpost_fashion.urls), ),
    path('addpost_land/', include(router_addpost_land.urls), ),
    path('addpost_phones/', include(router_addpost_phones.urls), ),
    path('addpost_computer/', include(router_addpost_computer.urls), ),

    path('addpost_bikes/<pk>/', ItemDetailViewBikes.as_view(), name='product-detail'),
    path('addpost_computer/<pk>/', ItemDetailViewComputer.as_view(), name='product-detail'),
    path('addpost_phones/<pk>/', ItemDetailViewPhone.as_view(), name='product-detail'),
    path('addpost_land/<pk>/', ItemDetailViewLand.as_view(), name='product-detail'),
    path('addpost_fashion/<pk>/', ItemDetailViewFashion.as_view(), name='product-detail'),
    # path('SearchPost/', SearchPost.as_view()),

]


# PostAdvertise