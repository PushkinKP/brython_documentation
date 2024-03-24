import tkinter
import customtkinter

'''
print("Bonjour")

import collecte_brython_trad

print(collecte_brython_trad.detection_langue())  

Récuperer toutes les informations dee tous les autres scripts pour faire le tableau de bord

'''


customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

window = customtkinter.CTk()

window.title("Etat des lieux du site de Brython")

screen_x = window.winfo_screenwidth()
screen_y = window.winfo_screenheight()
window_x = 960
window_y = 540
pos_x = (screen_x //2) - (window_x //2)
pos_y = (screen_y //2) - (window_y //2)
window.geometry("{}x{}+{}+{}".format(window_x, window_y, pos_x, pos_y))

window.minsize(960, 540)

window.maxsize(960, 540)


window.mainloop()