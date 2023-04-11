import time
import os

GPIO_PIN = 9
SYSFS_PIN = 119  # Sysfs hodnota odpovídající pinu 9

def export_gpio(pin):
    with open('/sys/class/gpio/export', 'w') as file:
        file.write(str(pin))

def set_gpio_direction(pin, direction):
    with open(f'/sys/class/gpio/gpio{pin}/direction', 'w') as file:
        file.write(direction)

def set_gpio_value(pin, value):
    with open(f'/sys/class/gpio/gpio{pin}/value', 'w') as file:
        file.write(str(value))

export_gpio(SYSFS_PIN)
set_gpio_direction(SYSFS_PIN, 'out')

while True:
    set_gpio_value(SYSFS_PIN, 1)
    time.sleep(5)
    set_gpio_value(SYSFS_PIN, 0)
    time.sleep(5)
