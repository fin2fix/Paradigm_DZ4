# ДЗ #4
# Написать скрипт для расчета корреляции Пирсона между двумя случайными величинами (двумя массивами).
# Можете использовать любую парадигму, но рекомендую использовать функциональную,
# т.к. в этом примере она значительно упростит вам жизнь.

from statistics import correlation, mean
from numpy import corrcoef
from math import sqrt

x = [11, 2, 7, 4, 15, 6, 10, 8, 9, 1, 11, 5, 13, 6, 15]
y = [2, 5, 17, 6, 10, 8, 13, 4, 6, 9, 11, 2, 5, 4, 7]


# Первый вариант (код с использованием функциональной парадигмы)
def pearsons(xList: list, yList: list):
    Mx = mean(xList)
    My = mean(yList)

    def numerator():
        xResults = list(map(lambda x: x - Mx, xList))
        yResults = list(map(lambda y: y - My, yList))
        return sum(map(lambda x, y: x * y, xResults, yResults))

    def denominator():
        return sqrt(
            sum(map(lambda x: (x - Mx) ** 2, xList))
            * sum(map(lambda y: (y - My) ** 2, yList))
        )

    return numerator() / denominator()


print(
    "\n 1st variant (full) - The pearson's coeffient of the x and y inputs are: \n",
    "%.8f" % pearsons(x, y),
)


# Второй вариант (с использованием статистических функций из Statistics)
pearsons_coeff2 = correlation(x, y)
print(
    "\n 2nd variant (Statistics) - The pearson's coeffient of the x and y inputs are: \n",
    "%.8f" % pearsons_coeff2,
)


# Третий вариант (с использованием пакета NumPy для научных вычислений на Python)
pearsons_coeff3 = corrcoef(x, y)
print(
    "\n 3d variant (NumPy) - The pearson's coeffient of the x and y inputs are: \n",
    pearsons_coeff3,
)
