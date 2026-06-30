# Kivy UI Implementation for Math King Calculator
# This file provides the mobile app interface using Kivy framework

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.tabbedpanel import TabbedPanel, TabbedPanelItem
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.image import Image
from kivy.core.window import Window
from kivy.garden.matplotlib.backend_kivyagg import FigureCanvasKivyAgg
import matplotlib.pyplot as plt

from calculator import MathKingCalculator
from todo_app import TodoList

# Set window size
Window.size = (400, 700)


class MathKingApp(App):
    """Main Kivy application for Math King Calculator + To-Do List"""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.calculator = MathKingCalculator()
        self.todo_list = TodoList()

    def build(self):
        """Build the main UI"""
        # Main container
        main_layout = BoxLayout(orientation='vertical')

        # Title
        title = Label(
            text='🧮 Math King Calculator + 📝 To-Do List',
            size_hint_y=0.08,
            font_size='18sp'
        )
        main_layout.add_widget(title)

        # Tabbed Panel
        tab_panel = TabbedPanel(size_hint_y=0.92)

        # Tab 1: Calculator
        calc_tab = TabbedPanelItem(text='Calculator')
        calc_tab.content = self.create_calculator_tab()
        tab_panel.add_widget(calc_tab)

        # Tab 2: To-Do List
        todo_tab = TabbedPanelItem(text='To-Do List')
        todo_tab.content = self.create_todo_tab()
        tab_panel.add_widget(todo_tab)

        main_layout.add_widget(tab_panel)
        return main_layout

    def create_calculator_tab(self):
        """Create calculator tab UI"""
        layout = BoxLayout(orientation='vertical', padding=10, spacing=5)

        # Input field
        self.calc_input = TextInput(
            multiline=False,
            size_hint_y=0.1,
            hint_text='Enter calculation...',
            font_size='16sp'
        )
        layout.add_widget(self.calc_input)

        # Result display
        self.calc_result = Label(
            text='Result: ',
            size_hint_y=0.1,
            font_size='18sp'
        )
        layout.add_widget(self.calc_result)

        # Buttons grid
        buttons_grid = GridLayout(cols=3, spacing=5, size_hint_y=0.6)

        # Calculator buttons
        calc_buttons = [
            ('Add', self.on_calc_add),
            ('Subtract', self.on_calc_subtract),
            ('Multiply', self.on_calc_multiply),
            ('Divide', self.on_calc_divide),
            ('Power', self.on_calc_power),
            ('Sqrt', self.on_calc_sqrt),
            ('Sin', self.on_calc_sin),
            ('Cos', self.on_calc_cos),
            ('Tan', self.on_calc_tan),
            ('Log10', self.on_calc_log10),
            ('Factorial', self.on_calc_factorial),
            ('Clear', self.on_calc_clear),
        ]

        for btn_text, btn_callback in calc_buttons:
            btn = Button(text=btn_text)
            btn.bind(on_press=btn_callback)
            buttons_grid.add_widget(btn)

        layout.add_widget(buttons_grid)
        return layout

    def create_todo_tab(self):
        """Create to-do list tab UI"""
        layout = BoxLayout(orientation='vertical', padding=10, spacing=5)

        # Input section
        input_layout = BoxLayout(size_hint_y=0.15, spacing=5)
        self.todo_input = TextInput(
            multiline=False,
            hint_text='Add new task...',
            size_hint_x=0.7
        )
        add_btn = Button(text='Add', size_hint_x=0.3)
        add_btn.bind(on_press=self.on_todo_add)
        input_layout.add_widget(self.todo_input)
        input_layout.add_widget(add_btn)
        layout.add_widget(input_layout)

        # Tasks display
        self.todo_list_display = Label(
            text='No tasks yet',
            size_hint_y=0.7,
            markup=True
        )
        scroll_view = ScrollView()
        scroll_view.add_widget(self.todo_list_display)
        layout.add_widget(scroll_view)

        # Action buttons
        buttons_layout = GridLayout(cols=3, spacing=5, size_hint_y=0.15)

        action_buttons = [
            ('Refresh', self.on_todo_refresh),
            ('Stats', self.on_todo_stats),
            ('Clear Done', self.on_todo_clear),
        ]

        for btn_text, btn_callback in action_buttons:
            btn = Button(text=btn_text)
            btn.bind(on_press=btn_callback)
            buttons_layout.add_widget(btn)

        layout.add_widget(buttons_layout)
        return layout

    # Calculator callbacks
    def on_calc_add(self, instance):
        try:
            values = self.calc_input.text.split(',')
            if len(values) >= 2:
                result = self.calculator.add(float(values[0]), float(values[1]))
                self.calc_result.text = f'Result: {result}'
            else:
                self.calc_result.text = 'Enter two values separated by comma'
        except Exception as e:
            self.calc_result.text = f'Error: {str(e)}'

    def on_calc_subtract(self, instance):
        try:
            values = self.calc_input.text.split(',')
            if len(values) >= 2:
                result = self.calculator.subtract(float(values[0]), float(values[1]))
                self.calc_result.text = f'Result: {result}'
        except Exception as e:
            self.calc_result.text = f'Error: {str(e)}'

    def on_calc_multiply(self, instance):
        try:
            values = self.calc_input.text.split(',')
            if len(values) >= 2:
                result = self.calculator.multiply(float(values[0]), float(values[1]))
                self.calc_result.text = f'Result: {result}'
        except Exception as e:
            self.calc_result.text = f'Error: {str(e)}'

    def on_calc_divide(self, instance):
        try:
            values = self.calc_input.text.split(',')
            if len(values) >= 2:
                result = self.calculator.divide(float(values[0]), float(values[1]))
                self.calc_result.text = f'Result: {result}'
        except Exception as e:
            self.calc_result.text = f'Error: {str(e)}'

    def on_calc_power(self, instance):
        try:
            values = self.calc_input.text.split(',')
            if len(values) >= 2:
                result = self.calculator.power(float(values[0]), float(values[1]))
                self.calc_result.text = f'Result: {result}'
        except Exception as e:
            self.calc_result.text = f'Error: {str(e)}'

    def on_calc_sqrt(self, instance):
        try:
            result = self.calculator.sqrt(float(self.calc_input.text))
            self.calc_result.text = f'Result: {result}'
        except Exception as e:
            self.calc_result.text = f'Error: {str(e)}'

    def on_calc_sin(self, instance):
        try:
            result = self.calculator.sin(float(self.calc_input.text))
            self.calc_result.text = f'Result: {result}'
        except Exception as e:
            self.calc_result.text = f'Error: {str(e)}'

    def on_calc_cos(self, instance):
        try:
            result = self.calculator.cos(float(self.calc_input.text))
            self.calc_result.text = f'Result: {result}'
        except Exception as e:
            self.calc_result.text = f'Error: {str(e)}'

    def on_calc_tan(self, instance):
        try:
            result = self.calculator.tan(float(self.calc_input.text))
            self.calc_result.text = f'Result: {result}'
        except Exception as e:
            self.calc_result.text = f'Error: {str(e)}'

    def on_calc_log10(self, instance):
        try:
            result = self.calculator.log10(float(self.calc_input.text))
            self.calc_result.text = f'Result: {result}'
        except Exception as e:
            self.calc_result.text = f'Error: {str(e)}'

    def on_calc_factorial(self, instance):
        try:
            result = self.calculator.factorial(int(float(self.calc_input.text)))
            self.calc_result.text = f'Result: {result}'
        except Exception as e:
            self.calc_result.text = f'Error: {str(e)}'

    def on_calc_clear(self, instance):
        self.calc_input.text = ''
        self.calc_result.text = 'Result: '

    # To-Do callbacks
    def on_todo_add(self, instance):
        if self.todo_input.text.strip():
            try:
                self.todo_list.add_task(self.todo_input.text)
                self.todo_input.text = ''
                self.on_todo_refresh(None)
            except Exception as e:
                self.todo_list_display.text = f'Error: {str(e)}'

    def on_todo_refresh(self, instance):
        tasks = self.todo_list.get_pending_tasks()
        if not tasks:
            self.todo_list_display.text = 'No pending tasks'
        else:
            text = '📝 Pending Tasks:\\n\\n'
            for i, task in enumerate(tasks, 1):
                text += f'{i}. {task.title}\\n'
            self.todo_list_display.text = text

    def on_todo_stats(self, instance):
        stats = self.todo_list.get_statistics()
        text = f"""📊 Statistics:
        
Total: {stats['total_tasks']}
Completed: {stats['completed']}
Pending: {stats['pending']}
Rate: {stats['completion_rate']}
        """
        self.todo_list_display.text = text

    def on_todo_clear(self, instance):
        count = self.todo_list.clear_completed_tasks()
        self.todo_list_display.text = f'Cleared {count} completed tasks'
        self.on_todo_refresh(None)


if __name__ == '__main__':
    MathKingApp().run()
