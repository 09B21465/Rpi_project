from gpiozero import LED
import time

led = LED(18)

while True:
    
    led.on()
    
    time.sleep(1.0)
    
    led.off()
    
    time.sleep(1.0)
