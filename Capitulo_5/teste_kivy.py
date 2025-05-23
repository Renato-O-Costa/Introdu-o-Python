from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

class MyApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')

        self.label = Label(text="Olá, Kivy!", font_size=24)
        btn = Button(text="Clique Aqui", size_hint=(1, 0.2))
        btn.bind(on_press=self.on_button_click)

        layout.add_widget(self.label)
        layout.add_widget(btn)

        return layout

    def on_button_click(self, instance):
        self.label.text = "Botão pressionado!"

if __name__ == '__main__':
    MyApp().run()
