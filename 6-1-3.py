import tkinter as tk
from PIL import Image, ImageTk


class Window(object):
	def __init__(self):
		self.window = tk.Tk()
		question = tk.Label(text="Favorite food?")
		question.pack()
		show_hidden_btn = tk.Button(text="Show answer", command=lambda: self.handle_button())
		show_hidden_btn.pack()

	def run(self):
		self.window.mainloop()

	def handle_button(self):
		burger = ImageTk.PhotoImage(Image.open("burger.jpg"))
		burger_lbl = tk.Label(self.window)
		burger_lbl.image = burger
		burger_lbl.configure(image=burger)
		burger_lbl.pack(side=tk.BOTTOM)


def main():
	w = Window()
	w.run()


if __name__ == '__main__':
	main()