from .models import Drone, DroneCategory, Pilot, Competition
from rest_framework import serializers #import HyperlinkedModelSerializer

class DroneCategorySerializer(serializers.HyperlinkedModelSerializer):
    drones = serializers.HyperlinkedRelatedField(
        many =True,
        read_only = True,
        view_name = 'drone-detail'
    )
    
    class Meta:
        model = DroneCategory
        fields = (
            'url',
            'pk',
            'name',
            'drones'
        )
        
class DroneSerializer(serializers.HyperlinkedModelSerializer):
    drone_category = serializers.SlugRelatedField(
        queryset= DroneCategory.objects.all(),
        slug_field='name')
    class Meta:
        model = Drone
        fields = (
            'url',
            'name',
            'drone_category',
            'manufacturing_date',
            'has_it_competed',
            'inserted_timestamp'
        )
        
class CompetitionSerializer(serializers.ModelSerializer):
    # Display all details for related drone
    drone = DroneSerializer(read_only=True)
    class Meta:
        model = Competition
        fields =  (
            'url',
            'pk',
            'distance_in_feet',
            'distance_achievement_date',
            'drone',
            'pilot'
        )
        
        
class PilotSerializer(serializers.HyperlinkedModelSerializer):
    competitions = CompetitionSerializer(many= True, read_only=True)
    gender = serializers.ChoiceField(
        choices =  Pilot.GENDER_CHOICES
    )
    gender_description = serializers.CharField(
        source = 'get_gender_display',
        read_only= True
    )
    
    class Meta:
        model = Pilot
        fields =(
            'url',
            'name',
            'gender',
            'gender_description',
            'races_count',
            'inserted_timestamp',
            'competitions',
        )


class PilotCompetitionSerializer(serializers.ModelSerializer):
    
    #Display the pilot's name
    pilot= serializers.SlugRelatedField(
        queryset=Pilot.objects.all(),
        slug_field='name'
    )
    
    #Display the drone's name
    drone= serializers.SlugRelatedField(
        queryset=Drone.objects.all(),
        slug_field = 'name'
        
    )
    
    class Meta:
        model = Competition
        fields = (
            'url',
            'pk',
            'distance_in_feet',
            'distance_achievement_date',
            'pilot',
            'drone'
        )
 
 
class pilots(serializers.ModelSerializer):
    new_pilot = serializers.SerializerMethodField()
    
    def get_new_pilot(self, obj):
        if obj.races_count ==0:
            return "New Racer"
        else:
            return "old racer"
            
    
    class Meta:
        model = Pilot
        fields = '__all__' 
          
class cat(serializers.ModelSerializer):
    pilot = pilots()
    
    
    class Meta:
        model = Competition
        fields = '__all__'