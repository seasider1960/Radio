
#!/usr/bin/env python

from luma.oled.device import ssd1306, sh1106
from luma.core.render import canvas
from PIL import ImageFont
from PIL import Image
import os.path
import os
from mpd import MPDClient
import RPi.GPIO as GPIO
import time, textwrap
import time
import alsaaudio
import datetime
import subprocess

# Configure the GPIO pins
BUTTON_PIN = 20 # Station change
ONOFF_PIN = 21
VOLUP_PIN = 16
VOLDOWN_PIN = 19
ANNOUNCE_PIN = 24 #"No toast" announcement - connected to rotary timer on/off switch
TOAST_PIN = 12 # Small red LED that indicates GA is "on" by flashing every 10 seconds - steady on when "no toast" playing
STOP_PIN = 18 # Stops and start GA servce
GPIO.setmode(GPIO.BCM)
GPIO.setup(STOP_PIN, GPIO.IN, GPIO.PUD_UP)
GPIO.setup(BUTTON_PIN, GPIO.IN, GPIO.PUD_UP)
GPIO.setup(ONOFF_PIN, GPIO.IN, GPIO.PUD_UP)
GPIO.setup(VOLUP_PIN, GPIO.IN, GPIO.PUD_UP)
GPIO.setup(VOLDOWN_PIN, GPIO.IN, GPIO.PUD_UP)
GPIO.setup(ANNOUNCE_PIN, GPIO.IN, GPIO.PUD_UP)
GPIO.setup(TOAST_PIN, GPIO.OUT)
GPIO.output(TOAST_PIN, GPIO.LOW)
pwm = GPIO.PWM(TOAST_PIN,0.1) # 10 sec flash
pwm.start(1)

GPIO.setup(STOP_PIN, GPIO.IN, GPIO.PUD_UP)

# Setup Display
device = ssd1306(port=1, address=0x3C)
small_font = ImageFont.truetype('FreeMono.ttf', 12) 
large_font = ImageFont.truetype('FreeMono.ttf', 22)

# Setup MPC
mpc = MPDClient()
mpc.connect("localhost", 6600)   
num_stations = 0

google = True
pwmOn = True


def main():
    today_last_time = "Unknown"
    seconds = 2.5
    start = time.time()
    if time.time() - start < seconds:
        now = datetime.datetime.now()
        today_date = now.strftime("%d %b %y")
        today_time = now.strftime("%H:%M:%S")
        if today_time != today_last_time:
            today_last_time = today_time
            with canvas(device) as draw:
                now = datetime.datetime.now()
                today_date = now.strftime("%d %b %y")


                draw.text((5, 5), today_date, fill="white",font=large_font)
                draw.text((12,35), today_time, fill="white", font=large_font)

        time.sleep(0.1)


def radio1():
    img_path = os.path.abspath(os.path.join(os.path.dirname(__file__),
         'BBC Radio 1_Fotor128.png'))
    logo = Image.open(img_path).convert("RGBA")
    background = Image.new("RGBA", device.size, "white")
    posn = ((device.width - logo.width) // 2, 0)
    background.paste(logo, posn)
    device.display(background.convert(device.mode))

def radio2():
    img_path = os.path.abspath(os.path.join(os.path.dirname(__file__),
         'BBC Radio 2_Fotor128.png'))
    logo = Image.open(img_path).convert("RGBA")
    background = Image.new("RGBA", device.size, "white")
    posn = ((device.width - logo.width) // 2, 0)
    background.paste(logo, posn)
    device.display(background.convert(device.mode))

def radio3():
    img_path = os.path.abspath(os.path.join(os.path.dirname(__file__),
         'BBC Radio 3_Fotor128.png'))
    logo = Image.open(img_path).convert("RGBA")
    background = Image.new("RGBA", device.size, "white")
    posn = ((device.width - logo.width) // 2, 0)
    background.paste(logo, posn)
    device.display(background.convert(device.mode))

def radio4():
    img_path = os.path.abspath(os.path.join(os.path.dirname(__file__),
         'BBC Radio 4_Fotor128bw.png'))
    logo = Image.open(img_path).convert("RGBA")
    background = Image.new("RGBA", device.size, "white")
    posn = ((device.width - logo.width) // 2, 0)
    background.paste(logo, posn)
    device.display(background.convert(device.mode))

def worldserv():
    img_path = os.path.abspath(os.path.join(os.path.dirname(__file__),
         'BBC World Service_Fotor128.png'))
    logo = Image.open(img_path).convert("RGBA")
    background = Image.new("RGBA", device.size, "white")
    posn = ((device.width - logo.width) // 2, 0)
    background.paste(logo, posn)
    device.display(background.convert(device.mode))

def wshu():
    img_path = os.path.abspath(os.path.join(os.path.dirname(__file__),
         'WSHU_Fotor128.png'))
    logo = Image.open(img_path).convert("RGBA")
    background = Image.new("RGBA", device.size, "white")
    posn = ((device.width - logo.width) // 2, 0)
    background.paste(logo, posn)
    device.display(background.convert(device.mode))

def wnyc():
    img_path = os.path.abspath(os.path.join(os.path.dirname(__file__),
         'WNYC_Fotor128.png'))
    logo = Image.open(img_path).convert("RGBA")
    background = Image.new("RGBA", device.size, "white")
    posn = ((device.width - logo.width) // 2, 0)
    background.paste(logo, posn)
    device.display(background.convert(device.mode))

def radio1X():
    img_path = os.path.abspath(os.path.join(os.path.dirname(__file__),
         'BBC Radio 1Xtra_Fotor128.png'))
    logo = Image.open(img_path).convert("RGBA")
    background = Image.new("RGBA", device.size, "white")
    posn = ((device.width - logo.width) // 2, 0)
    background.paste(logo, posn)
    device.display(background.convert(device.mode))

def radio4X():
    img_path = os.path.abspath(os.path.join(os.path.dirname(__file__),
         'BBC Radio4extra_Fotor128.png'))
    logo = Image.open(img_path).convert("RGBA")
    background = Image.new("RGBA", device.size, "white")
    posn = ((device.width - logo.width) // 2, 0)
    background.paste(logo, posn)
    device.display(background.convert(device.mode))

def dualit():
    img_path = os.path.abspath(os.path.join(os.path.dirname(__file__),
         'Dualit_Fotor128.png'))
    logo = Image.open(img_path).convert("RGBA")
    background = Image.new("RGBA", device.size, "white")
    posn = ((device.width - logo.width) // 2, 0)
    background.paste(logo, posn)
    device.display(background.convert(device.mode))

def dualitN():
    img_path = os.path.abspath(os.path.join(os.path.dirname(__file__),
         'Dualit_Fotor128N.png'))
    logo = Image.open(img_path).convert("RGBA")
    background = Image.new("RGBA", device.size, "white")
    posn = ((device.width - logo.width) // 2, 0)
    background.paste(logo, posn)
    device.display(background.convert(device.mode))

def volume_up():
    img_path = os.path.abspath(os.path.join(os.path.dirname(__file__),
         'volume_up_Fotor128.png'))
    logo = Image.open(img_path).convert("RGBA")
    background = Image.new("RGBA", device.size, "white")
    posn = ((device.width - logo.width) // 2, 0)
    background.paste(logo, posn)
    device.display(background.convert(device.mode))

def volume_max():
    img_path = os.path.abspath(os.path.join(os.path.dirname(__file__),
         'vol_Dude128_Fotor.png'))
    logo = Image.open(img_path).convert("RGBA")
    background = Image.new("RGBA", device.size, "white")
    posn = ((device.width - logo.width) // 2, 0)
    background.paste(logo, posn)
    device.display(background.convert(device.mode))

def volume_down():
    img_path = os.path.abspath(os.path.join(os.path.dirname(__file__),
         'volume_down_Fotor128.png'))
    logo = Image.open(img_path).convert("RGBA")
    background = Image.new("RGBA", device.size, "white")
    posn = ((device.width - logo.width) // 2, 0)
    background.paste(logo, posn)
    device.display(background.convert(device.mode))

def volume_min():
    img_path = os.path.abspath(os.path.join(os.path.dirname(__file__),
         'vol_AF_Fotor128.png'))
    logo = Image.open(img_path).convert("RGBA")
    background = Image.new("RGBA", device.size, "white")
    posn = ((device.width - logo.width) // 2, 0)
    background.paste(logo, posn)
    device.display(background.convert(device.mode))

def no_toast():
    img_path = os.path.abspath(os.path.join(os.path.dirname(__file__),
         'toast_Fotor128.png'))
    logo = Image.open(img_path).convert("RGBA")
    background = Image.new("RGBA", device.size, "white")
    posn = ((device.width - logo.width) // 2, 0)
    background.paste(logo, posn)
    device.display(background.convert(device.mode))
    GPIO.output(TOAST_PIN, GPIO.HIGH)
    



current_station = 0 # index of the current station

m = alsaaudio.Mixer(control ="PCM")
vol = m.getvolume() # Get the current Volume
m.setvolume(95) # Set the volume to 95%.
vol = int(vol[0]) # Convert volume to int so it can be incremented


try:
    mpc.play(current_station)
    while True:  
        if GPIO.input(ONOFF_PIN) == False and GPIO.input(ANNOUNCE_PIN) == True: 
            num_stations = int(mpc.status()['playlistlength'])
            mpc.play()
            if pwmOn == False:
                GPIO.output(TOAST_PIN, GPIO.LOW)
                pwm = GPIO.PWM(TOAST_PIN,0.1)
                pwm.start(1)
                pwmOn = True
            
            if GPIO.input(VOLDOWN_PIN) == True and GPIO.input(VOLUP_PIN) == True:
                if num_stations == 0:
                    display_message('Error', 'add stations', '$mpc add {url}')
                elif current_station == 0:
                    radio1()
                elif current_station == 1:
                    radio2()
                elif current_station == 2:
                    radio3()
                elif current_station == 3:
                    radio4()
                elif current_station == 4:
                    worldserv()
                elif current_station == 5:
                    radio1X()
                elif current_station == 6:
                    radio4X()
                elif current_station == 7:
                    wnyc() 
                elif current_station == 8:
                    wshu()
                
                if GPIO.input(BUTTON_PIN) == False:
                    current_station += 1
                    if current_station == num_stations:
                        current_station = 0
                    mpc.play(current_station)
                    time.sleep(0.2) # key debounce
            elif GPIO.input(VOLUP_PIN) == False or GPIO.input(VOLDOWN_PIN) == False:
                if GPIO.input(VOLUP_PIN) == False:
                    if vol > 98:
                        volume_max()
                    else:
                        volume_up()
                    if vol <= 98:
                        newvol = vol + 2
                        m.setvolume(newvol)
                        vol = newvol
                    time.sleep(0.5) # key debounce
                if GPIO.input(VOLDOWN_PIN) == False:
                    if vol< 45:
                        volume_min()
                    else:
                        volume_down()
                    if vol >= 40:
                        volume_down()
                        newvol = vol - 2
                        volume_down()
                        m.setvolume(newvol)
                        volume_down()
                        vol = newvol
                        volume_down()
                    time.sleep(0.5) # key debounce
                    volume_down()
        elif GPIO.input(ONOFF_PIN) == False and GPIO.input(ANNOUNCE_PIN) == False:
            no_toast()
            mpc.stop()
            pwm.stop()
            GPIO.output(TOAST_PIN, GPIO.HIGH)
            pwmOn = False
            os.system('mpg123 disabled_announce.mp3')
            #time.sleep(0.1)
        elif GPIO.input(ONOFF_PIN) == True and GPIO.input(BUTTON_PIN) == True and GPIO.input(ANNOUNCE_PIN) == True and GPIO.input(VOLDOWN_PIN) == True and GPIO.input(VOLUP_PIN) == True:
            mpc.stop()
            vol = 95
            if pwmOn == False:
                GPIO.output(TOAST_PIN, GPIO.LOW)
                pwm = GPIO.PWM(TOAST_PIN,0.1)
                pwm.start(1)
                pwmOn = True    
            start = time.time()
            elapsed = time.time() - start
            while time.time() - start <= 1: #All this is doing is checking for a button press every second - must be a better way!
                dualit()
                if GPIO.input(ONOFF_PIN) == True and GPIO.input(BUTTON_PIN) == True and GPIO.input(ANNOUNCE_PIN) == True and GPIO.input(VOLUP_PIN) == True and GPIO.input(VOLDOWN_PIN) == True:
                    while time.time() - start > 1 and time.time() - start <= 2:
                        dualit()
                        if GPIO.input(ONOFF_PIN) == True and GPIO.input(BUTTON_PIN) == True and GPIO.input(ANNOUNCE_PIN) == True and GPIO.input(VOLUP_PIN) == True and GPIO.input(VOLDOWN_PIN) == True:
                            while time.time() - start > 2 and time.time() - start <= 3:
                                dualit()
                                if GPIO.input(ONOFF_PIN) == True and GPIO.input(BUTTON_PIN) == True and GPIO.input(ANNOUNCE_PIN) == True and GPIO.input(VOLUP_PIN) == True and GPIO.input(VOLDOWN_PIN) == True :
                                    while time.time() - start > 3 and time.time() - start <= 4:
                                        dualit()
                                        if GPIO.input(ONOFF_PIN) == True and GPIO.input(BUTTON_PIN) == True and GPIO.input(ANNOUNCE_PIN) == True and GPIO.input(VOLUP_PIN) == True and GPIO.input(VOLDOWN_PIN) == True:
                                            while time.time() - start >4 and time.time() - start <= 5:
                                                main()
                                                if GPIO.input(ONOFF_PIN) == True and GPIO.input(BUTTON_PIN) == True and GPIO.input(ANNOUNCE_PIN) == True and GPIO.input(VOLUP_PIN) == True and GPIO.input(VOLDOWN_PIN) == True:
                                                    while time.time() - start > 5 and time.time() - start <= 6:
                                                        main()
                                                        if GPIO.input(ONOFF_PIN) == True and GPIO.input(BUTTON_PIN) == True and GPIO.input(ANNOUNCE_PIN) == True and GPIO.input(VOLUP_PIN) == True and GPIO.input(VOLDOWN_PIN) == True:
                                                            while time.time() - start > 6 and time.time() - start <= 7:
                                                                main()
                                                                if GPIO.input(ONOFF_PIN) == True and GPIO.input(BUTTON_PIN) == True and GPIO.input(ANNOUNCE_PIN) == True and GPIO.input(VOLUP_PIN) == True and GPIO.input(VOLDOWN_PIN) == True:
                                                                    while time.time() - start > 7 and time.time() - start <= 8:
                                                                        main()
                                                                        if GPIO.input(ONOFF_PIN) == True and GPIO.input(BUTTON_PIN) == True and GPIO.input(ANNOUNCE_PIN) == True and GPIO.input(VOLUP_PIN) == True and GPIO.input(VOLDOWN_PIN) == True:
                                                                            while time.time() - start > 8 and time.time() - start <= 9:
                                                                                main()
                                                                        
                
            start = time.time()
        elif GPIO.input(BUTTON_PIN) == False and GPIO.input(ONOFF_PIN) == True and GPIO.input(ANNOUNCE_PIN) == True and GPIO.input(VOLUP_PIN) == True and GPIO.input(VOLDOWN_PIN) == True:
            dualitN()
        elif GPIO.input(BUTTON_PIN) == True and GPIO.input(ONOFF_PIN) == True and GPIO.input(ANNOUNCE_PIN) == False and GPIO.input(VOLUP_PIN) == True and GPIO.input(VOLDOWN_PIN) == True:
            no_toast()
            mpc.stop()
            subprocess.Popen(["/usr/bin/pkill","vlc"],stdin=subprocess.PIPE)
            pwm.stop()
            pwmOn = False
            GPIO.output(TOAST_PIN, GPIO.HIGH)
            os.system('mpg123 disabled_announce.mp3')
            GPIO.output(TOAST_PIN, GPIO.HIGH)
            
        elif GPIO.input(BUTTON_PIN) == True and GPIO.input(ONOFF_PIN) == True and GPIO.input(ANNOUNCE_PIN) == True and GPIO.input(VOLUP_PIN) == False and GPIO.input(VOLDOWN_PIN) == True:
            if vol > 98:
                volume_max()
            else:
                volume_up()
                if vol <= 98:
                    newvol = vol + 2
                    m.setvolume(newvol)
                    vol = newvol
                time.sleep(0.5) # key debounce
            
        elif GPIO.input(BUTTON_PIN) == True and GPIO.input(ONOFF_PIN) == True and GPIO.input(ANNOUNCE_PIN) == True and GPIO.input(VOLUP_PIN) == True and GPIO.input(VOLDOWN_PIN) == False:
            if vol< 45:
                volume_min()
            else:
                volume_down()
                if vol >= 40:
                    volume_down()
                    newvol = vol - 2
                    volume_down()
                    m.setvolume(newvol)
                    volume_down()
                    vol = newvol
                    volume_down()
                time.sleep(0.5) # key debounce
                volume_down()

        if GPIO.input(STOP_PIN) == False and google == True:
            os.system("sudo systemctl stop gassistpi-ok-google.service")
            os.system('mpg123 google_Off.mp3')
            pwm.stop()
            google = False
        elif GPIO.input(STOP_PIN) == False and google == False:
            os.system("sudo systemctl start gassistpi-ok-google.service")
            os.system('mpg123 google_On.mp3')
            pwm = GPIO.PWM(TOAST_PIN,0.1)
            pwm.start(1)
            google = True
                    
                            
                
           
finally:
    GPIO.cleanup()
    mpc.close()              
    mpc.disconnect()
