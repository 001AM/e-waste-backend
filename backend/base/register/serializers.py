from rest_framework import serializers
from base.register.models import *
from django.utils.translation import gettext_lazy as _
from rest_framework import serializers

class Base64ImageField(serializers.ImageField):

    def to_internal_value(self, data):
        from django.core.files.base import ContentFile
        import base64
        import six
        import uuid

        # Check if this is a base64 string
        if isinstance(data, six.string_types):
            # Check if the base64 string is in the "data:" format
            if 'data:' in data and ';base64,' in data:
                # Break out the header from the base64 content
                header, data = data.split(';base64,')

            # Try to decode the file. Return validation error if it fails.
            try:
                decoded_file = base64.b64decode(data)
            except TypeError:
                self.fail('invalid_image')

            # Generate file name:
            file_name = str(uuid.uuid4())[:12] # 12 characters are more than enough.
            # Get the file name extension:
            file_extension = self.get_file_extension(file_name, decoded_file)

            complete_file_name = "%s.%s" % (file_name, file_extension, )

            data = ContentFile(decoded_file, name=complete_file_name)

        return super(Base64ImageField, self).to_internal_value(data)

class EventCardSerializer(serializers.ModelSerializer):
    img = Base64ImageField(
        max_length=None, use_url=True,
    )
    img = Base64ImageField(max_length=None, use_url=True)
    
    class Meta:
        model = EventCard
        fields = '__all__'

    def create(self, validated_data):
        return EventCard.objects.create(**validated_data)

class EventRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventRegistration
        fields = '__all__'

class CastImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = CastImage
        fields = ['id', 'image', 'event']