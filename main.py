import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Создание окна tkinter
root = tk.Tk()
root.title("3D буква 'Г'")
root.geometry("1200x900")  # Увеличение размера окна

# Параметры трансформации
scale_factor = [4, 4, 4]  # Начальный масштаб увеличен в 2 раза
translate = [0, 0, 0]
rotate_angle = [0, 0, 0]  # Углы вращения по X, Y, Z

# Каркас буквы 'Г' (в виде правильной пропорции)
vertices = np.array([
    [0, 0, 0], [3, 0, 0], [3, 0.5, 0], [1, 0.5, 0], [1, 4, 0],
    [0, 4, 0], [0, 0, 1], [3, 0, 1], [3, 0.5, 1], [1, 0.5, 1],
    [1, 4, 1], [0, 4, 1]
])


# Функция для обновления графика
def update_plot():
    ax.cla()  # Очистка осей
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_xlim([-25, 25])  # Увеличение диапазона для оси X
    ax.set_ylim([-25, 25])  # Увеличение диапазона для оси Y
    ax.set_zlim([-25, 25])  # Увеличение диапазона для оси Z

    # Применение трансформаций к вершинам
    transformed_vertices = vertices.copy()

    # Масштабирование
    transformed_vertices *= scale_factor

    # Перенос
    transformed_vertices += translate

    # Вращение
    transformed_vertices = rotate(transformed_vertices, rotate_angle)

    # Определение граней буквы 'Г'
    faces = [
        [0, 1, 2, 3, 4, 5], [6, 7, 8, 9, 10, 11],  # Передняя и задняя
        [0, 6, 7, 1], [1, 7, 8, 2], [2, 8, 9, 3], [3, 9, 10, 4], [4, 10, 11, 5], [5, 11, 6, 0]  # Боковые
    ]

    poly3d = [[transformed_vertices[vertice] for vertice in face] for face in faces]
    ax.add_collection3d(Poly3DCollection(poly3d, facecolors='cyan', linewidths=1, edgecolors='r', alpha=.25))

    canvas.draw()


# Функция для вращения по углам (углы в радианах)
def rotate(vertices, angles):
    Rx = np.array([[1, 0, 0], [0, np.cos(angles[0]), -np.sin(angles[0])], [0, np.sin(angles[0]), np.cos(angles[0])]])
    Ry = np.array([[np.cos(angles[1]), 0, np.sin(angles[1])], [0, 1, 0], [-np.sin(angles[1]), 0, np.cos(angles[1])]])
    Rz = np.array([[np.cos(angles[2]), -np.sin(angles[2]), 0], [np.sin(angles[2]), np.cos(angles[2]), 0], [0, 0, 1]])
    R = Rz @ Ry @ Rx  # Общая матрица вращения
    return vertices @ R.T


# Функции для изменения параметров трансформации
def on_scale_x(val):
    scale_factor[0] = float(val)
    update_plot()


def on_scale_y(val):
    scale_factor[1] = float(val)
    update_plot()


def on_scale_z(val):
    scale_factor[2] = float(val)
    update_plot()


def on_translate_x(val):
    translate[0] = float(val)
    update_plot()


def on_translate_y(val):
    translate[1] = float(val)
    update_plot()


def on_translate_z(val):
    translate[2] = float(val)
    update_plot()


def on_rotate_x(val):
    rotate_angle[0] = np.radians(float(val))
    update_plot()


def on_rotate_y(val):
    rotate_angle[1] = np.radians(float(val))
    update_plot()


def on_rotate_z(val):
    rotate_angle[2] = np.radians(float(val))
    update_plot()


# Функция для сброса трансформаций в начальные значения
def reset_view():
    global scale_factor, translate, rotate_angle
    scale_factor = [4, 4, 4]  # Начальный масштаб увеличен в 2 раза
    translate = [0, 0, 0]
    rotate_angle = [0, 0, 0]

    scale_x.set(scale_factor[0])
    scale_y.set(scale_factor[1])
    scale_z.set(scale_factor[2])
    trans_x.set(translate[0])
    trans_y.set(translate[1])
    trans_z.set(translate[2])
    rot_x.set(np.degrees(rotate_angle[0]))
    rot_y.set(np.degrees(rotate_angle[1]))
    rot_z.set(np.degrees(rotate_angle[2]))

    update_plot()


# Элементы интерфейса tkinter
tk.Label(root, text="Масштаб по X").grid(row=0, column=0)
scale_x = tk.DoubleVar(value=4)
scale_x_slider = tk.Scale(root, from_=0.1, to=10, orient=tk.HORIZONTAL, resolution=0.1, variable=scale_x,
                          command=on_scale_x)
scale_x_slider.grid(row=0, column=1)

tk.Label(root, text="Масштаб по Y").grid(row=1, column=0)
scale_y = tk.DoubleVar(value=4)
scale_y_slider = tk.Scale(root, from_=0.1, to=10, orient=tk.HORIZONTAL, resolution=0.1, variable=scale_y,
                          command=on_scale_y)
scale_y_slider.grid(row=1, column=1)

tk.Label(root, text="Масштаб по Z").grid(row=2, column=0)
scale_z = tk.DoubleVar(value=4)
scale_z_slider = tk.Scale(root, from_=0.1, to=10, orient=tk.HORIZONTAL, resolution=0.1, variable=scale_z,
                          command=on_scale_z)
scale_z_slider.grid(row=2, column=1)

tk.Label(root, text="Смещение по X").grid(row=3, column=0)
trans_x = tk.DoubleVar(value=0)
trans_x_slider = tk.Scale(root, from_=-15, to=15, orient=tk.HORIZONTAL, resolution=0.1, variable=trans_x,
                          command=on_translate_x)
trans_x_slider.grid(row=3, column=1)

tk.Label(root, text="Смещение по Y").grid(row=4, column=0)
trans_y = tk.DoubleVar(value=0)
trans_y_slider = tk.Scale(root, from_=-15, to=15, orient=tk.HORIZONTAL, resolution=0.1, variable=trans_y,
                          command=on_translate_y)
trans_y_slider.grid(row=4, column=1)

tk.Label(root, text="Смещение по Z").grid(row=5, column=0)
trans_z = tk.DoubleVar(value=0)
trans_z_slider = tk.Scale(root, from_=-15, to=15, orient=tk.HORIZONTAL, resolution=0.1, variable=trans_z,
                          command=on_translate_z)
trans_z_slider.grid(row=5, column=1)

tk.Label(root, text="Вращение по X").grid(row=6, column=0)
rot_x = tk.DoubleVar(value=0)
rot_x_slider = tk.Scale(root, from_=-180, to=180, orient=tk.HORIZONTAL, resolution=1, variable=rot_x,
                        command=on_rotate_x)
rot_x_slider.grid(row=6, column=1)

tk.Label(root, text="Вращение по Y").grid(row=7, column=0)
rot_y = tk.DoubleVar(value=0)
rot_y_slider = tk.Scale(root, from_=-180, to=180, orient=tk.HORIZONTAL, resolution=1, variable=rot_y,
                        command=on_rotate_y)
rot_y_slider.grid(row=7, column=1)

tk.Label(root, text="Вращение по Z").grid(row=8, column=0)
rot_z = tk.DoubleVar(value=0)
rot_z_slider = tk.Scale(root, from_=-180, to=180, orient=tk.HORIZONTAL, resolution=1, variable=rot_z,
                        command=on_rotate_z)
rot_z_slider.grid(row=8, column=1)

reset_button = tk.Button(root, text="Начальный вид", command=reset_view)
reset_button.grid(row=9, column=0, columnspan=2)

# Создание фигуры и канваса для отображения графика
fig = plt.Figure(figsize=(10, 8), dpi=100)
ax = fig.add_subplot(111, projection='3d')

canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().grid(row=0, column=2, rowspan=10)

update_plot()

root.mainloop()
