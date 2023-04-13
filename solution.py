import pandas as pd
import numpy as np
from scipy.stats import permutation_test

chat_id = 457863109 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool: # Одна или две выборке на входе, заполняется исходя из условия
    def statistic(x, y, axis):
        return np.mean(y, axis=axis) - np.mean(x, axis=axis)
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    alpha = 0.02
    statisticfloat, pvaluefloat, null_distributionndarray = permutation_test((y, x), statistic, vectorized=True, n_resamples=np.inf, alternative='less')
    return pvaluefloat < alpha # Ваш ответ, True или False
