import tkinter as tk
from tkinter import ttk
import random


class Label:
    def __init__(self, root):
        self.label = ttk.Label(root)


class Title(Label):
    def __init__(self, root, text, image, x, y):
        Label.__init__(self, root)
        self.label.config(text=text,
                          font=('Corbel', 20, 'bold underline'),
                          image=image,
                          compound=tk.BOTTOM)
        self.label.place(x=x, y=y, anchor='center')


class Text(Label):
    def __init__(self, root, text, x, y):
        Label.__init__(self, root)
        self.label.config(text=text,
                          font=('Corbel', 12))
        self.label.place(x=x, y=y, anchor='center')


class HiddenText(Label):
    def __init__(self, root, text):
        Label.__init__(self, root)
        self.label.config(text=text,
                          font=('Corbel', 12))


class HiddenImage(Label):
    def __init__(self, root, image):
        Label.__init__(self, root)
        self.label.config(image=image)


class HiddenImageText(HiddenText):
    def __init__(self, root, image, text):
        HiddenText.__init__(self, root, text)
        self.label.config(text=text,
                          image=image,
                          compound=tk.BOTTOM)


class Entry:
    def __init__(self, root, textvariable, width, x, y, showlabels, showbuttons):
        self.entry = ttk.Entry(root, textvariable=textvariable, width=width)
        self.entry.place(x=x, y=y, anchor='center')
        self.showlabels = showlabels
        self.showbuttons = showbuttons
        self.entry.bind('<Return>', lambda event: self.click(showlabels, showbuttons))
        self.entry_var = ''

    def click(self, showlabels, showbuttons):
        # disable entry itself
        self.entry.config(state='disabled')

        # show version labels and buttons
        for label in showlabels:
            label[0].label.place(x=label[1], y=label[2], anchor='center')
        for button in showbuttons:
            button[0].button.place(x=button[1], y=button[2], anchor='center')

        # save entry
        self.entry_var = self.entry.get()
        username = open('username.txt', 'w').write(f'{self.entry_var}')


class HiddenButton:
    def __init__(self, root):
        self.button = ttk.Button(root)


class HiddenImageButton(HiddenButton):
    def __init__(self, root, image, showbuttons, hidebuttons):
        HiddenButton.__init__(self, root)
        self.button.config(image=image)
        self.button.bind('<Button-1>', lambda event: self.click(showbuttons, hidebuttons))

    def click(self, showbuttons, hidebuttons):

        # check if version is not already chosen
        if not showbuttons[0][0].button.winfo_ismapped():

            # show sign buttons of chosen version
            for button in showbuttons:
                button[0].button.place(x=button[1], y=button[2], anchor='center')

        else:
            pass


class HiddenImageTextButton(HiddenButton):
    def __init__(self, root, image, text, showlabels, hidelabels, versionteaser, userlabels, pclabels, fightlabels,
                 scorelabel, winlabel, looselabel):
        HiddenButton.__init__(self, root)
        self.button.config(text=text, image=image, compound=tk.TOP)
        self.button.bind('<Button-1>', lambda event: (
            self.click(showlabels, hidelabels, versionteaser, userlabels, pclabels, fightlabels, scorelabel, winlabel,
                       looselabel)))

    def click(self, showlabels, hidelabels, versionteaser, userlabels, pclabels, fightlabels, scorelabel, winlabel,
              looselabel):

        # check if user or pc not already has won:
        if not winlabel.label.winfo_ismapped() and not looselabel.label.winfo_ismapped():

            # show thrown sign label
            for label in showlabels:
                label[0].label.place(x=label[1], y=label[2], anchor='center')

            # hide other labels
            for label in hidelabels:
                label.label.place_forget()
            for label in fightlabels:
                label.label.place_forget()

            # show random label for pc
            if versionteaser == [] or versionteaser.button.winfo_ismapped():
                i = random.randint(0, 4)
            elif not versionteaser.button.winfo_ismapped():
                i = random.randint(0, 2)
            pclabels[i].label.place(x=450, y=475, anchor='center')

            # show fight text
            if showlabels[0][0] == userlabels[0] and pclabels[i] == pclabels[2]:
                fightlabels[0].label.place(x=350, y=525, anchor='center')
                open('counter_user.csv', 'a').write('1')
            elif showlabels[0][0] == userlabels[0] and pclabels[i] == pclabels[3]:
                fightlabels[1].label.place(x=350, y=525, anchor='center')
                open('counter_user.csv', 'a').write('1')
            elif showlabels[0][0] == userlabels[1] and pclabels[i] == pclabels[0]:
                fightlabels[2].label.place(x=350, y=525, anchor='center')
                open('counter_user.csv', 'a').write('1')
            elif showlabels[0][0] == userlabels[1] and pclabels[i] == pclabels[4]:
                fightlabels[3].label.place(x=350, y=525, anchor='center')
                open('counter_user.csv', 'a').write('1')
            elif showlabels[0][0] == userlabels[2] and pclabels[i] == pclabels[1]:
                fightlabels[4].label.place(x=350, y=525, anchor='center')
                open('counter_user.csv', 'a').write('1')
            elif showlabels[0][0] == userlabels[2] and pclabels[i] == pclabels[3]:
                fightlabels[5].label.place(x=350, y=525, anchor='center')
                open('counter_user.csv', 'a').write('1')
            elif showlabels[0][0] == userlabels[3] and pclabels[i] == pclabels[1]:
                fightlabels[6].label.place(x=350, y=525, anchor='center')
                open('counter_user.csv', 'a').write('1')
            elif showlabels[0][0] == userlabels[3] and pclabels[i] == pclabels[4]:
                fightlabels[7].label.place(x=350, y=525, anchor='center')
                open('counter_user.csv', 'a').write('1')
            elif showlabels[0][0] == userlabels[4] and pclabels[i] == pclabels[0]:
                fightlabels[8].label.place(x=350, y=525, anchor='center')
                open('counter_user.csv', 'a').write('1')
            elif showlabels[0][0] == userlabels[4] and pclabels[i] == pclabels[2]:
                fightlabels[9].label.place(x=350, y=525, anchor='center')
                open('counter_user.csv', 'a').write('1')
            elif showlabels[0][0] == userlabels[2] and pclabels[i] == pclabels[0]:
                fightlabels[0].label.place(x=350, y=525, anchor='center')
                open('counter_pc.csv', 'a').write('1')
            elif showlabels[0][0] == userlabels[3] and pclabels[i] == pclabels[0]:
                fightlabels[1].label.place(x=350, y=525, anchor='center')
                open('counter_pc.csv', 'a').write('1')
            elif showlabels[0][0] == userlabels[0] and pclabels[i] == pclabels[1]:
                fightlabels[2].label.place(x=350, y=525, anchor='center')
                open('counter_pc.csv', 'a').write('1')
            elif showlabels[0][0] == userlabels[4] and pclabels[i] == pclabels[1]:
                fightlabels[3].label.place(x=350, y=525, anchor='center')
                open('counter_pc.csv', 'a').write('1')
            elif showlabels[0][0] == userlabels[1] and pclabels[i] == pclabels[2]:
                fightlabels[4].label.place(x=350, y=525, anchor='center')
                open('counter_pc.csv', 'a').write('1')
            elif showlabels[0][0] == userlabels[3] and pclabels[i] == pclabels[2]:
                fightlabels[5].label.place(x=350, y=525, anchor='center')
                open('counter_pc.csv', 'a').write('1')
            elif showlabels[0][0] == userlabels[1] and pclabels[i] == pclabels[3]:
                fightlabels[6].label.place(x=350, y=525, anchor='center')
                open('counter_pc.csv', 'a').write('1')
            elif showlabels[0][0] == userlabels[4] and pclabels[i] == pclabels[3]:
                fightlabels[7].label.place(x=350, y=525, anchor='center')
                open('counter_pc.csv', 'a').write('1')
            elif showlabels[0][0] == userlabels[0] and pclabels[i] == pclabels[4]:
                fightlabels[8].label.place(x=350, y=525, anchor='center')
                open('counter_pc.csv', 'a').write('1')
            elif showlabels[0][0] == userlabels[0] and pclabels[i] == pclabels[4]:
                fightlabels[9].label.place(x=350, y=525, anchor='center')
                open('counter_pc.csv', 'a').write('1')
            else:
                fightlabels[10].label.place(x=350, y=525, anchor='center')

            # show score
            counter_user = open('counter_user.csv', 'r').read()
            counter_user = sum([int(i) for i in counter_user])
            counter_pc = open('counter_pc.csv', 'r').read()
            counter_pc = sum([int(i) for i in counter_pc])
            scorelabel.label.config(text=f'{counter_user} : {counter_pc}')
            scorelabel.label.place(x=350, y=550, anchor='center')

            # check for winner
            if counter_user >= 3:
                username = open('username.txt', 'r').read()
                winlabel.label.config(text=f'You won! Congratulations, {username}!',
                                      font=('Corbel', 15, 'bold'),
                                      compound=tk.BOTTOM)
                winlabel.label.place(x=350, y=650, anchor='center')
            if counter_pc >= 3:
                looselabel.label.config(text='You loose! Game over!',
                                        font=('Corbel', 15, 'bold'),
                                        compound=tk.BOTTOM)
                looselabel.label.place(x=350, y=650, anchor='center')
        else:
            pass
