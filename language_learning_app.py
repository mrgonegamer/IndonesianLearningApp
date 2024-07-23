import tkinter as tk
import random
from words import words
from counting import counting  # Updated import
from days import days
from phrases import phrases

class LanguageLearningApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Language Learning App")
        
        self.main_menu()

    def main_menu(self):
        self.clear_frame()

        self.label = tk.Label(self.root, text="Select a category to learn:", font=("Arial", 14))
        self.label.pack(pady=20)

        self.words_button = tk.Button(self.root, text="Words", font=("Arial", 14), command=lambda: self.start_category(words))
        self.words_button.pack(pady=10)

        self.counting_button = tk.Button(self.root, text="Counting", font=("Arial", 14), command=lambda: self.start_category(counting))
        self.counting_button.pack(pady=10)

        self.days_button = tk.Button(self.root, text="Days", font=("Arial", 14), command=lambda: self.start_category(days))
        self.days_button.pack(pady=10)

        self.phrases_button = tk.Button(self.root, text="Phrases", font=("Arial", 14), command=lambda: self.start_category(phrases))
        self.phrases_button.pack(pady=10)

    def start_category(self, category):
        self.category = category
        self.clear_frame()

        self.back_button = tk.Button(self.root, text="Back", font=("Arial", 12), command=self.main_menu)
        self.back_button.pack(pady=10)

        self.label = tk.Label(self.root, text="Click on the word to see the translation!", font=("Arial", 14))
        self.label.pack(pady=20)

        self.word_button = tk.Button(self.root, text="", font=("Arial", 20), command=self.show_translation)
        self.word_button.pack(pady=20)

        self.translation_label = tk.Label(self.root, text="", font=("Arial", 14), fg="blue")
        self.translation_label.pack(pady=20)

        self.next_button = tk.Button(self.root, text="Next", font=("Arial", 14), command=self.next_word)
        self.next_button.pack(pady=20)

        self.current_word = ""
        self.next_word()

    def show_translation(self):
        indonesian_word = self.category[self.current_word]
        self.translation_label.config(text=f"{self.current_word} in Indonesian is '{indonesian_word}'")

    def next_word(self):
        self.current_word = random.choice(list(self.category.keys()))
        self.word_button.config(text=self.current_word)
        self.translation_label.config(text="")

    def clear_frame(self):
        for widget in self.root.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = LanguageLearningApp(root)
    root.mainloop()
