from random import *
from tkinter import *

window = Tk()
window.geometry('190x450')
window.config(bg = 'hot pink')
window.title('Быки и коровы!')

count = 0
words = ['слон', 'кора', 'гроб', 'мыло', 'мозг', 'крот', 'соль', 'лось',
         'кедр']
answer = choice(words)
otvet = ''


def Click(event):
    global count
    attempt = ans.get()
    bulls = 0
    cows = 0
    count += 1
    if attempt == answer:
        print('Ты угадал, это', answer)
        print('Количество попыток:', count)
        letter1['text'] = answer[0]
        letter2['text'] = answer[1]
        letter3['text'] = answer[2]
        letter4['text'] = answer[3]
        check.unbind('<Button-1>')
    else:
        if len(attempt) > 4 or len(set(attempt)) < 4:
            attempt = input('Нужно слово из 4 различных букв, '
                            'попробуй еще раз.\n')
        else:
            for i in range(4):
                if attempt[i] == answer[i]:
                    bulls += 1
                elif attempt[i] in answer:
                     cows += 1
        print(str(count), '.', 'Быки:', bulls, 'Коровы:', cows, attempt)

top = Label(text = 'Отгадай слово!', font = 'Times 26', bg = 'cyan',
            fg = 'dark green')
top.grid(row = 0, column = 0, columnspan = 4, padx = 5, pady = 5)

letter1 = Label(text = '*', font = 'Times 18', bg = 'skyblue',
            fg = 'black', width = '2')
letter2 = Label(text = '*', font = 'Times 18', bg = 'DarkOrchid',
            fg = 'black', width = '2')
letter3 = Label(text = '*', font = 'Times 18', bg = 'cadet blue',
            fg = 'black', width = '2')
letter4 = Label(text = '*', font = 'Times 18', bg = 'dark salmon',
            fg = 'black', width = '2')

letter1.grid(row = 1, column = 0, padx = 5, pady = 5)
letter2.grid(row = 1, column = 1, padx = 5, pady = 5)
letter3.grid(row = 1, column = 2, padx = 5, pady = 5)
letter4.grid(row = 1, column = 3, padx = 5, pady = 5)

question = Label(text = 'Твой вариант:', font = 'Times 12', bg = 'cornsilk',
            fg = 'dark red')
question.grid(row = 2, column = 0, columnspan = 4, padx = 5, pady = 5)
ans = Entry(text = '', font = 'Times 12', bg = 'goldenrod')
ans.grid(row = 3, column = 0, columnspan = 4, padx = 5, pady = 5)
check = Button(text = 'Проверить!', font = 'Times 16', fg = 'maroon')
check.grid(row = 4, column = 0, columnspan = 4, padx = 5, pady = 5)
bottom_text = Label(text = otvet, font = 'Times 12',
                    bg = 'hot pink')
bottom_text.grid(row = 5, column = 0, columnspan = 4, padx = 5, pady = 5)
check.bind('<Button-1>', Click)

window.mainloop()
