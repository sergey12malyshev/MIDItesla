# MIDItesla
MIDI Tesla Coil Controller

Проект музыкальной катушки Тесла построенной по топологии SSTC полумост. Состоит из непосредсвенно катушки Тесла, MIDI-контроллера состоящего из прерывателя bsvi на Atmega8 и микрокомпьютера Rasberry Pi 3B генерирующего MIDI мелодии.

<img src="https://github.com/sergey12malyshev/MIDItesla//raw/master/images/КТ.jpg" width=15% height=15%> <img src="https://github.com/sergey12malyshev/MIDItesla//raw/master/images/Пульт.jpg" width=25% height=15%>


### Аппаратная реализация (Hardware) ###

<img src="https://github.com/sergey12malyshev/MIDItesla//raw/master/schemes/Cхема_структурная.BMP" width=30% height=30%>

Cхема электрическая принципиальная КТ приведена в директории shemes:

<img src="https://github.com/sergey12malyshev/MIDItesla/blob/master/schemes/%D0%A1%D1%85%D0%B5%D0%BC%D0%B0%20%D0%BF%D1%80%D0%B8%D0%BD%D1%86%D0%B8%D0%BF%D0%B8%D0%B0%D0%BB%D1%8C%D0%BD%D0%B0%D1%8F%20%D0%9A%D0%A2.BMP" width=25% height=25%>


### Программная реализация (Software) ###
* **MainMidi.py** - python скрипт генерирующий MIDI последовательности в serial-порт raspberry pi. Осуществляет переключение мелодий путём опроса кнопки.
* **lcd1602notButton.py** - python скрипт осуществляющий вывод информации о состоянии raspberry на LCD экран 1602 (в проекте опционален).
* **runScripts.sh** - shell скрипт необходим для запуска скриптов MainMidi.py и lcd1602notButton.py в скрытом режиме при старте системы.
Запуск скрипта runScripts.sh прописан в системном файле crontab. Для открытия файла необходимо набрать:
```bash
sudo crontab -e
```
### Видео работы ###
https://youtu.be/iuJQ5y0yN18

# Полезная информация
* https://bsvi.ru/preryvatel-dlya-drsstc/ - прерыватель использованный для проекта
* https://bsvi.ru/malleus-maleficarum-apgrejd/
* http://teslacoil.ru/katushki-tesla/tranzistornyie-katushki/polumostovaya-sstc/ 
* https://stevehv.4hv.org/SSTC5.htm
* https://kaizerpowerelectronics.dk/tesla-coils/sstc-design-guide/
* https://teslafon.ru/techno/calcs

### Удалённое управление
VNC Viewer: http://wiki.amperka.ru/rpi:installation:vnc

### Параметры резонансного трансформатора
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
