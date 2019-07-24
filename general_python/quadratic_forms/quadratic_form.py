import numpy as np
from copy import deepcopy


class QuadraticForm:
    def __init__(self, form_str):
        self.q_form = form_str
        self.q_matrix = deepcopy(self.__get_quadratic_matrix())
        self.is_positive = self.__pos_finite()
        self.is_negative = self.__neg_finite()

    def __get_var_list(self):
        var_list = []
        for c in self.q_form:
            if c.isalpha() and c not in var_list:
                var_list.append(c)
        return var_list

    def __get_quadratic_matrix(self):
        var_list = self.__get_var_list()
        var_dict = dict()
        var_count = len(var_list)
        for i in range(var_count):
            var_dict[var_list[i]] = i

        quadratic_matrix = np.zeros((var_count, var_count))
        sign = '+'
        for sub_str in self.q_form.split():
            if sub_str == '+' or sub_str == '-':
                sign = sub_str
            else:
                if sub_str[0].isalpha():
                    sub_str = '1' + sub_str
                koefficient = int(sub_str[:-2]) / 2
                if sign == '-':
                    koefficient *= -1
                quadratic_matrix[var_dict[sub_str[-2]]][var_dict[sub_str[-1]]] += koefficient
                quadratic_matrix[var_dict[sub_str[-1]]][var_dict[sub_str[-2]]] += koefficient

        return quadratic_matrix

    def __pos_finite(self):
        len_ = len(self.__get_var_list())
        i = 1
        while i <= len_ and np.linalg.det(self.q_matrix[0:i, 0:i]) > 0:
            i += 1
        if i > len_:
            return True
        else:
            return False

    def __neg_finite(self):
        len_ = len(self.__get_var_list())
        i = 1
        while i <= len_:
            minor = np.linalg.det(self.q_matrix[0:i, 0:i])
            if (minor < 0 and i % 2) or (minor > 0 and not i % 2):
                i += 1
            else:
                break
        else:
            return True
        return False


open_file = open("input.txt", "r", encoding="utf-8")
my_form = QuadraticForm(open_file.readline())
open_file.close()
print(my_form.is_negative)
