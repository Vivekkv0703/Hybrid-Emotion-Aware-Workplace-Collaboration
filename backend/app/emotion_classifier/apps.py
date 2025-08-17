import os
from django.apps import AppConfig
from transformers import TFAutoModelForSequenceClassification, AutoTokenizer


class EmotionAnalysisConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "emotion_classifier"

    def ready(self):
        parent_dir = os.path.join(os.path.dirname(__file__), "dl_models")
        bert_dir = os.path.join(parent_dir, "bert_text_emotion_classifier")
        bert_dir_v2 = os.path.join(parent_dir, "bert_text_emotion_classifier_v2")

        self.bert_model = TFAutoModelForSequenceClassification.from_pretrained(
            bert_dir, local_files_only=True
        )
        self.bert_tokenizer = AutoTokenizer.from_pretrained(
            bert_dir, local_files_only=True
        )

        self.bert_model_v2 = TFAutoModelForSequenceClassification.from_pretrained(
            bert_dir_v2, local_files_only=True
        )
        self.bert_tokenizer_v2 = AutoTokenizer.from_pretrained(
            bert_dir_v2, local_files_only=True
        )
