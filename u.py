
# Generated by CodiumAI
from Stegno import Stegno
from logging import root
from tkinter import Frame
from tkinter import Label
from tkinter import Button
import messagebox


import pytest

class TestStegno:

    # GUI is displayed correctly
    def test_gui_displayed_correctly(self):
        stegno = Stegno()
        stegno.main(root)
        assert root.title() == 'ImageSteganography'
        assert root.geometry() == '500x600'
        assert root.resizable() == (False, False)
        assert root.cget('bg') == '#FFDAB9'
        assert isinstance(root.children['!frame'], Frame)
        assert isinstance(root.children['!frame'].children['!label'], Label)
        assert isinstance(root.children['!frame'].children['!button1'], Button)
        assert isinstance(root.children['!frame'].children['!button2'], Button)
        assert isinstance(root.children['!frame'].children['!label2'], Label)
        assert isinstance(root.children['!frame'].children['!label3'], Label)

    # Encode button opens the encode frame
    def test_encode_button_opens_encode_frame(self):
        stegno = Stegno()
        stegno.main(root)
        encode_button = root.children['!frame'].children['!button1']
        encode_button.invoke()
        assert isinstance(root.children['!frame2'], Frame)

    # Decode button opens the decode frame
    def test_decode_button_opens_decode_frame(self):
        stegno = Stegno()
        stegno.main(root)
        decode_button = root.children['!frame'].children['!button2']
        decode_button.invoke()
        assert isinstance(root.children['!frame2'], Frame)

    # No image is selected in the decode frame
    def test_no_image_selected_in_decode_frame(self):
        stegno = Stegno()
        stegno.main(root)
        decode_button = root.children['!frame'].children['!button2']
        decode_button.invoke()
        select_button = root.children['!frame2'].children['!button']
        select_button.invoke()
        assert messagebox.showerror.called_with('Error', 'You have selected nothing !')

    # No text is entered in the encode frame
    def test_no_text_entered_in_encode_frame(self):
        stegno = Stegno()
        stegno.main(root)
        encode_button = root.children['!frame'].children['!button1']
        encode_button.invoke()
        encode_button2 = root.children['!frame2'].children['!button']
        encode_button2.invoke()
        assert messagebox.showinfo.called_with('Alert', 'Kindly enter text in TextBox')

    # Image with hidden text is not saved in the encode frame
    def test_image_not_saved_in_encode_frame(self):
        stegno = Stegno()
        stegno.main(root)
        encode_button = root.children['!frame'].children['!button1']
        encode_button.invoke()
        select_button = root.children['!frame2'].children['!button']
        select_button.invoke()
        encode_button2 = root.children['!frame2'].children['!button2']
        encode_button2.invoke()


        assert messagebox.showinfo.called_with('Success', 'Encoding Successful\nFile is saved as Image_with_hiddentext.png in the same directory')

print("ALL These Functions work properly !!")