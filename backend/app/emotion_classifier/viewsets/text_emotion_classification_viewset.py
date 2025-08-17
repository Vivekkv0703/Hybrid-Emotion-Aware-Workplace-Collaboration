from rest_framework.views import APIView
from rest_framework.response import Response
from django.apps import apps
import tensorflow as tf


class TextEmotionClassificationView(APIView):
    def post(self, request, *args, **kwargs):
        model = request.query_params.get("model")
        text = request.data.get("text")

        if not text:
            return Response({"error": "No text provided"}, status=400)

        emotion_classifier_config = apps.get_app_config("emotion_classifier")

        if model == "v1":
            tokenizer, model = (
                emotion_classifier_config.bert_tokenizer,
                emotion_classifier_config.bert_model,
            )
        else:
            tokenizer, model = (
                emotion_classifier_config.bert_tokenizer_v2,
                emotion_classifier_config.bert_model_v2,
            )

        inputs = tokenizer(
            text, return_tensors="tf", truncation=True, padding=True, max_length=128
        )
        outputs = model(**inputs)
        probs = tf.nn.softmax(outputs.logits, axis=-1).numpy()[0]

        mapped_probs = list(
            zip(
                [
                    "anger",
                    "boredom",
                    "empty",
                    "enthusiasm",
                    "fun",
                    "happiness",
                    "hate",
                    "love",
                    "neutral",
                    "relief",
                    "sadness",
                    "surprise",
                    "worry",
                ],
                probs,
            )
        )

        top_emotion = max(mapped_probs, key=lambda a: a[1])

        return Response(
            {
                "top_emotion": {
                    "label": top_emotion[0],
                    "probability": float(top_emotion[1]),
                },
                "all_emotions": [
                    {"label": label, "probability": float(probability)}
                    for label, probability in mapped_probs
                ],
            }
        )


class BatchTextEmotionClassificationView(APIView):
    def post(self, request, *args, **kwargs):
        model = request.query_params.get("model")
        texts = request.data.get("texts")

        if len(texts) == 0:
            return Response({"error": "No text provided"}, status=400)

        emotion_classifier_config = apps.get_app_config("emotion_classifier")

        if model == "v1":
            tokenizer, model = (
                emotion_classifier_config.bert_tokenizer,
                emotion_classifier_config.bert_model,
            )
        else:
            tokenizer, model = (
                emotion_classifier_config.bert_tokenizer_v2,
                emotion_classifier_config.bert_model_v2,
            )

        results = []
        for text in texts:
            inputs = tokenizer(
                text, return_tensors="tf", truncation=True, padding=True, max_length=128
            )
            outputs = model(**inputs)
            probs = tf.nn.softmax(outputs.logits, axis=-1).numpy()[0]

            mapped_probs = list(
                zip(
                    [
                        "anger",
                        "boredom",
                        "empty",
                        "enthusiasm",
                        "fun",
                        "happiness",
                        "hate",
                        "love",
                        "neutral",
                        "relief",
                        "sadness",
                        "surprise",
                        "worry",
                    ],
                    probs,
                )
            )

            top_emotion = max(mapped_probs, key=lambda a: a[1])

            results.append(
                {
                    "text": text,
                    "top_emotion": {
                        "label": top_emotion[0],
                        "probability": float(top_emotion[1]),
                    },
                    "all_emotions": [
                        {"label": label, "probability": float(probability)}
                        for label, probability in mapped_probs
                    ],
                }
            )

        return Response({"data": results})
