from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label


class DynamicLabelsApp(App):
    """Kivy app to dynamically create labels"""

    def __init__(self, **kwargs):
        """Construct main app."""
        super().__init__(**kwargs)
        self.names = ["Ben", "Liam", "Joel", "David", "John", "Darcy", "Hunter"]

    def build(self):
        """Build the Kivy GUI"""
        self.title = "Dynamic Labels"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.create_labels()
        return self.root

    def create_labels(self):
        """Create labels from data and add them to the GUI"""
        for name in self.names:
            new_label = Label(text=name, size_hint_y=None, height=40)  # Adjust height if needed
            self.root.ids.main.add_widget(new_label)


if __name__ == '__main__':
    DynamicLabelsApp().run()
