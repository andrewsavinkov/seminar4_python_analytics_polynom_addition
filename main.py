# A. Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100)
# многочлена и записать в файл многочлен степени k
# Пример:
# если k = 2, то многочлены могут быть => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
# B. Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.
# НЕОБЯЗАТЕЛЬНОЕ, ДОПОЛНИТЕЛЬНОЕ ЗАДАНИЕ:
# Расширить значение коэффициентов до [-100..100]
from random import randint

def koefs():
    power = int(input('Введите натуральную степень: \t'))
    koef_list = []
    koef_list.append(randint(1, 100))        # старший член многочлена точно не равен 0
    for i in range(1, power+1):
        koef_list.append(randint(0, 100))
    return koef_list

def create_polynom(koeficients, file):
    poly=[]
    for i in range(len(koeficients)):
        if not koeficients[i]:
            poly.append('')
        elif i==len(koeficients)-1:
            poly.append(str(koeficients[i]))
        elif koeficients[i]==1:
            poly.append(f'x^{len(koeficients)-i-1}')
        elif i==len(koeficients)-2:
            poly.append(f'{str(koeficients[i])}x')
        else:
            poly.append(f'{str(koeficients[i])}x^{len(koeficients)-i-1}')
    remove_empty(poly)
    poly='+'.join(poly)
    with open(file, 'a', encoding="utf-8") as f:
        f.write(poly)
        f.write('\n')
    return poly

def remove_empty(poly):     #удаляем пустые значения
    while '' in poly:
        poly.remove('')

def poly_split_elements(some_poly):
    resulting_list=[]
    splitted_poly=some_poly.split('+')
    for i in range(len(splitted_poly)-2):
        if splitted_poly[i][0]=='x':
            kf=1
            pow = int(splitted_poly[i].split('^')[1])
        else:
            kf=int(splitted_poly[i].split('x^')[0])
            pow = int(splitted_poly[i].split('^')[1])
        resulting_list.append((kf, pow))
    resulting_list.append((int(splitted_poly[len(splitted_poly)-2].split('x')[0]), 1))
    resulting_list.append((int(splitted_poly[len(splitted_poly)-1][0]), 0))
    return resulting_list

def poly_sum(poly1, poly2):
    res_poly=[]
    res_koefs=[]
    file_sum='sum.txt'
    spl_pol1=poly_split_elements(poly1)
    spl_pol2= poly_split_elements(poly2)
    from_poly_one = 0
    from_poly_two = 0
    print(spl_pol1)
    print(spl_pol2)

    if spl_pol1[0][1]>spl_pol2[0][1]:
        max_power=spl_pol1[0][1]
    else:
        max_power=spl_pol2[0][1]
    for i in range(max_power+1):
        for j in range(len(spl_pol1)):
            if spl_pol1[j][1] == max_power-i:
                from_poly_one=spl_pol1[j][0]

        for k in range(len(poly_split_elements(poly2))):
            if poly_split_elements(poly2)[k][1] == max_power - i:
                from_poly_two = poly_split_elements(poly2)[k][0]

        res_poly.append((from_poly_one+from_poly_two, max_power-i))

    for i in range(len(res_poly)):
        res_koefs.append(res_poly[i][0])
    create_polynom(res_koefs, file_sum)
#
#
#
#
file1='poly1.txt'
file2='poly2.txt'
koef1=koefs()
koef2=koefs()
some_pol=create_polynom(koef1, file1)
some_pol2=create_polynom(koef2, file2)
poly_sum(some_pol, some_pol2)

