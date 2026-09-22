import numpy as np
import os

class MatrixLab:
    def __init__(self):
        self.my_array = None
        self.A = None
        self.B = None
        self.a_vec = None 
        self.b_vec = None
        self.AB = None
        self.A_sq = None
        self.B_sq = None
        self.inv_A = None
        self.inv_B = None

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

    def make_square(self):
        print("\n--- Шаг 7. Приведение к квадратному виду ---")
        self.A_sq = np.delete(self.A, 2, axis=1)
        
        new_columns = np.random.randint(10, 21, (6, 3))
        self.B_sq = np.hstack((self.B, new_columns))
        
        print(f"Новый размер матрицы A: {self.A_sq.shape}")
        print("Квадратная матрица A:")
        print(self.A_sq)
        print(f"Новый размер матрицы B: {self.B_sq.shape}")
        print("Квадратная матрица B:")
        print(self.B_sq)

    def determinants_and_inverses(self):
        print("\n--- Шаг 8. Определители и обратные матрицы ---")
        det_A = np.linalg.det(self.A_sq)
        det_B = np.linalg.det(self.B_sq)
        print(f"Определитель матрицы A: {det_A:.4f}")
        print(f"Определитель матрицы B: {det_B:.4f}")

        try:
            if np.abs(det_A) < 1e-9:
                raise np.linalg.LinAlgError("Матрица вырождена.")
            self.inv_A = np.linalg.inv(self.A_sq)
            print("Обратная матрица для A успешно найдена.")
        except np.linalg.LinAlgError:
            print("Обратная матрица для A не существует, так как матрица вырождена.")

        try:
            if np.abs(det_B) < 1e-9:
                raise np.linalg.LinAlgError("Матрица вырождена.")
            self.inv_B = np.linalg.inv(self.B_sq)
            print("Обратная матрица для B успешно найдена.")
        except np.linalg.LinAlgError:
            print("Обратная матрица для B не существует, так как матрица вырождена.")

    def matrix_power(self):
        print("\n--- Шаг 9. Возведение в степень ---")
        self.A_sq_pow = np.linalg.matrix_power(self.A_sq, 6)
        self.B_sq_pow = np.linalg.matrix_power(self.B_sq, 14)
        
        print(f"Размер A в 6-й степени: {self.A_sq_pow.shape}")
        print("Первые 2 строки и 2 столбца матрицы A^6:")
        print(self.A_sq_pow[:2, :2])
        
        print(f"Размер B в 14-й степени: {self.B_sq_pow.shape}")
        print("Первые 2 строки и 2 столбца матрицы B^14:")
        print(self.B_sq_pow[:2, :2])

    def solve_system(self):
        print("\n--- Шаг 10. Решение системы уравнений ---")
        M = np.array([
            [2.3, -3.4,   0.0, -12.0],
            [2.6,  8.4,   0.0,  -6.0],
            [1.3,  4.5, -17.0,   2.0],
            [1.8,  0.0,  15.0,  16.0]
        ])
        V = np.array([-14.0, 0.4, -3.6, 17.4])

        X = np.linalg.solve(M, V)
        print("Полученное решение системы для Варианта 4 (x1, x2, x3, x4):")
        print(X)

        residual = M @ X - V
        residual_norm = np.linalg.norm(residual)
        print(f"Норма невязки: {residual_norm:.4e}")
        print("Невязка близка к нулю:", np.isclose(residual_norm, 0.0, atol=1e-10))

    def additional_analysis(self):
        print("\n--- Шаг 11. Дополнительный анализ матриц (после шага 9) ---")
        rank_A = np.linalg.matrix_rank(self.A_sq_pow)
        rank_B = np.linalg.matrix_rank(self.B_sq_pow)
        print(f"Ранг матрицы A: {rank_A}, Ранг матрицы B: {rank_B}")

        print(f"Среднее элементов A: {self.A_sq_pow.mean():.4e}")
        print(f"Среднее элементов B: {self.B_sq_pow.mean():.4e}")

        cov_A = np.cov(self.A_sq_pow)
        print(f"Размер ковариационной матрицы A: {cov_A.shape}")

        max_idx_flat = np.argmax(self.A_sq_pow)
        row_max, col_max = divmod(max_idx_flat, self.A_sq_pow.shape[1])
        print(f"Индексы макс. элемента в A: строка {row_max}, столбец {col_max}")

        B_flat = self.B_sq_pow.flatten()
        print(f"Размерность одномерного вектора из матрицы B: {B_flat.shape}")

    def save_and_load(self):
        print("\n--- Шаг 12. Сохранение и загрузка матриц ---")
        file_A = "matrix_A.csv"
        file_B = "matrix_B.csv"

        np.savetxt(file_A, self.A_sq_pow, delimiter=",")
        np.savetxt(file_B, self.B_sq_pow, delimiter=",")
        print("Матрицы успешно сохранены в файлы.")

        loaded_A = np.loadtxt(file_A, delimiter=",")
        loaded_B = np.loadtxt(file_B, delimiter=",")

        max_diff_A = np.max(np.abs(self.A_sq_pow - loaded_A))
        max_diff_B = np.max(np.abs(self.B_sq_pow - loaded_B))
        print(f"Максимальная разность для матрицы A: {max_diff_A}")
        print(f"Максимальная разность для матрицы B: {max_diff_B}")

        if os.path.exists(file_A): os.remove(file_A)
        if os.path.exists(file_B): os.remove(file_B)

    def run(self):
        self.create_array()
        self.form_matrix_A()
        self.transform_A()
        self.create_matrix_B()
        self.sum_vectors()
        self.matrix_multiplication()
        self.make_square()
        self.determinants_and_inverses()
        self.matrix_power()
        self.solve_system()
        self.additional_analysis()
        self.save_and_load()

if __name__ == "__main__":
    lab = MatrixLab()
    lab.run()
