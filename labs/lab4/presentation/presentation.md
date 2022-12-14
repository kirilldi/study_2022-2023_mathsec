---
## Front matter
lang: ru-RU
title: Защита лабораторной 4
subtitle: по предмету мат. основы защиты информации
author:
  - Дидусь К.В.
institute:
  - Российский университет дружбы народов, Москва, Россия

## i18n babel
babel-lang: russian
babel-otherlangs: english

## Formatting pdf
toc: false
toc-title: Содержание
slide_level: 2
aspectratio: 169
section-titles: true
theme: metropolis
header-includes:
 - \metroset{progressbar=frametitle,sectionpage=progressbar,numbering=fraction}
 - '\makeatletter'
 - '\beamer@ignorenonframefalse'
 - '\makeatother'
---

# Информация

## Докладчик

:::::::::::::: {.columns align=center}
::: {.column width="70%"}

  * Дидусь Кирилл Валерьевич
  * Студент кафедры прикладной информатики и теории вероятностей
  * Российский университет дружбы народов
  * [1132223499@rudn.ru](mailto:1132223499@rudn.ru)
  * <https://github.com/kirilldi/>

:::
::: {.column width="30%"}

![](./image/me.jpg)

:::
::::::::::::::
# Введение

## Актуальность

- Изучение базовых принципов шифрования
- Важность знания основ шифрования для работы в сфере информационных технологий

## Цели и задачи лабораторной

Целью данной лабораторной работы является ознакомление с алгоритмом Евклида, а так же с его реализацей в программном виде.

## Материалы и методы

- ТУИС РУДН
- Язык программировния Python

# Выполнение лабораторной

## Алгоритм Евклида

Алгори́тм Евкли́да — эффективный алгоритм для нахождения наибольшего общего делителя двух целых чисел

![Рис. 1. Суть работы алгоритма](./image/1.png){width="80%"}

## Расширенный алгоритм Евклида

Расширенный алгоритм Евклида — это расширение алгоритма Евклида, которое вычисляет кроме наибольшего общего делителя (НОД) целых чисел a и b ещё и коэффициенты соотношения Безу, то есть целые x и y, такие что
ax+by=НОД(a,b)

![Рис. 2. Пример работы расширенного алгоритма](./image/2.png){width="80%"}

## Бинарный алгоритм Евклида

![Рис. 3. Пример работы расширенного алгоритма](./image/3.png){width="80%"}

## Применение алгоритма

- Шифрование открытым ключом
- Для поиска взаимно-простых чисел

## Вывод

Таким образом, была достигнута цель, поставленная в начале лабораторной работы: я ознакомился с алгоритмом Евклида, а так же мне удалось реализовать вариции этого алгоритма на языке программирования Python.
