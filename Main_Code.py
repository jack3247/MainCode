import RPi.GPIO as GPIO
import time
import Adafruit_CharLCD as LCD
import Adafruit_DHT
import thread
# Raspberry Pi pin setup
lcd_rs = 25
lcd_en = 24
lcd_d4 = 23
lcd_d5 = 17
lcd_d6 = 18
lcd_d7 = 22
lcd_backlight = 2
sensor = Adafruit_DHT.DHT22
# Define LCD column and row size for 16x2 LCD.
lcd_columns = 16
lcd_rows = 2
pin = 4
lcd = LCD.Adafruit_CharLCD(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7, lcd_columns, lcd_rows, lcd_backlight)
GPIO.setmode(GPIO.BCM)
GPIO.setup(21, GPIO.IN, pull_up_down=GPIO.PUD_UP)
counter = 0
input_state = GPIO.input(21)
  
while(True):
    input_state = GPIO.input(21)
    if input_state == False:
        counter += 1
    input_state = GPIO.input(21)
    if counter == 1:
        humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
        lcd.clear()
        input_state = GPIO.input(21)
        lcd.message('Air Temp:\n{0:0.1f}*F '.format(temperature))
        time.sleep(0.3)
        input_state = GPIO.input(21)
    else:
        input_state = GPIO.input(21)
        lcd.message("Counter:{0:0.1f}".format(counter))
        time.sleep(0.3)
        input_state = GPIO.input(21)
        lcd.clear()
        input_state = GPIO.input(21)
        
