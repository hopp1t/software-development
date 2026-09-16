import numpy as np

class MatrixLab:
    def __init__(self):
        self.my_array = None

    def step_1_create_array(self):
        print("\n--- Шаг 1. Создание массива ---")  
        self.my_array = np.arange(10, 70, 2)
        print("Массив my_array:")
        print(self.my_array)

    def run(self):
        self.step_1_create_array()

if __name__ == "__main__":
    lab = MatrixLab()
    lab.run()
