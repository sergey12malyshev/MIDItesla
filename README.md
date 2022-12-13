# MIDItesla
Tesla coil music project

<img src="https://github.com/sergey12malyshev/MIDItesla//raw/master/images/КТ.jpg" width=25% height=25%> <img src="https://github.com/sergey12malyshev/MIDItesla//raw/master/images/Пульт.jpg" width=35% height=35%>


### Аппаратная реализация ###

<img src="https://github.com/sergey12malyshev/MIDItesla//raw/master/schemes/Cхема_структурная.BMP" width=40% height=40%>

### Программная реализация ###
* MainMidi.py - python скрипт генерирующий MIDI последовательности в serial-порт raspberry pi. Осуществляет переключение мелодий путём опроса кнопки.
* lcd1602notButton.py - python скрипт осуществляющий вывод информации о состоянии raspberry на LCD экран 1602 (в проекте опционален).
* runScripts.sh - shell скрипт необходим для запуска скриптов MainMidi.py и lcd1602notButton.py в скрытом режиме при старте системы.
Запуск скрипта runScripts.sh прописан в системном файле crontab. Для открытия файла необходимо набрать:
```bash
sudo crontab -e
```
# Полезная информация
* https://bsvi.ru/preryvatel-dlya-drsstc/ - прерыватель использованный для проекта
* https://bsvi.ru/malleus-maleficarum-apgrejd/
* http://teslacoil.ru/katushki-tesla/tranzistornyie-katushki/polumostovaya-sstc/ 
* https://stevehv.4hv.org/SSTC5.htm
