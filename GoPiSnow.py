import snowboydecoder
import sys
import signal
from gopigo import *
import picamera
from time import sleep

# Demo code for listening two hotwords at the same time

interrupted = False
camera=picamera.PiCamera()
camera.vflip= True
camera.hflip= True

def signal_handler(signal, frame):
    global interrupted
    interrupted = True


def interrupt_callback():
    global interrupted
    return interrupted


models = ["pauls/go.pmdl", "pauls/left.pmdl", "pauls/right.pmdl", "pauls/backwards.pmdl", "pauls/robotdance.pmdl", "pauls/blinklights.pmdl", "pauls/look.pmdl"]
camera.start_recording('video.h264')

def go():
    fwd()
    sleep(3)
    stop()

def lefter():
    left_rot()
    sleep(0.25)
    stop()

def righter():
    right_rot()
    sleep(0.25)
    stop()
    

def backr():
    bwd()
    sleep(1.5)
    stop()

def dance():
    forward()
    sleep(0.25)
    left_rot()
    sleep(0.75)
    bwd()
    sleep(0.5)
    right_rot()
    sleep(1)
    stop()

def blinker():
    led_on(LED_L)
    sleep(.3)
    led_off(LED_L)
    led_on(LED_R)
    sleep(.3)
    led_off(LED_R)
    led_on(LED_L)
    sleep(.3)
    led_off(LED_L)
    led_on(LED_R)
    sleep(.3)
    led_off(LED_R)
    led_on(LED_L)
    sleep(.3)
    led_off(LED_L)
    led_on(LED_R)
    sleep(.3)
    led_off(LED_R)
    led_on(LED_L)
    sleep(.3)
    led_off(LED_L)
    led_on(LED_R)
    sleep(.3)
    led_off(LED_R)

def look():
    servo(180)
    sleep(0.4)
    servo(0)
    sleep(0.5)
    servo(90)
   
    

    
# capture SIGINT signal, e.g., Ctrl+C
signal.signal(signal.SIGINT, signal_handler)
enable_servo()
servo(90)

sensitivity = 0.37
detector = snowboydecoder.HotwordDetector(models, sensitivity=sensitivity)
callbacks = [lambda: go(), lambda: lefter(), lambda: righter(), lambda: backr(), lambda: dance(), lambda: blinker(), lambda: look()]

print('Listening... Press Ctrl+C to exit')


# main loop
# make sure you have the same numbers of callbacks and models
detector.start(detected_callback=callbacks,
               interrupt_check=interrupt_callback,
               sleep_time=0.03)

detector.terminate()
