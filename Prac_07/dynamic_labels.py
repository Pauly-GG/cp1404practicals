from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.properties import StringProperty


class DynamicLabelsApp(App):
    """Main program - Kivy app to demo dynamic widget creation."""
    status_text = StringProperty()

    def __init__(self, **kwargs):
        """Construct main app."""
        super().__init__(**kwargs)
        self.list_of_names = ["Paul", "Monkey", "Jeff", "Pepega", "Peepo"]

    def build(self):
        self.title = "Dynamic Widgets"
        self.root = Builder.load_file('dynamic_widgets.kv')
        self.create_widgets()
        return self.root

    def create_widgets(self):
        for name in self.list_of_names:
            temp_label = Label(text=name)
            self.root.ids.entries_box.add_widget(temp_label)


DynamicLabelsApp().run()
