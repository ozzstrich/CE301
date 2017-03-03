from kivy.app import App
from kivy.uix.scatter import Scatter
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
import random

class ScatterTextWidget(BoxLayout):
    def change_label_colour(self, *args):
        colour = [random.random() for i in xrange(3)] + [1]
        label = self.ids['my_label']
        label.color = colour

        label1 = self.ids.label1
        label2 = self.ids.label2

        label1.color = colour
        label2.color = colour

class TutorialApp(App):
    def build(self):
        return ScatterTextWidget()


if __name__ == "__main__":
    TutorialApp().run()

# Original scatter text widget in python
# b = BoxLayout(orientation='vertical')
# l = Label(text="hi",
#           font_size=30)
# t = TextInput(font_size=30,
#               size_hint_y=None,
#               height=50,
#               text='hi')
# f = FloatLayout()
# s = Scatter()
#
#
# t.bind(text=l.setter('text'))
#
# f.add_widget(s)
# s.add_widget(l)
# b.add_widget(f)
# b.add_widget(t)
