import numpy as np

class MatrixLab:
    def __init__(self):
        self.my_array = None
        self.A = None

    def create_array(self):
        print("\n--- Шаг 1. Создание массива ---")  
        self.my_array = np.arange(10, 70, 2)
        print("Массив my_array:")
        print(self.my_array)

    def form_matrix_A(self):
        print("\n--- Шаг 2. Формирование матрицы A ---")
        self.A = self.my_array.reshape(6, 5).T
        print(f"Размерность матрицы A: {self.A.shape}")
        print("Матрица A:")
        print(self.A)

    def transform_A(self):
        print("\n--- Шаг 3. Преобразование элементов A ---")
        self.A = self.A * 2.5 - 5
        print("Преобразованная матрица A:")
        print(self.A)
        print(f"Минимальный элемент в матрице A: {self.A.min()}")

    def run(self):
        self.create_array()
        self.form_matrix_A()
        self.transform_A()

if __name__ == "__main__":
    lab = MatrixLab()
    lab.run()
