import string
import random
import time
from collections import Counter  # для подсчета частот
from itertools import combinations

import matplotlib.pyplot as plt  # для построения графика

def format_time(seconds):
    if seconds < 1:
        return f"{seconds * 1000:.2f} миллисекунд"
    elif seconds < 60:
        return f"{seconds:.2f} секунд"
    elif seconds < 3600:
        return f"{seconds / 60:.2f} минут"
    elif seconds < 86400: # 24 часа * 60 минут * 60 секунд
        return f"{seconds / 3600:.2f} часов"
    elif seconds < 31536000: # 365 дней
        return f"{seconds / 86400:.2f} дней"
    else:
        return f"{seconds / 31536000:.2f} лет"

def generate_password(x):
    alfavit='абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    pasword=''.join(random.choices(alfavit,k=x))
    return pasword
def distribution_check(x):
    password=generate_password(x)
    counter=Counter(password)
    print()
    print(counter)
    sorted_chars = sorted(counter.keys())
    sorted_freqs = [counter[char] for char in sorted_chars]
    plt.figure(figsize=(10, 6))  # Размер фигуры
    plt.bar(range(len(sorted_chars)), sorted_freqs, alpha=0.7)
    plt.xlabel('Символ')
    plt.ylabel('Частота')
    plt.title(f'Распределение символов в пароле (длина={len(password)})')
    plt.xticks(range(len(sorted_chars)), sorted_chars, rotation=90)
    plt.grid(axis='y', alpha=0.3)
    plt.tight_layout()
    plt.show()
def time_check(x, alphavit=32, speed=1e9):
    combination = alphavit ** x
    average_attemts= combination / 2
    time_seconds = average_attemts/speed
    answer = format_time(time_seconds)
    return answer

def shedule_check(lenth: int, ):

def recomendation():
    pass

def main():
    print('Введите длинну пароля')
    x = int(input())
    pasword=generate_password(x)
    print(f'сгенерерованный пароль: {pasword}')
if __name__ == '__main__':
    main()
