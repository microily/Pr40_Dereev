from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.pickers import MDTimePicker

# Описание интерфейса в формате Kivy
kv = '''
<MyApp>:
    MDRaisedButton:
        text: "Выбрать время"
        pos_hint: {'center_x': 0.5, 'center_y': 0.6}
        on_release: app.show_time_picker()
    MDLabel:
        id: time_label
        text: "Выбранное время: "
        pos_hint: {'center_x': 0.5, 'center_y': 0.4}
'''

class MyApp(MDApp):
    def build(self):
        return Builder.load_string(kv)

    def show_time_picker(self):
        time_dialog = MDTimePicker()
        time_dialog.bind(time=self.set_time)
        time_dialog.open()

    def set_time(self, instance, time):
        self.root.ids.time_label.text = "Выбранное время: " + str(time)

if __name__ == "__main__":
    MyApp().run()
