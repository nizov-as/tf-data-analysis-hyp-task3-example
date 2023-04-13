import pandas as pd
import numpy as np
from statsmodels.stats.weightstats import ztest

chat_id = 457863109 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool: # Одна или две выборке на входе, заполняется исходя из условия
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    alpha = 0.02
    tstat, pvalue = ztest(y, x, 0, alternative='smaller')
    return pvalue < alpha # Ваш ответ, True или False
