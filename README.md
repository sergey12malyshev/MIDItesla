# MIDItesla
Tesla coil music project
### Аппаратная реализация ###
![Иллюстрация к проекту](https://github.com/sergey12malyshev/MIDItesla//raw/master/Cхема_структурная.BMP)
### Программная реализация ###
* MainMidi.py - python скрипт генерирующий MIDI последовательности в serial-порт raspberry pi. Осуществляет переключение мелодий путём опроса кнопки.
* lcd1602notButton.py - python скрипт осуществляющий вывод информации о состоянии raspberry на LCD экран 1602 (в проекте опционален).
* runScripts.sh - shell скрипт необходим для запуска скриптов MainMidi.py и lcd1602notButton.py в скрытом режиме при старте системы.
Запуск скрипта runScripts.sh прописан в системном файле crontab. Для открытия файла необходимо набрать:
```bash
sudo crontab -e
```
