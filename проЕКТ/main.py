import pandas as pd
import matplotlib.pyplot as plt
import re

def load_atomic_masses(filename='Книга2.xlsx'):
    df = pd.read_excel(filename)
    # Предполагаем, что в таблице есть столбцы "Element" и "AtomicMass"
    atomic_masses = pd.Series(df.AtomicMass.values, index=df.Element).to_dict()
    return atomic_masses

def parse_formula(formula):
    pattern = r'([A-Z][a-z]?)(\d*)'
    matches = re.findall(pattern, formula)
    composition = {}
    for elem, count in matches:
        count = int(count) if count else 1
        composition[elem] = composition.get(elem, 0) + count
    return composition

def calculate_molar_mass(composition, atomic_masses):
    mass = 0.0
    for elem, count in composition.items():
        if elem not in atomic_masses:
            raise ValueError(f"Элемент '{elem}' не найден в таблице атомных масс.")
        mass += atomic_masses[elem] * count
    return mass

def plot_composition(composition, atomic_masses):
    labels = []
    sizes = []
    for elem, count in composition.items():
        labels.append(elem)
        sizes.append(atomic_masses[elem] * count)
    fig, ax = plt.subplots()
    ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
    ax.axis('equal')
    plt.title('Вклад элементов в молярную массу')
    plt.show()

def main():
    print("Загрузка атомных масс из файла «Книга1.xlsx» ...")
    atomic_masses = load_atomic_masses()
    formula = input("Введите химическую формулу вещества (например, H2O, C6H12O6): ")
    try:
        composition = parse_formula(formula)
        molar_mass = calculate_molar_mass(composition, atomic_masses)
        print(f"Молярная масса вещества {formula}: {molar_mass:.3f} г/моль")
        plot_composition(composition, atomic_masses)
    except ValueError as e:
        print("Ошибка:", e)

if __name__ == '__main__':
    main()
