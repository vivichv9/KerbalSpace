# Програмная реализация проекта `"Сокол-С"`

## Ссылка на основной документ(отчет) - [:link:**_кликабельно_**:link:](https://docs.google.com/document/d/1I_B56GtqnuqOBQSlZflkZxK7ye1y5Lk2k9WJtWd6Uoo/edit#)

---

## I Часть:

### + **MathModel.py**

#### В данном файле происходит предварительный расчет скорости, времени, высоты за каждую секунду полета.

#### Далее мы переходим к выгрузке данных из симулятора "Kerbal Space Program" для сравнения с произведенными нами расчетами. Данные выгружаются в формате `.csv` и содержат в себе следующие данные:

`Time, Velocity,	GForce,	Acceleration, Thrust, TWR, Mass, AltitudeFromTerrain, AltitudeFromSea,	DownrangeDistance,	Latitude,	Longitude,	Apoapsis,	Periapsis,	Inclination,	OrbitalVelocity,	TargetDistance,	TargetVelocity,	StageDeltaV,	VesselDeltaV,	Pressure`

Количество выгружаемых данных - 21

## II Часть:

### :white_circle: **Csvparse.py**

#### Здесь мы обрабатываем полученный `csv` файл.

#### В результате получаем 1 двумерный список, состоящий из 21-го одномерного.

### :white_circle: **parse_data.py**

#### Этот файл отвечает за обработку полученного двумерного массива.

#### Он разбивает его на 21 одномерный по столбцам.

#### **_Пример:_**

    Input:                            Output:
    [[1, 2, 3, 4],                    [1, 5, 9, 4]
    [5, 6, 7, 8],                     [2, 6, 1, 5]
    [9, 1, 2, 3],                     [3, 7, 2, 6]
    [4, 5, 6, 7]]                     [4, 8, 3, 7]
