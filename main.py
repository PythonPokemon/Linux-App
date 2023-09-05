from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

class LinuxLearnApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')
        
        label = Label(text="Linux Lern-App", font_size=24)
        layout.add_widget(label)
        
        commands = [
            ("ls", "Liste Dateien und Verzeichnisse."),
            ("cd", "Wechsle das Verzeichnis."),
            ("pwd", "Zeigt das aktuelle Verzeichnis an."),
            ("mkdir", "Erstelle ein Verzeichnis."),
            ("cp", "Kopiere Dateien und Verzeichnisse."),
            ("mv", "Verschiebe Dateien und Verzeichnisse."),
            ("rm", "Lösche Dateien und Verzeichnisse."),
            ("chmod", "Ändere die Dateiberechtigungen."),
            ("grep", "Durchsuche Dateien nach einem Muster."),
            ("nano", "Öffne einen Texteditor."),
            ("man", "Zeige die Handbuchseite eines Befehls.")
        ]
        
        for command, description in commands:
            button = Button(text=command, font_size=16)
            button.bind(on_press=lambda _, desc=description: self.on_command_click(desc))
            layout.add_widget(button)

        
        self.output_label = Label(text="", font_size=16)
        layout.add_widget(self.output_label)
        
        return layout
    
    def on_command_click(self, description):
        self.output_label.text = description

if __name__ == '__main__':
    app = LinuxLearnApp()
    app.run()
