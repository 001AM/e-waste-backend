from rest_framework import serializers
from base.models import CustomUser,UserProducts
from django.utils.translation import gettext_lazy as _
from rest_framework.parsers import MultiPartParser, FormParser

from rest_framework import serializers    

class Base64ImageField(serializers.ImageField):
    """
    A Django REST framework field for handling image-uploads through raw post data.
    It uses base64 for encoding and decoding the contents of the file.

    Heavily based on
    https://github.com/tomchristie/django-rest-framework/pull/1268

    Updated for Django REST framework 3.
    """

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

    def get_file_extension(self, file_name, decoded_file):
        import imghdr

        extension = imghdr.what(file_name, decoded_file)
        extension = "jpg" if extension == "jpeg" else extension

        return extension
    
class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('email','username','phone')

    def create(self, validated_data):
        email = validated_data.get('email')
        username = validated_data.get('username')
        phone = validated_data.get('phone')
        password = validated_data.get('password')

        if not email:
            raise ValueError(_('The Email must be set'))

        user = CustomUser(email=email, username=username, phone=phone)
        user.set_password(password)  # Set the password using set_password method
        user.save()
        return user
    
class CustomUserDetailsSerializer(serializers.ModelSerializer):
    parser_classes = (MultiPartParser, FormParser)
    user_image = Base64ImageField(
        max_length=None, use_url=True,
    )
    class Meta:
        model = CustomUser
        exclude=['password','is_active','is_superuser']

class CustomUserProductSerializer(serializers.ModelSerializer):
    parser_classes = (MultiPartParser, FormParser)
    product_image = Base64ImageField(
        max_length=None, use_url=True,
    ) 
    class Meta:
        model = UserProducts
        fields ='__all__'
        read_only_fields = ('user',)