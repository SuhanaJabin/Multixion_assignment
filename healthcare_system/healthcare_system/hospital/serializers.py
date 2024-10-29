from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from .models import User, Patient
from django.contrib.auth import authenticate
from django.utils.translation import gettext as _
class PatientSignupSerializer(serializers.ModelSerializer):
    age = serializers.IntegerField(required=True)
    blood_group = serializers.ChoiceField(choices=[
        ('A+', 'A+'), ('A-', 'A-'),
        ('B+', 'B+'), ('B-', 'B-'),
        ('AB+', 'AB-'),
        ('O+', 'O-')
    ])
    phone_no = serializers.CharField(max_length=15, required=False, allow_blank=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'age', 'blood_group', 'phone_no']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        # Extract patient-specific information
        age = validated_data.pop('age')
        blood_group = validated_data.pop('blood_group')
        phone_no = validated_data.pop('phone_no', '')

        # Create the User with the role 'patient'
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            role='patient',
            password=make_password(validated_data['password'])  # Hash password
        )

        # Create the associated Patient profile
        Patient.objects.create(user=user, age=age, blood_group=blood_group, phone_no=phone_no)
        
        return user
    
class PatientLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        # Authenticate the user
        user = authenticate(email=email, password=password)

        if user is None:
            raise serializers.ValidationError(_("Invalid email or password."))

        attrs['user'] = user  # Add the user object to the validated data
        return attrs

class PatientDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ['user', 'age', 'blood_group', 'phone_no'] 
