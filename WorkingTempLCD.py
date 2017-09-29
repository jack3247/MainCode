#Start of setup
import time
import Adafruit_CharLCD as LCD
import Adafruit_DHT
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
#End of setup

while(True):
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
    if humidity is not None and temperature is not None:
        temperature = temperature * 1.8 + 32
        lcd.clear()
        lcd.message('Air Temp:{0:0.1f}*F \nHumidity:{1:0.1f}%'.format(temperature, humidity))
        time.sleep(3)
        lcd.clear()
        lcd.message("Soil Moisture:NA")
        
    else:
        print('Failed to get reading. Try again!')
    time.sleep(2)
