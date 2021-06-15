import math

shapesDict = {
    'Круг': 1,
    'Треугольник': 2,
    'Прямоугольник': 3
}

roundArea = int()
triArea = int()
rectArea = int()

print('Введите тип фигуры:')
shape = input()

if shapesDict.get(shape) == 1:
    print('Введите радиус круга:')
    radius = int(input())
    roundArea = round(math.pi * radius * radius, 2)
    print(f'Площадь круга: {roundArea}')
elif shapesDict.get(shape) == 2:
    print('Введите длину стороны A:')
    triA = int(input())
    print('Введите длину стороны B:')
    triB = int(input())
    print('Введите длину стороны C:')
    triC = int(input())
    halfPer = (triA + triB + triC) / 2
    triArea = round((halfPer * (halfPer - triA) * (halfPer - triB) * (halfPer - triC)) ** 0.5, 2)
    print(f'Площадь треугольника: {triArea}')
elif shapesDict.get(shape) == 3:
    print('Введите длину стороны A:')
    rectA = int(input())
    print('Введите длину стороны B:')
    rectB = int(input())
    rectArea = rectA * rectB
    print(f'Площадь прямоугольника: {rectArea}')
