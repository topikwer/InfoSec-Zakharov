import random
from collections import Counter
import matplotlib.pyplot as plt
def format_time(seconds):
    if seconds < 1:
        return f"{seconds * 1000:.2f} миллисекунд"
    elif seconds < 60:
        return f"{seconds:.2f} секунд"
    elif seconds < 3600:
        return f"{seconds / 60:.2f} минут"
    elif seconds < 86400:
        return f"{seconds / 3600:.2f} часов"
    elif seconds < 31536000:
        return f"{seconds / 86400:.2f} дней"
    else:
        return f"{seconds / 31536000:.2f} лет"
def generate_password(x):
    alfavit = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    pasword = ''.join(random.choices(alfavit, k=x))
    return pasword
def distribution_check(password):
    counter = Counter(password)
    print()
    print(counter)
    sorted_chars = sorted(counter.keys())
    sorted_freqs = [counter[char] for char in sorted_chars]
    plt.figure(figsize=(10, 6))
    plt.bar(range(len(sorted_chars)), sorted_freqs, alpha=0.7)
    plt.xlabel('Символ')
    plt.ylabel('Частота')
    plt.title(f'Распределение символов в пароле (длина={len(password)})')
    plt.xticks(range(len(sorted_chars)), sorted_chars, rotation=90)
    plt.grid(axis='y', alpha=0.3)
    plt.tight_layout()
    plt.show()
def time_check(x, alphavit=33, speed=1e9):
    combination = alphavit ** x
    average_attemts = combination / 2
    time_seconds = average_attemts / speed
    return time_seconds
def shedule_check(max_lenth: int = 15):
    times = []
    lenths = []
    for i in range(1, max_lenth + 1):
        lenths.append(i)
        t = time_check(i)
        times.append(t)
    plt.plot(lenths, times, marker='o')
    plt.yscale('log')
    plt.xlabel('Длина пароля')
    plt.ylabel('Время подбора (секунды)')
    plt.title('Зависимость времени подбора от длины пароля')
    plt.grid(True)
    plt.show()
def recomendation(length: int, info_value: str = 'средняя',
                  speed: float = 1e9, alphabet_power: int = 33) -> None:
    required_years = {
        'низкая': 0.1,
        'средняя': 1,
        'высокая': 100,
        'критическая': 10000,
    }
    years = required_years.get(info_value, 1)
    required_seconds = years * 365 * 24 * 3600
    current_seconds = (alphabet_power ** length / 2) / speed
    min_length = 1
    while (alphabet_power ** min_length / 2) / speed < required_seconds:
        min_length += 1
    print("\n=== РЕКОМЕНДАЦИИ ===")
    print(f"Алфавит: русские строчные буквы, мощность = {alphabet_power}")
    print(f"Ценность информации: {info_value} (нужный срок стойкости: {years} лет)")
    print(f"Скорость атакующего: {speed:.0e} попыток/сек")
    print(f"Длина пароля: {length} -> время подбора: {format_time(current_seconds)}")
    print(f"Минимально необходимая длина: {min_length} символов")
    if length >= min_length:
        print("Вывод: пароль достаточной стойкости")
    else:
        print(f"Вывод: пароль СЛАБЫЙ! Увеличьте длину минимум до {min_length} символов")
    print("\nПрактические советы:")
    print(" - генерируйте пароль случайно, без слов и дат;")
    print(" - меняйте пароль раз в 3-6 месяцев;")
    print(" - не используйте один пароль на разных сервисах;")
    print(" - храните пароли в менеджере паролей;")
    print(" - включайте двухфакторную аутентификацию.")
def main():
    length = int(input("Введите длину пароля: "))
    password = generate_password(length)
    print(f"Сгенерированный пароль: {password}")
    distribution_check(password)
    seconds = time_check(length)
    print(f"Среднее время подбора: {format_time(seconds)}")
    shedule_check(max(length, 15))
    recomendation(length)


if __name__ == '__main__':
    main()