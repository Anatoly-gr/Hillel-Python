# 3. Написать функцию которая вернет площадь фигуры: по-умолчанию треугольника, опционально квадрата.
# На входе 2 величины и параметр типа фигуры.
def figure_area(x, y, z=1):
    if z == 2:
        return x ** 2
    else:
        return x * y * 0.5


figure_type = int(input('Ведите тип фигуры 1-треугольник, 2-квадрат '))
if figure_type == 1:
    h_tri = float(input('Введите высоту треугольника '))
    side_tri = float(input('Введите сторону треугольника '))
    print(f'Площадь треугольника = {figure_area(h_tri, side_tri)}')

if figure_type == 2:
    side_square = float(input('Введите сторону квадрата '))
    print(f'Площадь квадрата = {figure_area(side_square, side_square, figure_type)}')
