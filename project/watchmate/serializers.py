from rest_framework import serializers
from .models import Movie


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        # fields = '__all__'
        exclude = ['active']

    # Field level validation (Validation for title field)
    def validate_title(self,value):
        if len(value) <= 3:
            raise serializers.ValidationError("Title is too short")
        else:
            return value
        
    #Object level validation 
    def validate(self, data):
        title = data.get('title')
        description = data.get('description')
        if title == description:
            raise serializers.ValidationError(
                "Title and Description should not be the same")
        else:
            return data
    





# class MovieSerializer(serializers.Serializer):
#     id=serializers.IntegerField(read_only=True)
#     title=serializers.CharField(max_length=100)
#     description=serializers.CharField(max_length=1000)
#     active=serializers.BooleanField(default=True)

#     # Create a new movie object
#     def create(self, validated_data):
#         return Movie.objects.create(**validated_data)
    
#     # Check if the movie already exists in the database
#     def validate(self, data):
#         title = data.get('title')
#         existing_movie = Movie.objects.filter(title=title).first()
#         if existing_movie:
#             raise serializers.ValidationError('This movie already exists.')
#         return data
    
#     # Update an existing movie object
#     def update(self, instance, validated_data):
#         instance.title = validated_data.get('title', instance.title)
#         instance.description = validated_data.get(
#             'description', instance.description)
#         instance.active = validated_data.get('active', instance.active)
#         instance.save()
#         return instance
    
#     #Field level validation (Validation for title field)
#     def validate_title(self,value):
#         if len(value) <= 3:
#             raise serializers.ValidationError("Title is too short")
#         else:
#             return value
        
#     #Object level validation 
#     def validate(self, data):
#         title = data.get('title')
#         description = data.get('description')
#         if title == description:
#             raise serializers.ValidationError(
#                 "Title and Description should not be the same")
#         else:
#             return data
    

