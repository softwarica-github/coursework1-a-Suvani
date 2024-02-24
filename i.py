import unittest
from unittest.mock import MagicMock
from tkinter import Tk
from Stegno import Stegno

class TestStegnoIntegration(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.root = Tk()
        cls.app = Stegno()

    @classmethod
    def tearDownClass(cls):
        cls.root.destroy()  # Destroy the Tkinter application after all tests are done

    def test_encode_decode_integration(self):
        mock_frame = MagicMock()  # Mocking the frame object
        self.app.main(self.root)  # Start the application
        self.app.frame1_encode(mock_frame)  # Simulate button click to go to encoding frame
        # You may need to simulate selecting an image and entering text into the text area
        # Simulate clicking the encode button
        # Assert that encoding completes without raising any errors

        # Simulate decoding
        mock_frame = MagicMock()  # Mocking the frame object
        self.app.frame1_decode(mock_frame)  # Simulate button click to go to decoding frame
        # You may need to simulate selecting an image for decoding
        # Assert that decoding completes without raising any errors

if __name__ == '__main__':
    unittest.main()
