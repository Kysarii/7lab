from itertools import combinations
from tkinter import *
from tkinter.messagebox import showwarning
from tkinter.scrolledtext import ScrolledText

nmax = 10

def square(a, b, c, d):
    if a == b and a == c and a == d and b == c and b == d and c == d:
        return False
    else:
        s1 = (a['x'] - b['x']) ** 2 + (a['y'] - b['y']) ** 2
        s2 = (a['x'] - c['x']) ** 2 + (a['y'] - c['y']) ** 2
        s3 = (a['x'] - d['x']) ** 2 + (a['y'] - d['y']) ** 2
        s4 = (b['x'] - c['x']) ** 2 + (b['y'] - c['y']) ** 2
        s5 = (b['x'] - d['x']) ** 2 + (b['y'] - d['y']) ** 2
        s6 = (c['x'] - d['x']) ** 2 + (c['y'] - d['y']) ** 2
        return ((s1 == s3) and (s1 == s4) and (s1 == s6) and (s2 == s5) and (s2 == 2 * s1)) \
            or ((s1 == s2) and (s1 == s5) and (s1 == s6) and (s3 == s4) and (s3 == 2 * s1)) \
            or ((s2 == s3) and (s2 == s4) and (s2 == s5) and (s1 == s6) and (s1 == 2 * s2))

def find_square_alg(t, n):
    s_list = []
    n_list = []
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                for l in range(k + 1, n):
                    if square(t[i], t[j], t[k], t[l]):
                        s_list.append([[t[i]['x'], t[i]['y']],
                                       [t[j]['x'], t[j]['y']],
                                       [t[k]['x'], t[k]['y']],
                                       [t[l]['x'], t[l]['y']]])
                    else:
                        n_list.append([[t[i]['x'], t[i]['y']],
                                       [t[j]['x'], t[j]['y']],
                                       [t[k]['x'], t[k]['y']],
                                       [t[l]['x'], t[l]['y']]])
    return s_list, n_list


def find_square_py(t):
    s_list = []
    n_list = []
    for combination in list(combinations(t, 4)):
        if square(combination[0], combination[1], combination[2], combination[3]):
            s_list.append([[combination[0]['x'], combination[0]['y']],
                           [combination[1]['x'], combination[1]['y']],
                           [combination[2]['x'], combination[2]['y']],
                           [combination[3]['x'], combination[3]['y']]])
        else:
            n_list.append([[combination[0]['x'], combination[0]['y']],
                           [combination[1]['x'], combination[1]['y']],
                           [combination[2]['x'], combination[2]['y']],
                           [combination[3]['x'], combination[3]['y']]])
    return s_list, n_list

def find_square_opt(t):
    s_list = []
    n_list = []
    filtered_t = list(filter(lambda p: p['x'] % 2 == 0 and p['y'] % 2 == 0, t))
    for combination in list(combinations(filtered_t, 4)):
        if square(combination[0], combination[1], combination[2], combination[3]):
            s_list.append([[combination[0]['x'], combination[0]['y']],
                           [combination[1]['x'], combination[1]['y']],
                           [combination[2]['x'], combination[2]['y']],
                           [combination[3]['x'], combination[3]['y']]])
        else:
            n_list.append([[combination[0]['x'], combination[0]['y']],
                           [combination[1]['x'], combination[1]['y']],
                           [combination[2]['x'], combination[2]['y']],
                           [combination[3]['x'], combination[3]['y']]])
    return s_list, n_list

def clear_coordinates_interface():
    for interface_fields in interface_coordinates_fields:
        for field in interface_fields:
            field.destroy()

def resize_and_center(window_width, window_height):
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x_cordinate = int((screen_width / 2) - (window_width / 2))
    y_cordinate = int((screen_height / 2) - (window_height / 2))
    root.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))

def create_squares():
    global t
    for idx, coordinates in enumerate(coordinates_entries):
        t[idx]['x'] = int(coordinates[0].get())
        t[idx]['y'] = int(coordinates[1].get())

    resize_and_center(750, 550)
    create_square_fields()

    square_list, no_square_list = find_square_alg(t, n)
    if len(square_list) > 0:
        algo_scrolled_text.insert(INSERT, f"Квадрат: \n{square_list}\n")
        algo_scrolled_text.insert(INSERT, f"А из этих точек нельзя сделать квадрат: \n{no_square_list}")
    else:
        algo_scrolled_text.insert(INSERT, f"Для данных точек нельзя сделать квадрат")


    square_list, no_square_list = find_square_py(t)
    if len(square_list) > 0:
        py_scrolled_text.insert(INSERT, f"Квадрат: \n{square_list}\n")
        py_scrolled_text.insert(INSERT, f"А из этих точек нельзя сделать квадрат: \n{no_square_list}")
    else:
        py_scrolled_text.insert(INSERT, f"Для данных точек нельзя сделать квадрат")


    square_list, no_square_list = find_square_opt(t)
    if len(square_list) > 0:
        py_with_condition_scrolled_text.insert(INSERT, f"Квадрат: \n{square_list}\n")
    else:
        py_with_condition_scrolled_text.insert(INSERT, f"Для данных точек(с условием) нельзя сделать квадрат")

def create_square_fields():
    global algo_scrolled_text, py_scrolled_text, py_with_condition_scrolled_text
    Label(right_frame, text="Решение алгоритмически").grid(row=0, padx=5, pady=5)
    algo_scrolled_text = ScrolledText(right_frame, wrap=WORD, width=40, height=8)
    algo_scrolled_text.grid(row=1, padx=5, pady=5)

    Label(right_frame, text="Решение с помощью функции python'a").grid(row=2, padx=5, pady=5)
    py_scrolled_text = ScrolledText(right_frame, wrap=WORD, width=40, height=8)
    py_scrolled_text.grid(row=3, padx=5, pady=5)

    Label(right_frame, text="Решение с ограничением").grid(row=4, padx=5, pady=5)
    py_with_condition_scrolled_text = ScrolledText(right_frame, wrap=WORD, width=40, height=8)
    py_with_condition_scrolled_text.grid(row=5, padx=5, pady=5)

coordinates_entries = []
interface_coordinates_fields = []
algo_scrolled_text = ''
py_scrolled_text = ''
py_with_condition_scrolled_text = ''

def create_entry_fields(n):
    global interface_coordinates_fields
    for i in range(n):
        label_x = Label(coordinates_frame, text="x:")
        label_x.grid(row=i + 1, column=0, padx=5, pady=5)
        coordinates_x = Entry(coordinates_frame, relief=RAISED, borderwidth=1)
        coordinates_x.grid(row=i + 1, column=1, padx=5, pady=5)

        label_y = Label(coordinates_frame, text="y:")
        label_y.grid(row=i + 1, column=2, padx=5, pady=5)
        coordinates_y = Entry(coordinates_frame, relief=RAISED, borderwidth=1)
        coordinates_y.grid(row=i + 1, column=3, padx=5, pady=5)

        coordinates_entries.append([coordinates_x, coordinates_y])
        interface_coordinates_fields.append([label_x, coordinates_x, label_y, coordinates_y])

    Button(input_frame, text="Найти квадраты", relief=RAISED, command=create_squares).grid(row=1, column=2, padx=5, pady=3)

t = []
def validate_n():
    global n, t, coordinates_entries, interface_coordinates_fields

    if len(interface_coordinates_fields) > 0:
        clear_coordinates_interface()
    coordinates_entries = []

    n = int(input_n.get())
    t = [{'x': 0, 'y': 0} for _ in range(n)]
    if not 4 <= n <= nmax:
        showwarning(title="Предупреждение", message=f"Количество точек должно быть больше 4 и меньше {nmax}")
    else:
        resize_and_center(350, 425)
        create_entry_fields(n)


root = Tk()
root.title("Квадратный поисковик")

root.config(bg="skyblue")

left_frame = Frame(root, width=200, height=400)
left_frame.grid(row=0, column=0, padx=10, pady=5)

right_frame = Frame(root, width=0, height=400, bg="skyblue")
right_frame.grid(row=0, column=1, padx=10, pady=5)

Label(left_frame, text="Введите количество точек: ").grid(row=0, padx=5, pady=5)

input_frame = Frame(left_frame, width=250, height=60)
input_frame.grid(row=1, padx=5, pady=5)
input_n = Entry(input_frame, relief=RAISED, borderwidth=2)
input_n.grid(row=1, column=0, padx=5, pady=3)
Button(input_frame, text="Ввод", relief=RAISED, borderwidth=2, command=validate_n).grid(row=1, column=1, padx=5, pady=5)

coordinates_frame = Frame(left_frame, width=250, height=185)
coordinates_frame.grid(row=2, padx=5, pady=5)

resize_and_center(280, 400)
root.mainloop()
