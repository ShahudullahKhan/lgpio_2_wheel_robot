#  Run a 2-wheeled robot with the LGPIO library on Raspberry Pi 4 using L298N dc motor driver
#  Uses lgpio library, compatible with kernel 5.11
#  Author: Shahudullah Khan

from time import sleep
import lgpio

print("program starts")
#gpio pins connected with L298N motor driver module
MOTOR_ENA = 18
MOTORIN1A = 23
MOTORIN2A = 24
MOTOR_ENB = 12
MOTORIN1B = 16
MOTORIN2B = 20

# open the gpio chip and set the motor gpio pins as output
h = lgpio.gpiochip_open(0)
lgpio.gpio_claim_output(h, MOTOR_ENA)
lgpio.gpio_claim_output(h, MOTORIN1A)
lgpio.gpio_claim_output(h, MOTORIN2A)
lgpio.gpio_claim_output(h, MOTOR_ENB)
lgpio.gpio_claim_output(h, MOTORIN1B)
lgpio.gpio_claim_output(h, MOTORIN2B)
try:
    while True:
        #Stop Robot
        print("First Robot stops")
        lgpio.gpio_write(h, MOTOR_ENA, 1)
        lgpio.gpio_write(h, MOTORIN1A, 0)
        lgpio.gpio_write(h, MOTORIN2A, 0)
        lgpio.gpio_write(h, MOTOR_ENB, 1)
        lgpio.gpio_write(h, MOTORIN1B, 0)
        lgpio.gpio_write(h, MOTORIN2B, 0)
        sleep(5)
        
        #Move Robot Forward
        print("Then Robot moving Forward")
        lgpio.gpio_write(h, MOTOR_ENA, 1)
        lgpio.gpio_write(h, MOTORIN1A, 1)
        lgpio.gpio_write(h, MOTORIN2A, 0)
        lgpio.gpio_write(h, MOTOR_ENB, 1)
        lgpio.gpio_write(h, MOTORIN1B, 1)
        lgpio.gpio_write(h, MOTORIN2B, 0)
        print("value of MOTORIN1A", lgpio.gpio_read(h, MOTORIN1A))
        print("value of MOTORIN2A", lgpio.gpio_read(h, MOTORIN2A))
        sleep(10)
        
        #Stop Robot
        print("Then again Robot stops")
        lgpio.gpio_write(h, MOTOR_ENA, 1)
        lgpio.gpio_write(h, MOTORIN1A, 0)
        lgpio.gpio_write(h, MOTORIN2A, 0)
        lgpio.gpio_write(h, MOTOR_ENB, 1)
        lgpio.gpio_write(h, MOTORIN1B, 0)
        lgpio.gpio_write(h, MOTORIN2B, 0)
        sleep(1)
        
        #Move Robot Backward
        print("Then Robot moving Backward")
        lgpio.gpio_write(h, MOTOR_ENA, 1)
        lgpio.gpio_write(h, MOTORIN1A, 0)
        lgpio.gpio_write(h, MOTORIN2A, 1)
        lgpio.gpio_write(h, MOTOR_ENB, 1)
        lgpio.gpio_write(h, MOTORIN1B, 0)
        lgpio.gpio_write(h, MOTORIN2B, 1)
        print("value of MOTORIN1A", lgpio.gpio_read(h, MOTORIN1A))
        print("value of MOTORIN2A", lgpio.gpio_read(h, MOTORIN2A))
        sleep(10)
        
        #Stop Robot
        print("Then again Robot stops")
        lgpio.gpio_write(h, MOTOR_ENA, 1)
        lgpio.gpio_write(h, MOTORIN1A, 0)
        lgpio.gpio_write(h, MOTORIN2A, 0)
        lgpio.gpio_write(h, MOTOR_ENB, 1)
        lgpio.gpio_write(h, MOTORIN1B, 0)
        lgpio.gpio_write(h, MOTORIN2B, 0)
        sleep(1)
        
        #Move Robot Right
        print("Then Robot moving Right")
        lgpio.gpio_write(h, MOTOR_ENA, 1)
        lgpio.gpio_write(h, MOTORIN1A, 0)
        lgpio.gpio_write(h, MOTORIN2A, 1)
        lgpio.gpio_write(h, MOTOR_ENB, 1)
        lgpio.gpio_write(h, MOTORIN1B, 1)
        lgpio.gpio_write(h, MOTORIN2B, 0)
        sleep(10)
        
        #Stop Robot
        print("Then again Robot stops")
        lgpio.gpio_write(h, MOTOR_ENA, 1)
        lgpio.gpio_write(h, MOTORIN1A, 0)
        lgpio.gpio_write(h, MOTORIN2A, 0)
        lgpio.gpio_write(h, MOTOR_ENB, 1)
        lgpio.gpio_write(h, MOTORIN1B, 0)
        lgpio.gpio_write(h, MOTORIN2B, 0)
        sleep(1)
        
        #Move Robot Left
        print("Then Robot moving Left")
        lgpio.gpio_write(h, MOTOR_ENA, 1)
        lgpio.gpio_write(h, MOTORIN1A, 1)
        lgpio.gpio_write(h, MOTORIN2A, 0)
        lgpio.gpio_write(h, MOTOR_ENB, 1)
        lgpio.gpio_write(h, MOTORIN1B, 0)
        lgpio.gpio_write(h, MOTORIN2B, 1)
        sleep(10)
        
        #Stop Robot
        print("Then again Robot stops")
        lgpio.gpio_write(h, MOTOR_ENA, 1)
        lgpio.gpio_write(h, MOTORIN1A, 0)
        lgpio.gpio_write(h, MOTORIN2A, 0)
        lgpio.gpio_write(h, MOTOR_ENB, 1)
        lgpio.gpio_write(h, MOTORIN1B, 0)
        lgpio.gpio_write(h, MOTORIN2B, 0)
        sleep(1)
except KeyboardInterrupt:
    print("ctrl-c typed")
    #Stop Robot
    lgpio.gpio_write(h, MOTOR_ENA, 0)
    lgpio.gpio_write(h, MOTORIN1A, 0)
    lgpio.gpio_write(h, MOTORIN2A, 0)
    lgpio.gpio_write(h, MOTOR_ENB, 0)
    lgpio.gpio_write(h, MOTORIN1B, 0)
    lgpio.gpio_write(h, MOTORIN2B, 0)
    lgpio.gpiochip_close(h)
