from rest_framework.viewsets import ViewSet
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.response import Response
from ..service.ambience_emotion_classification_service import (
    AmbienceEmotionClassifactionService,
)

class AmbienceEmotionClassificationViewset(ViewSet):
    def process_image(self, request, *args, **kwargs):
        image_file = request.FILES.get("image")
        if not image_file:
            return Response({"error": "No image provided"}, status=HTTP_400_BAD_REQUEST)

        metadata = AmbienceEmotionClassifactionService.process_uploaded_image(
            image_file
        )

        return Response(metadata, status=HTTP_200_OK)

    def process_voice(self, request, *args, **kwargs):
        audio_file = request.FILES.get('voice')
        if not audio_file:
            return Response({"error": "No audio provided"}, status=HTTP_400_BAD_REQUEST)
        
        response = AmbienceEmotionClassifactionService.process_uploaded_voice(audio_file)
        
        return Response(response, status=HTTP_200_OK)
        