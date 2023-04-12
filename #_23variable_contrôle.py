#coding:utf-8
import tkinter
import tkinter.messagebox as tkmes
"""
StringVar()
IntVar()
DoubleVar()
BooleanVar()

type de police récement utilisé:	Old English Text MT | MD thaitype A
"""

win = tkinter.Tk()
win.geometry("650x400")
win.title("#_22Variable_de_contrôle")
win.maxsize(800, 500)
win.minsize(450, 253)

varlabel_1 = tkinter.StringVar()
label_1 = tkinter.Label(win, text = "Bonjour je suis un texte écrit....", font = ("Old English Text MT", 30), textvariable = varlabel_1)
varlabel_1.set("Hello I'm a Text!!!!!")#La méthode .set() fonctionne qu'avec les variables afféctés à des variables de contrôle
label_1.pack()

#Définition d'une fonction observateur Entry|Label
def update_load(*args):
	varlabel_2.set(entry_1.get())
	if len(entry_1.get()) == 0:
		varlabel_2.set("Input Text")

#Définition d'une fonction observateur Radiobutton
def radobs(*args):
	if var_rad.get():
		varlabel_4.set("Vous avez choisit Menu ©")
	else:
		varlabel_4.set("Vous avez choisit Acceuil ®")

#Définition d'une fonction observateur au rapport
def button_rap(*args):
	if var_rad_2.get():
		varlabel_3.set("Vous avez séléctionné l'option Femme ©")
	else:
		varlabel_3.set("Vous avez séléctionné l'option Homme ®")

varentry = tkinter.StringVar()
varentry.trace("w", update_load)
entry_1 = tkinter.Entry(win, font = ("MD thaitype A", 30), bg = "black", fg = "white", textvariable = varentry)
entry_1.pack()

varlabel_2 = tkinter.StringVar()
label_2 = tkinter.Label(win, textvariable = varlabel_2, font = ("Blackadder ITC", 37), fg = "blue")
varlabel_2.set("Input Text!!!")
label_2.pack()

var_rad = tkinter.IntVar()
var_rad.trace("w", radobs)
radio_1 = tkinter.Radiobutton(win, text = "Acceuil", value = False, variable = var_rad)
radio_2 = tkinter.Radiobutton(win, text = "Menu   ", value = True, variable = var_rad)
radio_1.pack()
radio_2.pack()

var_rad_2 = tkinter.IntVar()
var_rad_2.trace("w", button_rap)
radio_3 = tkinter.Radiobutton(win, text = "Homme", fg = "blue", value = 0, variable = var_rad_2)
radio_4 = tkinter.Radiobutton(win, text = "Female", fg = "green", value = 1, variable = var_rad_2)
radio_3.pack()
radio_4.pack()

varlabel_4 = tkinter.StringVar()
label_4 = tkinter.Label(win, textvariable = varlabel_4, bg = "darkgrey", font = ("Arial", 15))
varlabel_4.set("Button 1 & 2 rapport")
label_4.pack()

varlabel_3 = tkinter.StringVar()
label_3 = tkinter.Label(win, text = str(), font = ("Arial", 15), textvariable = varlabel_3, bg = "darkgrey")
varlabel_3.set("Button 3 & 4 rapport!")
label_3.pack()

win.mainloop()