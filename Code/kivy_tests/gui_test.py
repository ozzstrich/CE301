import kivy
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.base import runTouchApp
from kivy.lang import Builder
from kivy.properties import StringProperty

# Builder.load_string('''
# <ScrollableLabel>:
#     text: str('Fake news and dank memes' * 50)
#     Label:
#         text: root.my_any()
#         font_size: 50
#         text_size: self.width, None
#         size_hint_y: None
#         height: self.texture_size[1]
# ''')

Builder.load_string('''
<ScrollableLabel>:
    canvas:
        Color:
            rgb: 55, 55, 55

    Label:
        text: root.my_any() * 60
        font_size: 60
        text_size: self.width, None
        size_hint_y: None
        height: self.texture_size[1]
''')


class ScrollableLabel(ScrollView):
    def my_any(self):
        print ('in my_any')
        w = 'this is a string'
        return w


runTouchApp(ScrollableLabel())
