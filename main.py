import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import xlrd
import openpyxl

#zad1
# x = np.arange(0, 21, 1)
# y = (1/x)
# plt.plot(x, y, label='f(x)')
# plt.xlabel('x')
# plt.ylabel('f(x)')
# plt.ylim(0, 1)
# plt.xlim(1, len(x))
# plt.legend()
# plt.show()

# zad2
# x = np.arange(0, 21, 1)
# y = (1/x)
# plt.plot(x, y, 'g>:', label='f(x) = 1/x')
# plt.xlabel('x')
# plt.ylabel('f(x)')
# plt.ylim(0, 1)
# plt.xlim(0, len(x))
# plt.legend()
# plt.show()

# zad3
# x = np.arange(0, 30, 0.1)
# f = (np.sin(x))
# g = np.cos(x)
# plt.plot(x, f, x, g)
# plt.legend(['sin(x)', 'cos(x)'], loc='upper right')
# plt.yticks(np.arange(-1, 2, step=0.5))
# plt.xlabel('x')
# plt.ylabel('wartości sin(x) i cos(x)')
# plt.show()

# zad4
# x = np.arange(0, 30, 0.1)
# f = np.sin(x)+2
# g = -(np.sin(x))
# plt.plot(x, f, x, g)
# plt.yticks(np.arange(-1, 3.5, step=0.5))
# plt.xlabel('x')
# plt.ylabel('sin(x)')
# plt.title('Wykres sin(x), sin(x)')
# plt.legend(['sin(x)', 'sin(x)'], loc='center left')
# plt.show()


# zad6
# excel = pd.ExcelFile('imiona.xlsx')
# df = pd.read_excel(excel, header=0)
# print(df)
#
# grupa1 = df.groupby(['Plec']).agg({'Liczba':['sum']})
# wykres = grupa1.plot.bar()
# plt.xlabel("Płeć")
# plt.ylabel("Liczba")
# plt.xticks(rotation=0)
#plt.show()