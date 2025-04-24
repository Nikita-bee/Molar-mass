import pandas as pd
import matplotlib.pyplot as plt

# Создание DataFrame с элементами и их атомными массами
data = {
    'Element': ['H', 'He', 'Li', 'Be', 'B', 'C', 'N', 'O', 'F', 'Ne',
                'Na', 'Mg', 'Al', 'Si', 'P', 'S', 'Cl', 'Ar', 'K', 'Ca',
                'Sc', 'Ti', 'V', 'Cr', 'Mn', 'Fe', 'Co', 'Ni', 'Cu', 'Zn',
                'Ga', 'Ge', 'As', 'Se', 'Br', 'Kr', 'Rb', 'Sr', 'Y', 'Zr',
                'Nb', 'Mo', 'Tc', 'Ru', 'Rh', 'Pd', 'Ag', 'Cd', 'In', 'Sn',
                'Sb', 'Te', 'I', 'Xe', 'Cs', 'Ba', 'La', 'Ce', 'Pr', 'Nd',
                'Pm', 'Sm', 'Eu', 'Gd', 'Tb', 'Dy', 'Ho', 'Er', 'Tm', 'Yb',
                'Lu', 'Hf', 'Ta', 'W', 'Re', 'Os', 'Ir', 'Pt', 'Au', 'Hg',
                'Tl', 'Pb', 'Bi', 'Po', 'At', 'Rn', 'Fr', 'Ra', 'Ac', 'Th',
                'Pa', 'U', 'Np', 'Pu', 'Am', 'Cm', 'Bk', 'Cf', 'Es', 'Fm',
                'Md', 'No', 'Lr', 'Rf', 'Db', 'Sg', 'Bh', 'Hs', 'Mt', 'Ds',
                'Rg', 'Cn', 'Nh', 'Fl', 'Mc', 'Lv', 'Ts', 'Og'],
    'Atomic Mass': [1.008, 4.0026, 6.94, 9.0122, 10.81, 12.01, 14.01, 16.00, 19.00, 20.18,
                    22.99, 24.31, 26.98, 28.09, 30.97, 32.07, 35.45, 39.95, 39.10, 40.08,
                    44.96, 47.87, 50.94, 51.996, 54.94, 55.85, 58.93, 58.69, 63.55, 65.38,
                    69.72, 72.63, 74.92, 78.97, 79.90, 83.80, 85.47, 87.62, 88.91, 91.22,
                    92.91, 95.95, 98, 101.07, 102.91, 106.42, 107.87, 112.41, 114.82, 118.71,
                    121.76, 127.60, 126.90, 131.29, 132.91, 137.33, 138.91, 140.12, 140.91, 144.24,
                    145, 150.36, 151.96, 157.25, 158.93, 162.50, 164.93, 167.26, 168.93, 173.04,
                    174.97, 178.49, 180.95, 183.84, 186.21, 190.23, 192.22, 195.08, 196.97, 200.59,
                    204.38, 207.2, 208.98, 209, 210, 222, 223, 226, 227, 232.04,
                    231.04, 238.03, 237, 244, 243, 247, 247, 251, 252, 257,
                    258, 259, 262, 267, 270, 271, 270, 277, 276, 281,
                    282, 285, 286, 289, 290, 293, 294, 294, 294, 294]
}

elements_df = pd.DataFrame(data)

# Определение молекулярных формул
molecular_formulas = {
    'Water': {'H': 2, 'O': 1},
    'Carbon Dioxide': {'C': 1, 'O': 2},
    'Glucose': {'C': 6, 'H': 12, 'O': 6}
}

# Функция для расчета молярной массы
def calculate_molar_mass(formula):
    molar_mass = 0
    for element, count in formula.items():
        atomic_mass = elements_df.loc[elements_df['Element'] == element, 'Atomic Mass'].values[0]
        molar_mass += atomic_mass * count
    return molar_mass

# Расчет молярной массы для каждой формулы
molar_masses = {compound: calculate_molar_mass(formula) for compound, formula in molecular_formulas.items()}

# Вывод результатов
for compound, mass in molar_masses.items():
    print(f"Молярная масса {compound}: {mass:.2f} г/моль")

# Визуализация результатов
plt.bar(molar_masses.keys(), molar_masses.values())
plt.xlabel('Соединения')
plt.ylabel('Молярная масса (г/моль)')
plt.title('Молярные массы различных соединений')
plt.show()