# MIDItesla
MIDI Tesla Coil Controller

Программно-аппаратный проект музыкальной катушки Тесла построенной по топологии SSTC полумост. Состоит из непосредсвенно катушки Тесла, MIDI-контроллера состоящего из прерывателя bsvi на Atmega8 и микрокомпьютера Raspberry Pi 3B генерирующего MIDI мелодии.

<img src="https://github.com/sergey12malyshev/MIDItesla//raw/master/images/1677242053874.jpg" width=18% height=18%> <img src="https://github.com/sergey12malyshev/MIDItesla//raw/master/images/1677242053886.jpg" width=18% height=18%> 

<img src="https://github.com/sergey12malyshev/MIDItesla//raw/master/images/1677241838375.jpg" width=19% height=19%> <img src="https://github.com/sergey12malyshev/MIDItesla//raw/master/images/1677241838365.jpg" width=20% height=20%>

## Программная реализация (Software) ##
Представляет собой python-скрипты выполняющиеся на Raspberry Pi B3:
* **MainMidi.py** - python скрипт генерирующий MIDI последовательности в serial-порт raspberry pi. Осуществляет переключение мелодий путём опроса кнопки.
* **lcd1602.py** - python скрипт осуществляющий вывод информации о состоянии raspberry на LCD экран 1602 (в проекте опционален).
* **runScripts.sh** - исполняемый bash скрипт необходим для запуска скриптов MainMidi.py и lcd1602notButton.py в скрытом режиме при старте системы.
Запуск скрипта runScripts.sh прописан в системном файле crontab. Для открытия файла необходимо набрать:
```bash
crontab -e
```
В файле добавить запись:
```bash
@reboot /home/pi/Desktop/runScripts.sh
```
Второй вариант запуска (вместо **runScripts.sh**) 
В crontab файле добавить запись:
```bash
@reboot python3 /home/pi/Desktop/MainMidi.py &
@reboot python3 /home/pi/Desktop/lcd1602.py &
```
## Аппаратная реализация (Hardware) ##
Cтруктурная схема всего комплекса:

<img src="https://github.com/sergey12malyshev/MIDItesla//raw/master/schemes/Cхема_структурная.BMP" width=37% height=57%>

Cхема электрическая принципиальная трансформатора Тесла(приведена в директории shemes):

<img src="https://github.com/sergey12malyshev/MIDItesla/blob/master/schemes/%D0%A1%D1%85%D0%B5%D0%BC%D0%B0%20%D0%BF%D1%80%D0%B8%D0%BD%D1%86%D0%B8%D0%BF%D0%B8%D0%B0%D0%BB%D1%8C%D0%BD%D0%B0%D1%8F%20%D0%9A%D0%A2.BMP" width=60% height=60%>

Схема подключения MIDI OUT и схема подключения LCD 1602:

<img src="https://github.com/sergey12malyshev/MIDItesla/blob/master/schemes/Untitled%20Sketch%202_bb.png" width=30% height=30%>     <img src="https://github.com/sergey12malyshev/MIDItesla/blob/master/schemes/Untitled%20Sketch%203_bb.png" width=45% height=45%>

## Создание MIDI-мелодий (Creating MIDI tunes) ##
Написание MIDI-мелодий происходит непосредственно в файле **MainMidi.py** используя функцию *playNote(note, timeOn, timeOff)*, где note - номер ноты от 36 до 71;  timeOn - время звучания в секундах; timeOff - время паузы в секундах (нет звучания). Соотношение нота-номер и нота-время приведено на рисунке:

<img src="https://github.com/sergey12malyshev/MIDItesla//raw/master/schemes/1677514975394.jpg" width=45% height=35%>

Доступные мелодии:
- Gershon Kingsley - Popcorn
- Super Mario Song
- Mortal Kombat Theme Song
- Valces Dogs melody
- Star Wars - The Imperial March

## Видео работы ##
https://youtu.be/iuJQ5y0yN18

## Полезная информация
* https://bsvi.ru/preryvatel-dlya-drsstc/ - прерыватель использованный для проекта
* https://bsvi.ru/malleus-maleficarum-apgrejd/ - дизайн SSTC
* http://teslacoil.ru/katushki-tesla/tranzistornyie-katushki/polumostovaya-sstc/  - дизайн SSTC
* https://stevehv.4hv.org/SSTC5.htm  - дизайн SSTC
* https://kaizerpowerelectronics.dk/tesla-coils/sstc-design-guide/ - советы по конструкции SSTC
* https://teslafon.ru/techno/calcs - калькулятор для расчёта резонансного трансформатора
* https://www.loneoceans.com/labs/ud27/ - Universal DRSSTC Tesla Coil Driver 2.7 Rev C
* https://www.osaelectronics.com/learn/setting-up-raspberry-pi-for-midi/ - работа с midi на raspberry
* https://www.midi.org/specifications-old/item/midi-din-electrical-specification - спецификация аппаратного уровня MIDI
* http://flyback.org.ru/viewtopic.php?p=4425021#4425021 - ссылка на форум по данной конструкции

### Удалённое управление
VNC Viewer: http://wiki.amperka.ru/rpi:installation:vnc

Для автоматического запуска VNC запустить скрипт **runVNC.sh**

### Параметры резонансного трансформатора ###
Емкость тороида: 6 пФ

Индуктивность первичной обмотки: 2.94 мкГн

Индуктивность вторичной обмотки: 32901 мкГн

Количество витков вторичной обмотки: 840

Емкость вторичной обмотки: 5.8 пФ

Общая емкость вторичного контура: 11.8 пФ

Резонансная частота катушки тесла: 255.4 кГц

Доп. информация для искушенных:

Длина волны: 1565 м

Длина провода вторичной обмотки (фактическая): 290 м

Длина провода 1/4 длины волны (расчетная): 391.25 м

Процент совпадения фактической и расчетной длин: 74.1 %

Сопротивление первичной обмотки:
xL = 2 * ПИ * F * L = 2ПИ * 255.4 кГц * 2.94 мкГн = 4,73 Ом

Ток первичной обмотки:
Ipeack = U/xL = (310 В/2)/4,73 Ом =  32,8 А (выбрал ключи W45NM60 - 45 А)

### TODO
Переработать проект под чтение готовых файлов .mid
