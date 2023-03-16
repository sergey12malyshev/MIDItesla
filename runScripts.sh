#!/bin/bash

# Run two python scripts
# https://habr.com/ru/company/ruvds/blog/325522/ 
# Разрешить исполнение скрипта: chmod +x ./runScripts.sh (https://pingvinus.ru/note/chmod)
# Запуск из CLI: ./runScripts.sh

cd /home/pi/Desktop

echo "run MainMidi"
python3 MainMidi.py &

echo "run lcd1602.py"
python3 lcd1602.py &

# Complete and return success value
exit 0