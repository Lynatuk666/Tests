def discriminant(a, b, c):
    """
    функция для нахождения дискриминанта
    """
    Dis = b**2 - 4 * a * c
    return Dis
def solution(a, b, c):
    """
    функция для нахождения корней уравнения
    """
    if discriminant(a, b, c) > 0:
      return(f'{(-(b) + (discriminant(a, b, c) ** 0.5)) / (2 * a)} {(-(b) - (discriminant(a, b, c) ** 0.5)) / (2 * a)}')
    elif discriminant(a, b, c) < 0:
      return(f'корней нет')
    elif discriminant(a, b, c) == 0:
      return(f'{(-(b))/(2 * a)}')
if __name__ == '__main__':
    print(solution(1, 8, 15))
    print(solution(1, -13, 12))
    print(solution(-4, 28, -49))
    print(solution(1, 1, 1))