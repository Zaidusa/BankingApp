
#sudo pip3 install Adafruit_DHT
#sudo apt-get install python3-dev python3-pip
#sudo python3 -m pip install --upgrade pip setuptools wheel

import time
import os
import RPi.GPIO as GPIO
import urllib.request as urllib2
myAPI = "J67IJL8F59RG6ARD"

GPIO.setmode(GPIO.BCM)
DEBUG = 1
import serial
# baseURL = 'https://api.thingspeak.com/update?api_key=%s' % myAPI
import Adafruit_DHT
import time
 
DHT_SENSOR = Adafruit_DHT.DHT11
DHT_PIN = 4
# read SPI data from MCP3008 chip, 8 possible adc's (0 thru 7)
def readadc(adcnum, clockpin, mosipin, misopin, cspin):
        if ((adcnum > 7) or (adcnum < 0)):
                return -1
        GPIO.output(cspin, True)

        GPIO.output(clockpin, False)  # start clock low
        GPIO.output(cspin, False)     # bring CS low

        commandout = adcnum
        commandout |= 0x18  # start bit + single-ended bit
        commandout <<= 3    # we only need to send 5 bits here
        for i in range(5):
                if (commandout & 0x80):
                        GPIO.output(mosipin, True)
                else:
                        GPIO.output(mosipin, False)
                commandout <<= 1
                GPIO.output(clockpin, True)
                GPIO.output(clockpin, False)

        adcout = 0
        # read in one empty bit, one null bit and 10 ADC bits
        for i in range(12):
                GPIO.output(clockpin, True)
                GPIO.output(clockpin, False)
                adcout <<= 1
                if (GPIO.input(misopin)):
                        adcout |= 0x1

        GPIO.output(cspin, True)
        
        adcout >>= 1       # first bit is 'null' so drop it
        return adcout

# change these as desired - they're the pins connected from the
# SPI port on the ADC to the Cobbler
SPICLK = 18
SPIMISO = 23
SPIMOSI = 24
SPICS = 25 

# set up the SPI interface pins
GPIO.setup(SPIMOSI, GPIO.OUT)
GPIO.setup(SPIMISO, GPIO.IN)
GPIO.setup(SPICLK, GPIO.OUT)
GPIO.setup(SPICS, GPIO.OUT)

while True:
    Moist = readadc(1, SPICLK, SPIMOSI, SPIMISO, SPICS)
    print("pressor:",Moist)
    sound = readadc(2, SPICLK, SPIMOSI, SPIMISO, SPICS)
    print("sound:",sound)
    humidity, temperature = Adafruit_DHT.read(DHT_SENSOR, DHT_PIN)
    if humidity is not None and temperature is not None:
        print("Temp={0:0.1f}C Humidity={1:0.1f}%".format(temperature, humidity))
        urllib2.urlopen(baseURL +"&field1=%s" % (str(temperature)))
        time.sleep(1)
        urllib2.urlopen(baseURL +"&field2=%s" % (str(humidity)))
        time.sleep(1)
        urllib2.urlopen(baseURL +"&field3=%s" % (str(Moist)))
        time.sleep(1)
        urllib2.urlopen(baseURL +"&field4=%s" % (str(sound)))
        time.sleep(1)

          

    
