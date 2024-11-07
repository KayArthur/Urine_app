from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.clock import Clock

# Dictionary for urine color health insights and recommended water intake
urine_color_info = {
    'clear': {'meaning': 'Well hydrated, but too much water.', 'risk': 'Overhydration can dilute essential salts.', 'water_needed': 0.5},
    'pale yellow': {'meaning': 'Healthy color, proper hydration.', 'risk': 'No risks, you’re doing well!', 'water_needed': 0.3},
    'dark yellow': {'meaning': 'Slightly dehydrated.', 'risk': 'May lead to dehydration.', 'water_needed': 1.0},
    'amber': {'meaning': 'Dehydrated, need water.', 'risk': 'Dehydration can affect kidney function.', 'water_needed': 1.5},
    'brown': {'meaning': 'Severe dehydration or liver issues.', 'risk': 'Seek medical advice.', 'water_needed': 2.0},
    'pink/red': {'meaning': 'Blood in urine, possible infection.', 'risk': 'See a doctor immediately.', 'water_needed': 1.5}
}

class UrineApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical')

        self.label = Label(text='Enter the color of your urine:')
        self.layout.add_widget(self.label)

        self.color_input = TextInput(multiline=False)
        self.layout.add_widget(self.color_input)

        self.submit_button = Button(text='Submit', on_press=self.analyze_color)
        self.layout.add_widget(self.submit_button)

        self.result_label = Label(text='')
        self.layout.add_widget(self.result_label)

        self.water_label = Label(text='')
        self.layout.add_widget(self.water_label)

        return self.layout

    def analyze_color(self, instance):
        color = self.color_input.text.lower()
        info = urine_color_info.get(color, {'meaning': 'Unknown color', 'risk': 'Consult a doctor', 'water_needed': 1.0})
        self.result_label.text = f"Meaning: {info['meaning']}\nRisks: {info['risk']}"
        self.water_label.text = f"Recommended Water Intake: {info['water_needed']} liters"

# Run the app
if __name__ == "__main__":
    UrineApp().run()
