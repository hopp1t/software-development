import numpy as np

class MatrixLab:
    def __init__(self):
        self.my_array = None
        self.A = None
        self.B = None
        self.a_vec = None 
        self.b_vec = None
        self.AB = None

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

    def create_matrix_B(self):
        print("\n--- Шаг 4. Создание матрицы B ---")
        np.random.seed(1611)
        self.B = np.random.randint(0, 11, (6, 3))
        print(f"Размерность матрицы B: {self.B.shape}")
        print("Матрица B: ")
        print(self.B)

    def sum_vectors(self):
        print("\n--- Шаг 5. Векторы сумм ---")
        self.a_vec = self.A.sum(axis=1)
        self.b_vec = self.B.sum(axis=0)
        
        print(f"Вектор a (суммы строк A), размер {self.a_vec.shape}:")
        print(self.a_vec)
        print(f"Вектор b (суммы столбцов B), размер {self.b_vec.shape}:")
        print(self.b_vec)

    def matrix_multiplication(self):
        print("\n--- Шаг 6. Умножение матриц ---")
        self.AB = self.A @ self.B
        print(f"Размерность произведения A * B: {self.AB.shape}")
        print("Результат произведения A * B:")
        print(self.AB)

    def run(self):
        self.create_array()
        self.form_matrix_A()
        self.transform_A()
        self.create_matrix_B()
        self.sum_vectors()
        self.matrix_multiplication()

if __name__ == "__main__":
    lab = MatrixLab()
    lab.run()
