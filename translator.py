import tkinter as tk
from tkinter import ttk
from transformers import MarianMTModel, MarianTokenizer

class Translator:

	def __init__(self, root):
		self.root = root
		self.root.title("Language Translator")

		self.languages = ["ar", "de", "el", "en", "es", "fr", "it", "ja", "ko", "nl", "pt", "ru", "vi", "zh"]

		self.source_lang_label = ttk.Label(root, text="Source Language:")
		self.source_lang_var = tk.StringVar()
		self.source_lang_dropdown = ttk.Combobox(root, textvariable=self.source_lang_var, values=self.languages)
		self.source_lang_dropdown.set("en") #Set your default input language here.
		self.source_lang_label.grid(row=0, column=0, padx=10, pady=10)
		self.source_lang_dropdown.grid(row=0, column=1, padx=10, pady=10)

		self.target_lang_label = ttk.Label(root, text="Target Language:")
		self.target_lang_var = tk.StringVar()
		self.target_lang_dropdown = ttk.Combobox(root, textvariable=self.target_lang_var, values=self.languages)
		self.target_lang_dropdown.set("it") #Set your default output language here
		self.target_lang_label.grid(row=0, column=2, padx=10, pady=10)
		self.target_lang_dropdown.grid(row=0, column=3, padx=10, pady=10)

		self.input_label = ttk.Label(root, text="Enter text here!")
		self.input_text = tk.Text(root, height=5, width=40, state="normal")
		self.input_label.grid(row=1, column=0, padx=10, pady=10, columnspan=2)
		self.input_text.grid(row=1, column=2, padx=10, pady=10, columnspan=2)

		self.output_label = ttk.Label(root, text="Translation:")
		self.output_text = tk.Text(root, height=5, width=40, state="normal")
		self.output_label.grid(row=2, column=0, padx=10, pady=10, columnspan=2)
		self.output_text.grid(row=2, column=2, padx=10, pady=10, columnspan=2)

		self.translate_button = ttk.Button(root, text="Translate", command=self.translate_text)
		self.translate_button.grid(row=3, column=0, columnspan=4, pady=10)

	def translate_text(self):

		source_lang = self.source_lang_var.get()
		target_lang = self.target_lang_var.get()
		input_text = self.input_text.get("1.0", "end-1c")

		translated_text = translate_text(input_text, source_lang, target_lang)

		self.output_text.config(state="normal")
		self.output_text.delete("1.0", "end")
		self.output_text.insert("1.0", translated_text)
		self.output_text.config(state="disabled")

def translate_text(text, source_lang, target_lang):
	model_name = f'Helsinki-NLP/opus-mt-{source_lang}-{target_lang}'
	model = MarianMTModel.from_pretrained(model_name)
	tokenizer = MarianTokenizer.from_pretrained(model_name)

	input_ids = tokenizer.encode(text, return_tensors="pt")
	output_ids = model.generate(input_ids)
	translated_text = tokenizer.decode(output_ids[0], skip_special_tokens=True)

	return translated_text

if __name__ == "__main__":
	root = tk.Tk()
	app = Translator(root)
	root.mainloop()

