---
## Front matter
title: "Отчет по лабораторной работе 6"
subtitle: "По предмету мат. основы защиты информации"
author: 
- "Студент: Дидусь Кирилл Валерьевич, 1132223499"
- "Группа: НПМмд-02-22"
- "Преподаватель: Кулябов Дмитрий Сергеевич,"
- "д-р.ф.-м.н., проф."
date: "Москва, 2022"

## Generic otions
lang: ru-RU
toc-title: "Содержание"

## Bibliography
bibliography: bib/cite.bib
csl: pandoc/csl/gost-r-7-0-5-2008-numeric.csl

## Pdf output format
toc: true # Table of contents
toc-depth: 2
lof: true # List of figures
lot: true # List of tables
fontsize: 12pt
linestretch: 1.5
papersize: a4
documentclass: scrreprt
## I18n polyglossia
polyglossia-lang:
  name: russian
  options:
	- spelling=modern
	- babelshorthands=true
polyglossia-otherlangs:
  name: english
## I18n babel
babel-lang: russian
babel-otherlangs: english
## Fonts
mainfont: PT Serif
romanfont: PT Serif
sansfont: PT Sans
monofont: PT Mono
mainfontoptions: Ligatures=TeX
romanfontoptions: Ligatures=TeX
sansfontoptions: Ligatures=TeX,Scale=MatchLowercase
monofontoptions: Scale=MatchLowercase,Scale=0.9
## Biblatex
biblatex: true
biblio-style: "gost-numeric"
biblatexoptions:
  - parentracker=true
  - backend=biber
  - hyperref=auto
  - language=auto
  - autolang=other*
  - citestyle=gost-numeric
## Pandoc-crossref LaTeX customization
figureTitle: "Рис."
tableTitle: "Таблица"
listingTitle: "Листинг"
lofTitle: "Список иллюстраций"
lotTitle: "Список таблиц"
lolTitle: "Листинги"
## Misc options
indent: true
header-includes:
  - \usepackage{indentfirst}
  - \usepackage{float} # keep figures where there are in the text
  - \floatplacement{figure}{H} # keep figures where there are in the text
---

# Цель работы

Целью данной лабораторной работы является ознакомление с алгоритмом по разложению числа на множители.

# Задание

Реализовать алгоритм для разложения заданного числа на 2 нетривиальных сомножителя.

# Выполнение лабораторной работы

В ходе выполнения лабораторной работы было реализован алгоритм для разложения заданного числа на 2 нетривиальных сомножителя. Он реализует p-метод Полларда. 

 Программный код представлен в качестве листинга в конце отчета.

# Выводы

Таким образом, была достигнута цель, поставленная в начале лабораторной работы: я ознакомился с алгоритмом для разложения заданного числа на 2 нетривиальных сомножителя, а так же мне удалось реализовать его на языке программирования Python.

# Листинг программы

``` python
import math

def p_pollard(n,c,func):
    a = c 
    b = func(c,n)
    count = 0
    while(True):
        a = func(a,n)
        b = func(b,n)
        d = math.gcd(a-b,n) #НОД
        count += 1
        if((d > 1) & (d < n)):
            return d
        elif(d == n): 
            return "делитель не найден"
        if(count>100):
            return "ошибка вычисления"

def func(x,n):
    return (x**2 + 5)%n

print(p_pollard(133,1,func))
``` 