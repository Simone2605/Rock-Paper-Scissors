import tkinter as tk
import rps_classes as clas
import rps_texts as text

# 1. build window
root = tk.Tk()
root.title('Rock, Paper, Scissors')
window_width = 700
window_height = 750
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
centerX = int(screen_width / 2 - window_width / 2)
centerY = int(screen_height / 2 - window_height / 2)
root.geometry(f'{window_width}x{window_height}+{centerX}+{centerY}')
root.resizable(width=False, height=False)

# 2. import icons
rps_icon = tk.PhotoImage(file=f'images/rockpaperscissors.png')
rpsls_icon = tk.PhotoImage(file=f'images/rockpaperscissorslizardspock.png')
rock_icon = tk.PhotoImage(file=f'images/rock.png')
paper_icon = tk.PhotoImage(file=f'images/paper.png')
scissors_icon = tk.PhotoImage(file=f'images/scissors.png')
lizard_icon = tk.PhotoImage(file=f'images/lizard.png')
spock_icon = tk.PhotoImage(file=f'images/spock.png')
firework_icon = tk.PhotoImage(file=f'images/firework.png')
grave_icon = tk.PhotoImage(file=f'images/grave.png')

# 3. title, welcome and explanation
title_label = clas.Title(root, 'Rock, Paper, Scissors', rps_icon, 350, 50)

welcome_label = clas.Text(root, text.welcome_text, 350, 150)

# 10. end game: win or loose
win_label = clas.HiddenImage(root, firework_icon)
loose_label = clas.HiddenImage(root, grave_icon)

# 9. csv-files to save current score and score text
counter_user = open('counter_user.csv', 'w').write('0')
counter_pc = open('counter_pc.csv', 'w').write('0')
score_label = clas.HiddenText(root, f'{counter_user} : {counter_pc}')

# 8. fight texts
fight_rock_scissors = clas.HiddenText(root, 'ROCK  crushes  SCISSORS!')
fight_rock_lizard = clas.HiddenText(root, 'ROCK  crushes  LIZARD!')
fight_paper_rock = clas.HiddenText(root, 'PAPER  covers  ROCK!')
fight_paper_spock = clas.HiddenText(root, 'PAPER  disproves  SPOCK!')
fight_scissors_paper = clas.HiddenText(root, 'SCISSORS  cuts  PAPER!')
fight_scissors_lizard = clas.HiddenText(root, 'SCISSORS  decapitates  LIZARD!')
fight_lizard_paper = clas.HiddenText(root, 'LIZARD  eats  PAPER!')
fight_lizard_spock = clas.HiddenText(root, 'LIZARD  poisons  SPOCK!')
fight_spock_rock = clas.HiddenText(root, 'SPOCK  vaporizes  ROCK!')
fight_spock_scissors = clas.HiddenText(root, 'SPOCK  smashes  SCISSORS!')
fight_undecided = clas.HiddenText(root, 'undecided')
fight_labels = [fight_rock_scissors, fight_rock_lizard, fight_paper_rock, fight_paper_spock, fight_scissors_paper,
                fight_scissors_lizard, fight_lizard_paper, fight_lizard_spock, fight_spock_rock, fight_spock_scissors,
                fight_undecided]

# 7. user signs vs. pc signs
rock_label = clas.HiddenImageText(root, rock_icon, 'ROCK')
paper_label = clas.HiddenImageText(root, paper_icon, 'PAPER')
scissors_label = clas.HiddenImageText(root, scissors_icon, 'SCISSORS')
lizard_label = clas.HiddenImageText(root, lizard_icon, 'LIZARD')
spock_label = clas.HiddenImageText(root, spock_icon, 'SPOCK')
vs_label = clas.HiddenText(root, 'vs.')

rock_label_pc = rock_label
paper_label_pc = paper_label
scissors_label_pc = scissors_label
lizard_label_pc = lizard_label
spock_label_pc = spock_label
pc_labels = [rock_label_pc, paper_label_pc, scissors_label_pc, lizard_label_pc, spock_label_pc]
user_labels = [rock_label, paper_label, scissors_label, lizard_label, spock_label]

# 6. click on button to start game and choose your sign
spock_button = clas.HiddenImageTextButton(root, spock_icon, 'SPOCK',
                                          [[spock_label, 250, 475], [vs_label, 350, 475]],
                                          [rock_label, paper_label, scissors_label, lizard_label],
                                          [], user_labels, pc_labels, fight_labels, score_label,
                                          win_label, loose_label)

lizard_button = clas.HiddenImageTextButton(root, lizard_icon, 'LIZARD',
                                           [[lizard_label, 250, 475], [vs_label, 350, 475]],
                                           [rock_label, paper_label, scissors_label, spock_label],
                                           spock_button, user_labels, pc_labels, fight_labels, score_label,
                                           win_label, loose_label)

scissors_button = clas.HiddenImageTextButton(root, scissors_icon, 'SCISSORS',
                                             [[scissors_label, 250, 475], [vs_label, 350, 475]],
                                             [rock_label, paper_label, lizard_label, spock_label],
                                             spock_button, user_labels, pc_labels, fight_labels, score_label,
                                             win_label, loose_label)

paper_button = clas.HiddenImageTextButton(root, paper_icon, 'PAPER',
                                          [[paper_label, 250, 475], [vs_label, 350, 475]],
                                          [rock_label, scissors_label, lizard_label, spock_label],
                                          spock_button, user_labels, pc_labels, fight_labels, score_label,
                                          win_label, loose_label)

rock_button = clas.HiddenImageTextButton(root, rock_icon, 'ROCK',
                                         [[rock_label, 250, 475], [vs_label, 350, 475]],
                                         [paper_label, scissors_label, lizard_label, spock_label],
                                         spock_button, user_labels, pc_labels, fight_labels, score_label,
                                         win_label, loose_label)

# 5. choose version
v1_label = clas.HiddenText(root, 'classic version:')

v2_label = clas.HiddenText(root, 'extended version:')

v1_button = clas.HiddenImageButton(root, rps_icon,
                                   [[rock_button, 250, 375], [paper_button, 350, 375], [scissors_button, 450, 375]],
                                   [lizard_button, spock_button])
v2_button = clas.HiddenImageButton(root, rpsls_icon,
                                   [[rock_button, 150, 375], [paper_button, 250, 375], [scissors_button, 350, 375],
                                    [lizard_button, 450, 375], [spock_button, 550, 375]], [])

# 4. type in username
username_label = clas.Text(root, 'What is your name?', x=95, y=225)

username_entry = clas.Entry(root, 'username', 20, 230, 225, [[v1_label, 250, 260], [v2_label, 450, 260]],
                            [[v1_button, 250, 290], [v2_button, 450, 290]])

root.mainloop()
