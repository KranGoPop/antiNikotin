#!/bin/bash

# Путь к скомпилированному файлу (для Arduino Uno это .hex)
HEX_FILE=".pio/build/uno/firmware.hex"
PI_USER="pi"
PI_DEST="/tmp/firmware.hex"
PI_PORT="/dev/ttyUSB0"

# Компиляция на Mac
echo "Compiling on Mac..."
source ~/.platformio/penv/bin/activate &&  pio run || { echo "Compilation failed"; exit 1; }

# Копирование файла на Pi
echo "Copying $HEX_FILE to $PI_USER..."
scp "$HEX_FILE" "$PI_USER:$PI_DEST" || { echo "SCP failed"; exit 1; }

# Выполнение загрузки на Pi через SSH
echo "Uploading to Arduino from Pi..."
ssh "$PI_USER" "avrdude -c arduino -p atmega328p -P $PI_PORT -b 115200 -U flash:w:$PI_DEST" || { echo "Upload failed"; exit 1; }

# Удаление временного файла на Pi
echo "Upload complete!"