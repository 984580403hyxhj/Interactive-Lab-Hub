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


calender = {1 : [("VR/AR", ["9:40","11:00"]), ("PSYsocial", ["11:25","12:40"]), ("HCI", ["13:00","14:15"])],
            2 : [("idd", ["8:20","9:30"]), ("AML", ["13:00","14:15"])],
            3 : [("VR/AR", ["9:40","11:00"]), ("PSYsocial", ["11:25","12:40"]), ("HCI", ["13:00","14:15"])],
            4 : [("idd", ["8:20","9:30"]), ("AML", ["13:00","14:15"])],
            5 : [],
            6 : [],
            7 : []
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

score = 0

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
        # image = Image.open("red.jpg")
        # backlight = digitalio.DigitalInOut(board.D22)
        # backlight.switch_to_output()
        # backlight.value = True
        #
        # # Scale the image to the smaller screen dimension
        # image_ratio = image.width / image.height
        # screen_ratio = width / height
        # if screen_ratio < image_ratio:
        #     scaled_width = image.width * height // image.height
        #     scaled_height = height
        # else:
        #     scaled_width = width
        #     scaled_height = image.height * width // image.width
        # image = image.resize((scaled_width, scaled_height), Image.BICUBIC)
        #
        # # Crop and center the image
        # x = scaled_width // 2 - width // 2
        # y = scaled_height // 2 - height // 2
        # image = image.crop((x, y, x + width, y + height))
        draw.rectangle((0, 0, width, height), outline=0, fill=0)
        welcome = "Welcome to CT Calender"
        y = top
        draw.text((x, y), welcome, font=font, fill="#FFFFFF")
        y += font.getsize(welcome)[1]
        draw.text((x,y), "Time:"+str(now), font=font, fill="#FFFFFF")
        y += font.getsize(welcome)[1]
        draw.text((x, y), "You've attended " + str(score) + "lectures", font=font, fill="#FFFFFF")
        y += font.getsize(welcome)[1]
        draw.text((x, y), "Great Job!", font=font, fill="#00FFFF")
        #print("none")
        pass
    if not buttonA.value and buttonB.value:
        draw.rectangle((0, 0, width, height), outline=0, fill=0)
        print(calender)
        welcome = "Hello, today is " + weekDayName[weekday]
        dayInfo = "You have " + str(len(calender[weekday])) + " classes"
        y = top
        draw.text((x, y), welcome, font=font, fill="#FFFFFF")
        y += font.getsize(welcome)[1]
        draw.text((x,y), dayInfo, font = font, fill="#FFFFFF")
        print("A")

    if buttonA.value and not buttonB.value:
        draw.rectangle((0, 0, width, height), outline=0, fill=0)
        info = "Your classes are:"
        y = top
        draw.text((x, y), info, font=font, fill="#FFFFFF")
        for i in calender[weekday]:
            y += font.getsize(info)[1]
            output = i[0] + " from " + i[1][0] + " to " + i[1][1]
            draw.text((x,y), output, font=font, fill="#FFFF00")
        print("B")


    if not buttonA.value and not buttonB.value:
        draw.rectangle((0, 0, width, height), outline=0, fill=0)
        info = "Next classes is "
        have_class = False
        for i in calender[weekday]:
            tempTime = datetime.datetime.strptime(i[1][0], '%H:%M')
            class_hour = tempTime.hour
            class_minute = tempTime.minute
            hour = now.hour
            minute = now.minute
            if class_hour > hour or class_hour == hour and class_minute > minute:
                have_class = True
                info = info + i[0]
                y = top
                draw.text((x, y), info, font=font, fill="#FFFFFF")
                minute_gap = class_minute - minute
                if minute_gap < 0:
                    minute_gap = 60 + minute_gap
                    class_hour -= 1
                hour_gap = class_hour - hour
                info = "You still have " + str(hour_gap) + "h" + str(minute_gap) + "m"
                score += 1
                y += font.getsize(info)[1]
                color = "#0000FF"
                if hour_gap < 1:
                    color = "#FF0000"
                draw.text((x,y), info, font=font, fill=color)
                break
        print(have_class)
        if not have_class:
            draw.text((x,y), "You have no class! Enjoy!", font=font, fill="#00FF00")

    # Display image.
    disp.image(image, rotation)
    time.sleep(1)
