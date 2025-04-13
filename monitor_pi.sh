#!/bin/bash

PI_USER="pi"
PI_PORT="/dev/ttyUSB0"
PI_BOND=9600

# Запуск монитора на Pi и вывод логов в терминал
echo "Starting monitor on Pi..."
ssh -t "$PI_USER" "minicom -b $PI_BOND -D $PI_PORT"