from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.properties import StringProperty

__author__ = 'Alan Wilson'

MILES_TO_KM_CONVERSION_FACTOR = 1.60934


class ConvertMilesKmApp(App):
    """ConvertMilesKmApp is a Kivy App for distance unit conversions"""
    kilometers = StringProperty("0.0")

    def build(self):
        """Build the Kivy app"""
        Window.size = (600, 200)
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_conversion(self):
        """Convert the miles input into kilometers using conversion factor"""
        try:
            miles = float(self.root.ids.input_number.text)
            self.kilometers = str(miles * MILES_TO_KM_CONVERSION_FACTOR)
        except ValueError:
            self.kilometers = "0.0"

    def increment_input(self, delta):
        """Increment or decrement the miles input"""
        try:
            current_value = float(self.root.ids.input_number.text)
        except ValueError:
            current_value = 0.0

        new_value = current_value + delta
        self.root.ids.input_number.text = str(new_value)


ConvertMilesKmApp().run()
