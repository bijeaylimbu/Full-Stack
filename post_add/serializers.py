from rest_framework import serializers


from .models import PostAdd_Car,PostAdd_Bikes, PostAdd_Computer, PostAdd_Fashion, PostAdd_LandHouse, PostAdd_Phones,PostAdvertise

class AddPostSerializer(serializers.ModelSerializer):
    class Meta:
        model=PostAdd_Car

        fields='__all__'


class ItemDetailSerializer(serializers.ModelSerializer):
    category = serializers.SerializerMethodField()
    label = serializers.SerializerMethodField()
    variations = serializers.SerializerMethodField()

    class Meta:
        model = PostAdd_Car
        fields = '__all__'


class CarDetailSerializer(serializers.ModelSerializer):
    category = serializers.SerializerMethodField()
    label = serializers.SerializerMethodField()
    variations = serializers.SerializerMethodField()

    class Meta:
        model = PostAdd_Car

        fields = '__all__'


class AddBikesPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostAdd_Bikes

        fields = '__all__'


class BikesDetailSerializer(serializers.ModelSerializer):
    category = serializers.SerializerMethodField()
    label = serializers.SerializerMethodField()
    variations = serializers.SerializerMethodField()

    class Meta:
        model = PostAdd_Bikes

        fields = '__all__'


class AddComputerPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostAdd_Computer

        fields = '__all__'


class ComputerDetailSerializer(serializers.ModelSerializer):
    category = serializers.SerializerMethodField()
    label = serializers.SerializerMethodField()
    variations = serializers.SerializerMethodField()

    class Meta:
        model = PostAdd_Computer

        fields = '__all__'


class AddPhonesPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostAdd_Phones

        fields = '__all__'


class PhonesDetailSerializer(serializers.ModelSerializer):
    category = serializers.SerializerMethodField()
    label = serializers.SerializerMethodField()
    variations = serializers.SerializerMethodField()

    class Meta:
        model = PostAdd_Phones

        fields = '__all__'


class AddFashionPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostAdd_Fashion

        fields = '__all__'


class FashionDetailSerializer(serializers.ModelSerializer):
    category = serializers.SerializerMethodField()
    label = serializers.SerializerMethodField()
    variations = serializers.SerializerMethodField()

    class Meta:
        model = PostAdd_LandHouse

        fields = '__all__'


class AddLandPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostAdd_LandHouse

        fields = '__all__'


class LandDetailSerializer(serializers.ModelSerializer):
    category = serializers.SerializerMethodField()
    label = serializers.SerializerMethodField()
    variations = serializers.SerializerMethodField()

    class Meta:
        model = PostAdd_LandHouse

        fields = '__all__'



class PostAdvertise(serializers.ModelSerializer):
    class Meta:
        model = PostAdvertise

        fields = '__all__'