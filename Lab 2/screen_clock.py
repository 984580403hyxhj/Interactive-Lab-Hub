import datetime
import time
import subprocess
import digitalio
import board
from PIL import Image, ImageDraw, ImageFont
import adafruit_rgb_display.st7789 as st7789

# Configuration for CS and DC pins (these are FeatherWing defaults on M0/M4):
cs_pin = digitalio.DigitalInOut(board.CE0)
dc_pin = digitalio.DigitalInOut(board.D25)
reset_pin = None

# Config for display baudrate (default max is 24mhz):
BAUDRATE = 64000000

# Setup SPI bus using hardware SPI:
spi = board.SPI()

# Create the ST7789 display:
disp = st7789.ST7789(
    spi,
    cs=cs_pin,
    dc=dc_pin,
    rst=reset_pin,
    baudrate=BAUDRATE,
    width=135,
    height=240,
    x_offset=53,
    y_offset=40,
)

# Create blank image for drawing.
# Make sure to create image with mode 'RGB' for full color.
height = disp.width  # we swap height/width to rotate it to landscape!
width = disp.height
image = Image.new("RGB", (width, height))
rotation = 90

# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)

# Draw a black filled box to clear the image.
draw.rectangle((0, 0, width, height), outline=0, fill=(0, 0, 0))
disp.image(image, rotation)
# Draw some shapes.
# First define some constants to allow easy resizing of shapes.
padding = -2
top = padding
bottom = height - padding
# Move left to right keeping track of the current x position for drawing shapes.
x = 0

# Alternatively load a TTF font.  Make sure the .ttf font file is in the
# same directory as the python script!
# Some other nice fonts to try: http://www.dafont.com/bitmap.php
font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 18)

# these setup the code for our buttons and the backlight and tell the pi to treat the GPIO pins as digitalIO vs analogIO
backlight = digitalio.DigitalInOut(board.D22)
backlight.switch_to_output()
backlight.value = True
buttonA = digitalio.DigitalInOut(board.D23)
buttonB = digitalio.DigitalInOut(board.D24)
buttonA.switch_to_input()
buttonB.switch_to_input()


calender = {1 : [("VR/AR", "9:40"), ("PSYsocial", "11:00"), ("HCI", "13:00")],
            2 : [("idd", "8:20"), ("AML", "13:00")],
            3 : [("VR/AR", "9:40"), ("PSYsocial", "11:00"), ("HCI", "13:00")],
            4 : [("idd", "8:20"), ("AML", "13:00")]
            }

weekDayName = {
    1 : "Monday",
    2 : "Tuesday",
    3 : "Wednesday",
    4 : "Thursday",
    5 : "Friday",
    6 : "Saturday",
    7 : "Sunday"
}

while True:
    # Draw a black filled box to clear the image.
    draw.rectangle((0, 0, width, height), outline=0, fill=0)

    #TODO: Lab 2 part D work should be filled in here. You should be able to look in cli_clock.py and stats.py 
    # if buttonA.value and buttonB.value:
    #     backlight.value = False  # turn off backlight
    # else:
    #     backlight.value = True  # turn on backlight
    # if buttonB.value and not buttonA.value:  # just button A pressed
    #     display.fill(screenColor) # set the screen to the users color
    # if buttonA.value and not buttonB.value:  # just button B pressed
    #     display.fill(color565(255, 255, 255))  # set the screen to white
    # if not buttonA.value and not buttonB.value:  # none pressed
    #     display.fill(color565(0, 255, 0))  # green
    # y = top
    # draw.text((x, y), IP, font=font, fill="#FFFFFF")
    # y += font.getsize(IP)[1]
    # draw.text((x, y), WTTR, font=font, fill="#FFFF00")
    # y += font.getsize(WTTR)[1]
    # draw.text((x, y), USD, font=font, fill="#0000FF")
    # y += font.getsize(USD)[1]
    # draw.text((x, y), Temp, font=font, fill="#FF00FF")
    now = datetime.datetime.now()
    weekday = now.weekday() + 1
    backlight.value = True
    if buttonA.value and buttonB.value:
        welcome = "Hello, today is " + weekDayName[weekday]
        dayInfo = "You have " + str(len(calender[weekday])) + " classes"
        y = top
        draw.text((x, y), welcome, font=font, fill="#FFFFFF")
        y += font.getsize(welcome)[1]
        draw.text((x,y), dayInfo, font = font, fill="#FFFFFF")

    if not ButtonA.value and buttonB.value:
        info = "Your classes are:"
        y = top
        draw.text((x, y), info, font=font, fill="#FFFFFF")
        for i in calender[weekday]:
            y += font.getsize(info)[1]
            output = i[0] + " at " + i[1]
            draw.text((x,y), output, font=font, fill="#FFFF00")

    # Display image.
    disp.image(image, rotation)
    time.sleep(1)
