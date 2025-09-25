import os
from django.apps import AppConfig


class EmotionAnalysisConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "emotion_classifier"

    def ready(self):
        parent_dir = os.path.join(os.path.dirname(__file__), "dl_models")
        self.bert_dir = os.path.join(parent_dir, "bert_text_emotion_classifier")
        self.bert_dir_v2 = os.path.join(parent_dir, "bert_text_emotion_classifier_v2")
