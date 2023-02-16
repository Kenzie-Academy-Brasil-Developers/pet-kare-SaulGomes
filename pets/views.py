from django.forms import model_to_dict
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import PetsSerializer
from ..groups.models import Group
from ..traits.models import Trait
from .models import Pet
# Create your views here.

class PetViews(APIView):
    def post(self, request):
        serializer = PetsSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        group = serializer.validated_data.pop("group")
        traits = serializer.validated_data.pop("traits")

        group_objeto = Group.objects.filter(scientific_name__iexact=group["scientific_name"]).first()
        if not group_objeto:
            new_group = Group.objects.create(**group)
            pet = Pet.objects.create(**serializer.validated_data, group=new_group)
        else:
            pet = Pet.objects.create(**serializer.validated_data, group=group_objeto)
        

        for trait in traits:
            trait_object = Trait.objects.filter(name__iexact=trait["name"]).first()
            if not trait_object:
                trait_object = Trait.objects.create(**trait)
            pet.traits.add(trait_object)
        
        serializer = PetsSerializer(pet)
        return Response(serializer.data, status=200)

    def get(self, request, pet_id):
        try:
            unique_pet = Pet.objects.get(id=pet_id)
            return Response(model_to_dict(unique_pet), 200)
        except Pet.DoesNotExist:
            return Response({"message": "Pet not found"}, 404)
