"""
Unit tests for the Emotion Detection module.
"""
import unittest
from EmotionDetection.emotion_detection import emotion_detector

class TestEmotionDetection(unittest.TestCase):
    """
    Test cases for emotion_detector function.
    """

    def test_emotion_joy(self):
        """
        Test that the emotion_detector correctly identifies joy.
        """
        result = emotion_detector("I am glad this happened")
        self.assertEqual(result['dominant_emotion'], 'joy')

    def test_emotion_anger(self):
        """
        Test that the emotion_detector correctly identifies anger.
        """
        result = emotion_detector("I am really mad about this")
        self.assertEqual(result['dominant_emotion'], 'anger')

    def test_emotion_disgust(self):
        """
        Test that the emotion_detector correctly identifies disgust.
        """
        result = emotion_detector("I feel disgusted just hearing about this")
        self.assertEqual(result['dominant_emotion'], 'disgust')

    def test_emotion_sadness(self):
        """
        Test that the emotion_detector correctly identifies sadness.
        """
        result = emotion_detector("I am so sad about this")
        self.assertEqual(result['dominant_emotion'], 'sadness')

    def test_emotion_fear(self):
        """
        Test that the emotion_detector correctly identifies fear.
        """
        result = emotion_detector("I am really afraid that this will happen")
        self.assertEqual(result['dominant_emotion'], 'fear')

if __name__ == '__main__':
    unittest.main()