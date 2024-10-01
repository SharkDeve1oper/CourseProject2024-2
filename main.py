import tkinter as tk
from tkinter import messagebox


# Функция для нахождения обратной матрицы методом Гаусса-Жордана
def gauss_jordan_inverse(matrix):
    pass


# Функция для получения элементов матрицы и вычисления обратной
def calculate_inverse():
    pass


# Функция для создания полей ввода матрицы
def create_matrix_entries():
    try:
        n = int(size_entry.get())
        if n < 2 or n > 5:
            messagebox.showerror("Ошибка", "Размер матрицы должен быть от 2 до 5.")
            return
        # Очищаем предыдущие поля ввода
        for widget in matrix_frame.winfo_children():
            widget.destroy()
        global entries
        entries = []
        for i in range(n):
            row_entries = []
            for j in range(n):
                entry = tk.Entry(matrix_frame, width=5, font=("Arial", 13))
                entry.grid(row=i, column=j, padx=2, pady=2)
                row_entries.append(entry)
            entries.append(row_entries)

        # Динамическое изменение размера окна
        root.geometry(f"{300 + n * 50}x{300 + n * 50}")
    except ValueError:
        messagebox.showerror("Ошибка", "Пожалуйста, введите целое число для размера матрицы.")


# Функция для отображения инструкций
def show_instructions():
    instructions = (
        "Инструкция:\n\n"
        "1. Введите размер квадратной матрицы (от 2 до 5).\n"
        "2. Введите элементы матрицы.\n"
        "3. Нажмите 'Найти обратную матрицу'.\n\n"
        "Примечания:\n"
        "- Программа рассчитана на работу с вещественными числами.\n"
        "- Если ввести некорректные данные (например, буквы вместо чисел), "
        "программа выдаст сообщение об ошибке.\n"
        "- Матрицы с нулевым определителем (вырожденные матрицы) не имеют обратной, "
        "и программа сообщит об этом."
    )
    messagebox.showinfo("Инструкция", instructions)


# Создаем главное окно
root = tk.Tk()
root.title("Обращение квадратной матрицы")
root.geometry("500x300")
root.eval('tk::PlaceWindow %s center' % root.winfo_pathname(root.winfo_id()))

# Заголовок программы
title_label = tk.Label(root, text="Обращение квадратной матрицы", font=("Arial", 13, "bold"))
title_label.pack(pady=10)

# Ввод размера матрицы
size_label = tk.Label(root, text="Введите размер матрицы (от 2 до 5):", font=("Arial", 13))
size_label.pack(pady=10)
size_entry = tk.Entry(root, font=("Arial", 13))
size_entry.pack()

size_button = tk.Button(root, text="Создать матрицу", font=("Arial", 13), command=create_matrix_entries)
size_button.pack(pady=5)

# Фрейм для ввода элементов матрицы
matrix_frame = tk.Frame(root)
matrix_frame.pack(pady=10)

# Кнопка для вычисления обратной матрицы
calculate_button = tk.Button(root, text="Найти обратную матрицу", font=("Arial", 13), command=calculate_inverse)
calculate_button.pack(pady=5)

# Кнопка для отображения инструкции
instruction_button = tk.Button(root, text="Инструкция", font=("Arial", 13), command=show_instructions)
instruction_button.pack(pady=5)

root.mainloop()
