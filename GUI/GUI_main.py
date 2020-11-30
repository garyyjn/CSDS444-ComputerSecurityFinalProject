from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.textinput import TextInput
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
from VG import VG
from des import des
from RSA import xRsa
import os
Builder.load_string("""
<MenuScreen>:
    BoxLayout:
        Button:
            text: 'Encrypt'
            on_press: root.manager.current = 'encrypt'
        Button:
            text: 'Decrypt'
            on_press: root.manager.current = 'decrypt'

<EncryptScreen>:
    BoxLayout:
        orientation: 'vertical'
        Button:
            text: 'RSA'
            on_press: root.manager.current = 'en_RSA'
        Button:
            text: 'VG'
            on_press: root.manager.current = 'en_VG'
        Button:
            text: 'MD5'
            on_press: root.onClick('MD5')
        Button:
            text: 'DES'
            on_press: root.manager.current = 'en_DES'
        Button:
            text: 'Back to menu'
            on_press: root.manager.current = 'menu'

<DecryptScreen>:
    BoxLayout:
        orientation: 'vertical'
        Button:
            text: 'RSA'
            on_press: root.manager.current = 'de_RSA'
        Button:
            text: 'VG'
            on_press: root.manager.current = 'de_VG'
        Button:
            text: 'MD5'
            on_press: root.onClick('MD5')
        Button:
            text: 'DES'
            on_press: root.onClick('DES')
        Button:
            text: 'Back to menu'
            on_press: root.manager.current = 'menu'
    
<VGEncryptScreen>:
    BoxLayout:
        orientation: 'vertical'
        Button:
            text: 'load from file'
            on_press: root.show_load()
        TextInput:
            on_text: root.calculate()
            id: plane
        TextInput:
            on_text: root.calculate()
            id: key
        TextInput:
            id: cipher
        Button:
            text: 'Save into file'
            on_press: root.show_save()

<VGDecryptScreen>:
    BoxLayout:
        orientation: 'vertical'
        Button:
            text: 'load from file'
            on_press: root.show_load()
        TextInput:
            on_text: root.calculate()
            id: cipher
        TextInput:
            on_text: root.calculate()
            id: key
        TextInput:
            id: plane
        Button:
            text: 'Save into file'
            on_press: root.show_save()
            
<DESEncryptScreen>:
    BoxLayout:
        orientation: 'vertical'
        Button:
            text: 'load from file'
            on_press: root.show_load()
        TextInput:
            on_text: root.calculate()
            id: plane
        TextInput:
            id: cipher
        Button:
            text: 'Save into file'
            on_press: root.show_save()

<DESDecryptScreen>:
    BoxLayout:
        orientation: 'vertical'
        Button:
            text: 'load from file'
            on_press: root.show_load()
        TextInput:
            on_text: root.calculate()
            id: cipher
        TextInput:
            on_text: root.calculate()
            id: key
        TextInput:
            id: plane
        Button:
            text: 'Save into file'
            on_press: root.show_save()

<RSAEncryptScreen>:
    BoxLayout:
        orientation: 'vertical'
        Button:
            text: 'load from file'
            on_press: root.show_load()
        TextInput:
            on_text: root.calculate()
            id: plane
        TextInput:
            id: key
        TextInput:
            id: cipher
        Button:
            text: 'Save into file'
            on_press: root.show_save()

<RSADecryptScreen>:
    BoxLayout:
        orientation: 'vertical'
        Button:
            text: 'load from file'
            on_press: root.show_load()
        TextInput:
            on_text: root.calculate()
            id: cipher
        TextInput:
            id: public key
        TextInput:
            id: private key
        TextInput:
            id: plane
        Button:
            text: 'Save into file'
            on_press: root.show_save()

<MD5EncryptScreen>:
    BoxLayout:
        orientation: 'vertical'
        Button:
            text: 'load from file'
            on_press: root.show_load()
        TextInput:
            on_text: root.calculate()
            id: cipher
        TextInput:
            id: key
        TextInput:
            id: plane
        Button:
            text: 'Save into file'
            on_press: root.show_save()

<LoadDialog>:
    BoxLayout:
        size: root.size
        pos: root.pos
        orientation: "vertical"
        FileChooserListView:
            id: filechooser

        BoxLayout:
            size_hint_y: None
            height: 30
            Button:
                text: "Cancel"
                on_release: root.cancel()

            Button:
                text: "Load"
                on_release: root.load(filechooser.path, filechooser.selection)

<SaveDialog>:
    text_input: text_input
    BoxLayout:
        size: root.size
        pos: root.pos
        orientation: "vertical"
        FileChooserListView:
            id: filechooser
            on_selection: text_input.text = self.selection and self.selection[0] or ''

        TextInput:
            id: text_input
            size_hint_y: None
            height: 30
            multiline: False

        BoxLayout:
            size_hint_y: None
            height: 30
            Button:
                text: "Cancel"
                on_release: root.cancel()

            Button:
                text: "Save"
                on_release: root.save(filechooser.path, text_input.text)
""")

class MenuScreen(Screen):
    pass

class EncryptScreen(Screen):
    def onClick(self, algorithm):
        if(algorithm == 'RSA'):
            print("running rsa")
        elif(algorithm == 'VG'):
            pass
        elif(algorithm == 'MD5'):
            pass
        elif(algorithm == 'DES'):
            pass
    pass

class DecryptScreen(Screen):
    def onClick(self, algorithm):
        if(algorithm == 'RSA'):
            pass
        elif(algorithm == 'VG'):
            pass
        elif(algorithm == 'MD5'):
            pass
        elif(algorithm == 'DES'):
            pass
    pass
'''
VG encryption/decryption algorithm screens
'''
class VGEncryptScreen(Screen):
    def calculate(self):
        algo = VG()
        plane_text = self.ids.plane.text
        key = self.ids.key.text
        if(key != ''):
            algo.create_table(key)
            ciper_text = algo.cipher(plane_text,key)
            self.ids.cipher.text = ciper_text
        else:
            self.ids.cipher.text = plane_text

    loadfile = ObjectProperty(None)
    savefile = ObjectProperty(None)
    text_input = ObjectProperty(None)

    def dismiss_popup(self):
        self._popup.dismiss()

    def show_load(self):
        content = LoadDialog(load=self.load, cancel=self.dismiss_popup)
        self._popup = Popup(title="Load file", content=content,
                            size_hint=(0.9, 0.9))
        self._popup.open()

    def show_save(self):
        content = SaveDialog(save=self.save, cancel=self.dismiss_popup)
        self._popup = Popup(title="Save file", content=content,
                            size_hint=(0.9, 0.9))
        self._popup.open()

    def load(self, path, filename):
        with open(os.path.join(path, filename[0])) as stream:
            self.ids.plane.text = stream.read()

        self.dismiss_popup()

    def save(self, path, filename):
        with open(os.path.join(path, filename), 'w') as stream:
            stream.write(self.ids.cipher.text)
        self.dismiss_popup()
    pass


class VGDecryptScreen(Screen):
    def calculate(self):
        algo = VG()
        cipher_text = self.ids.cipher.text
        key = self.ids.key.text
        if (key != ''):
            algo.create_table(key)
            plane_text = algo.decipher(cipher_text, key)
            self.ids.plane.text = plane_text
        else:
            self.ids.cipher.text = cipher_text

    loadfile = ObjectProperty(None)
    savefile = ObjectProperty(None)
    text_input = ObjectProperty(None)

    def dismiss_popup(self):
        self._popup.dismiss()

    def show_load(self):
        content = LoadDialog(load=self.load, cancel=self.dismiss_popup)
        self._popup = Popup(title="Load file", content=content,
                            size_hint=(0.9, 0.9))
        self._popup.open()

    def show_save(self):
        content = SaveDialog(save=self.save, cancel=self.dismiss_popup)
        self._popup = Popup(title="Save file", content=content,
                            size_hint=(0.9, 0.9))
        self._popup.open()

    def load(self, path, filename):
        with open(os.path.join(path, filename[0])) as stream:
            self.ids.cipher.text = stream.read()

        self.dismiss_popup()

    def save(self, path, filename):
        with open(os.path.join(path, filename), 'w') as stream:
            stream.write(self.ids.plane.text)
        self.dismiss_popup()

    pass
'''
DES encryption/decryption
'''
class DESEncryptScreen(Screen):
    def calculate(self):
        algo = des()
        file = 'en_des_input.txt'
        f = open(file, 'r+')
        f.truncate(0)
        plane_text = self.ids.plane.text
        f.write(plane_text)
        key_file = '../key.txt'
        algo.encryption(keyPath=key_file,filename=file)
        o = open('en_des_input(txt).des')
        self.ids.cipher.text = o.read()

    loadfile = ObjectProperty(None)
    savefile = ObjectProperty(None)
    text_input = ObjectProperty(None)

    def dismiss_popup(self):
        self._popup.dismiss()

    def show_load(self):
        content = LoadDialog(load=self.load, cancel=self.dismiss_popup)
        self._popup = Popup(title="Load file", content=content,
                            size_hint=(0.9, 0.9))
        self._popup.open()

    def show_save(self):
        content = SaveDialog(save=self.save, cancel=self.dismiss_popup)
        self._popup = Popup(title="Save file", content=content,
                            size_hint=(0.9, 0.9))
        self._popup.open()

    def load(self, path, filename):
        with open(os.path.join(path, filename[0])) as stream:
            self.ids.plane.text = stream.read()
        self.dismiss_popup()

    def save(self, path, filename):
        with open(os.path.join(path, filename), 'w') as stream:
            stream.write(self.ids.cipher.text)
        self.dismiss_popup()
    pass
'''
md5 encryption
'''
'''
RSA encryption
'''
class RSAEncryptScreen(Screen):
    def calculate(self):
        algo = xRsa()
        plane_text = self.ids.plane.text
        cipher, private, public = algo.encrptyMsg(plane_text)
        self.ids.key.text = "public key: " + str(public) + "\nprivate key:" + str(private)
        self.ids.cipher.text = str(cipher)

    loadfile = ObjectProperty(None)
    savefile = ObjectProperty(None)
    text_input = ObjectProperty(None)

    def dismiss_popup(self):
        self._popup.dismiss()

    def show_load(self):
        content = LoadDialog(load=self.load, cancel=self.dismiss_popup)
        self._popup = Popup(title="Load file", content=content,
                            size_hint=(0.9, 0.9))
        self._popup.open()

    def show_save(self):
        content = SaveDialog(save=self.save, cancel=self.dismiss_popup)
        self._popup = Popup(title="Save file", content=content,
                            size_hint=(0.9, 0.9))
        self._popup.open()

    def load(self, path, filename):
        with open(os.path.join(path, filename[0])) as stream:
            self.ids.plane.text = stream.read()
        self.dismiss_popup()

    def save(self, path, filename):
        with open(os.path.join(path, filename), 'w') as stream:
            stream.write(self.ids.cipher.text)
        self.dismiss_popup()

    pass

class RSADecryptScreen(Screen):
    def calculate(self):
        algo = xRsa()
        try:
            cipher = int(self.ids.cipher.text)
            private_key = int(self.ids.private_key.text)
            public_key = int(self.ids.public_key.text)
        except:
            self.ids.plane.text = "numeric input only"
        try:
            plane = algo.decrptyMsg(cipher,private_key, public_key)
            self.ids.plane.text = plane
        except:
            self.ids.plane.text = "Invalid key/cipher"

    loadfile = ObjectProperty(None)
    savefile = ObjectProperty(None)
    text_input = ObjectProperty(None)

    def dismiss_popup(self):
        self._popup.dismiss()

    def show_load(self):
        content = LoadDialog(load=self.load, cancel=self.dismiss_popup)
        self._popup = Popup(title="Load file", content=content,
                            size_hint=(0.9, 0.9))
        self._popup.open()

    def show_save(self):
        content = SaveDialog(save=self.save, cancel=self.dismiss_popup)
        self._popup = Popup(title="Save file", content=content,
                            size_hint=(0.9, 0.9))
        self._popup.open()

    def load(self, path, filename):
        with open(os.path.join(path, filename[0])) as stream:
            self.ids.cipher.text = stream.read()
        self.dismiss_popup()

    def save(self, path, filename):
        with open(os.path.join(path, filename), 'w') as stream:
            stream.write(self.ids.plane.text)
        self.dismiss_popup()

    pass
'''
Input/Output
'''
class LoadDialog(FloatLayout):
    load = ObjectProperty(None)
    cancel = ObjectProperty(None)


class SaveDialog(FloatLayout):
    save = ObjectProperty(None)
    text_input = ObjectProperty(None)
    cancel = ObjectProperty(None)

# Create the screen manager
sm = ScreenManager()
sm.add_widget(MenuScreen(name='menu'))
sm.add_widget(EncryptScreen(name='encrypt'))
sm.add_widget(DecryptScreen(name='decrypt'))
sm.add_widget(VGEncryptScreen(name='en_VG'))
sm.add_widget(VGDecryptScreen(name='de_VG'))
sm.add_widget(DESEncryptScreen(name='en_DES'))
sm.add_widget(RSAEncryptScreen(name='en_RSA'))
sm.add_widget(RSADecryptScreen(name='de_RSA'))


class TestApp(App):

    def build(self):
        return sm

if __name__ == '__main__':
    TestApp().run()