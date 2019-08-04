import tkinter as tk
from tkinter import ttk

app = tk.Tk()



class LabelInput(tk.Frame):
	'''A frame containing labels and input'''
	def __init__(self,label='',input_class=ttk.Entry,input_var=None,input_args=None,label_args=None,**kwargs):
		super.__init__(parent,**kwargs)
		input_args=input_args or {}
		label_args=input_var or {}
		self.variable=input_var
		if input_class in (ttk.Checkbutton,ttk.Button,ttk.Radioibutton):
			input_args["text"]=label
			input_args["variable"]=input_var
		else:
			self.label = ttk.Label(self, text=label, **label_args)
			self.label.grid(row=0, column=0, sticky=(tk.W + tk.E))
			input_args["textvariable"] = input_var
		self.input = input_class(self, **input_args)
		self.input.grid(row=1, column=0, sticky=(tk.W + tk.E))
		columnconfigure(0,weight=)


app.mainloop()