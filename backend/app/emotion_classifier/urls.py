from django.urls import path
from .viewsets.text_emotion_classification_viewset import (
    TextEmotionClassificationView,
    BatchTextEmotionClassificationView,
)

urlpatterns = [
    path("text/", TextEmotionClassificationView.as_view()),
    path(
        "text/batch/",
        BatchTextEmotionClassificationView.as_view(),
    ),
]
