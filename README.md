# Програмная реализация проекта `"Сокол-С"`

## Ссылка на основной документ(отчет) - [:link:**_кликабельно_**:link:](https://drive.google.com/drive/folders/1tzqJS5CrVNDyZwkM-oI2SHfHYNAkCa-8)

## I Часть:

### + **MathModel.py**

#### В данном файле происходит предварительный расчет скорости, времени, высоты за каждую секунду полета.

#### Далее мы переходим к выгрузке данных из симулятора "Kerbal Space Program" для сравнения с произведенными нами расчетами. Данные выгружаются в формате `.csv` и содержат в себе следующие данные:

`Time, Velocity, GForce, Acceleration, Thrust, TWR, Mass, AltitudeFromTerrain, AltitudeFromSea, DownrangeDistance, Latitude, Longitude, Apoapsis, Periapsis, Inclination, OrbitalVelocity, TargetDistance, TargetVelocity, StageDeltaV, VesselDeltaV, Pressure`

Количество выгружаемых данных - 21

## II Часть:

### :shipit: **Csvparse.py**

#### Здесь мы обрабатываем полученный `csv` файл.

#### В результате получаем 1 двумерный список, состоящий из 21-го одномерного.

### :shipit: **parse_data.py**

#### Этот файл отвечает за обработку полученного двумерного списка.

#### Он разбивает его на 21 одномерный по столбцам.

#### **_Пример:_**

    Input:                            Output:
    [[1, 2, 3, 4],                    [1, 5, 9, 4]
    [5, 6, 7, 8],                     [2, 6, 1, 5]
    [9, 1, 2, 3],                     [3, 7, 2, 6]
    [4, 5, 6, 7]]                     [4, 8, 3, 7]

## III Часть:

### Обработка списка и построение графиков.

### :shipit: **CreateGraphs.py**

Здесь происходят необходимые математические операции и построения графиков.
С помощью библиотек `NumPy` и `MatPlotLib` мы передаем полученные ранее списки в функции этих библиотек.

### :shipit: **main.py**

В основном файле происходят вызовы всех необходимых функций и методов для работы программы.

---

## **Итог работы:**

Полный вывод был сформулирован в [:link:**_отчёте_**:link:](https://drive.google.com/drive/folders/1tzqJS5CrVNDyZwkM-oI2SHfHYNAkCa-8).

А здесь представлены результаты работы программы:
![](https://i.imgur.com/hUNDGy9.png)
![](https://i.imgur.com/QqhWYOQ.png)
![](https://i.imgur.com/x28QJlH.png)
![](https://i.imgur.com/mxWdvQK.png)
![](https://i.imgur.com/JQMnPaU.png)
![](https://i.imgur.com/19DIPa2.png)
