from django.urls import path
from .viewsets.text_emotion_classification_viewset import (
    TextEmotionClassificationView,
    BatchTextEmotionClassificationView,
)

urlpatterns = [
    path("emotion-classification/text/", TextEmotionClassificationView.as_view()),
    path(
        "emotion-classification/text/batch/",
        BatchTextEmotionClassificationView.as_view(),
    ),
]
