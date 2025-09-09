import io
import tempfile
from django.test import TestCase
from rest_framework.test import APIClient
from PIL import Image
import wave
import numpy as np

class AmbienceEmotionTests(TestCase):
    def setUp(self):
        self.client = APIClient()

    def _create_test_image(self):
        image = Image.new("RGB", (100, 100), color="white")
        tmp = tempfile.NamedTemporaryFile(suffix=".jpg", delete=False)
        image.save(tmp, format="JPEG")
        tmp.seek(0)
        return tmp

    def _create_test_audio(self):
       
        tmp = tempfile.NamedTemporaryFile(suffix=".wav", delete=False)
        with wave.open(tmp, "w") as wf:
            wf.setnchannels(1)
            wf.setsampwidth(2)
            wf.setframerate(16000)
            samples = np.zeros(16000, dtype=np.int16)  
            wf.writeframes(samples.tobytes())
        tmp.seek(0)
        return tmp

    def test_upload_image(self):
        image_file = self._create_test_image()
        with open(image_file.name, "rb") as f:
            response = self.client.post(
                "/api/emotion-classification/ambience/process_image/", {"image": f}, format="multipart"
            )
        self.assertEqual(response.status_code, 200)
        self.assertIn("e67d288bc38db3a940c17b8c8a2c1acf", response.data) 

    def test_upload_voice(self):
        audio_file = self._create_test_audio()
        with open(audio_file.name, "rb") as f:
            response = self.client.post(
                "/api/emotion-classification/ambience/process_voice/", {"voice": f}, format="multipart"
            )
        self.assertEqual(response.status_code, 200)
