from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class CalculatorApp(App):
    def build(self):
        self.title = "Test Calculator"
        self.root_layout = BoxLayout(orientation="vertical", padding=10, spacing=10)
        
        # Display Screen
        self.solution = TextInput(
            font_size=32, readonly=True, halign="right", 
            multiline=False, size_hint=(1, 0.2)
        )
        self.root_layout.add_widget(self.solution)
        
        # Keypad Grid Layout
        buttons = [
            ["7", "8", "9", "/"],
            ["4", "5", "6", "*"],
            ["1", "2", "3", "-"],
            [".", "0", "C", "+"]
        ]
        
        for row in buttons:
            h_layout = BoxLayout(spacing=10)
            for label in row:
                btn = Button(
                    text=label, font_size=24,
                    background_color=(0.1, 0.4, 0.7, 1)
                )
                btn.bind(on_press=self.on_button_press)
                h_layout.add_widget(btn)
            self.root_layout.add_widget(h_layout)
            
        # Equal Button
        equals_btn = Button(
            text="=", font_size=24, size_hint=(1, 0.15),
            background_color=(0.2, 0.7, 0.3, 1)
        )
        equals_btn.bind(on_press=self.on_solution)
        self.root_layout.add_widget(equals_btn)
        
        return self.root_layout

    def on_button_press(self, instance):
        current = self.solution.text
        button_text = instance.text
        
        if button_text == "C":
            self.solution.text = ""
        else:
            if current and (self.last_was_operator and button_text in ["/", "*", "-", "+"]):
                return
            elif current == "" and button_text in ["/", "*", "+"]:
                return
            else:
                self.solution.text = current + button_text
                
        self.last_was_operator = button_text in ["/", "*", "-", "+"]

    def on_solution(self, instance):
        text = self.solution.text
        try:
            # Safe evaluation for basic math
            result = str(eval(text))
            self.solution.text = result
        except Exception:
            self.solution.text = "Error"

if __name__ == "__main__":
    CalculatorApp().run()