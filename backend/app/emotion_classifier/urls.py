from django.urls import path
from .viewsets.text_emotion_classification_viewset import (
    TextEmotionClassificationView,
    BatchTextEmotionClassificationView,
)
from .viewsets.ambience_emotion_classification_viewset import (
    AmbienceEmotionClassificationViewset,
)
from .viewsets.frame_emotion_classification_viewset import FrameEmotionClassificationView

urlpatterns = [
    path("text/", TextEmotionClassificationView.as_view()),
    path(
        "text/batch/",
        BatchTextEmotionClassificationView.as_view(),
    ),
    path(
        "ambience/process_image/",
        AmbienceEmotionClassificationViewset.as_view({"post": "process_image"}),
    ),
    path(
        "ambience/process_voice/",
        AmbienceEmotionClassificationViewset.as_view({"post": "process_voice"}),
    ),
    path("frame/", FrameEmotionClassificationView.as_view({"post": "post"}))
]
