# Длина маршрута велоралли "100 километров за 10 часов по Поясу Славы" - примерно 100 километров.
# Велосипедист Вася стартует с нулевого километра маршрута и едет со скоростью `v` километров в час.
# На какой отметке он остановится через `t` часов?
v = int(input('Введите скорость велосипедиста Васи v = '))
t = int(input('Введите время в пути велосипедиста Васи t = '))
if v > 0:
    print('Вяся движется по маршруту в прямом направлении', 'Через время t = ', t,
          'Вася будет на отметке ', v / t)
else:
    print('Вася движется по маршруту в обратном направлении', 'Через время t = ', t,
          'Вася будет на отметке ', int(abs(v / t))
          )
