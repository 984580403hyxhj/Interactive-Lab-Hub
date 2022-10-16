# Ph-UI!!!

Akhil Uddandam
Steve Xue

For lab this week, we focus both on sensing, to bring in new modes of input into your devices, as well as prototyping the physical look and feel of the device. You will think about the physical form the device needs to perform the sensing as well as present the display or feedback about what was sensed. 

## Part 1 Lab Preparation

### Get the latest content:
As always, pull updates from the class Interactive-Lab-Hub to both your Pi and your own GitHub repo. As we discussed in the class, there are 2 ways you can do so:

**\[recommended\]**Option 1: On the Pi, `cd` to your `Interactive-Lab-Hub`, pull the updates from upstream (class lab-hub) and push the updates back to your own GitHub repo. You will need the personal access token for this.

```
pi@ixe00:~$ cd Interactive-Lab-Hub
pi@ixe00:~/Interactive-Lab-Hub $ git pull upstream Fall2022
pi@ixe00:~/Interactive-Lab-Hub $ git add .
pi@ixe00:~/Interactive-Lab-Hub $ git commit -m "get lab4 content"
pi@ixe00:~/Interactive-Lab-Hub $ git push
```

Option 2: On your your own GitHub repo, [create pull request](https://github.com/FAR-Lab/Developing-and-Designing-Interactive-Devices/blob/2021Fall/readings/Submitting%20Labs.md) to get updates from the class Interactive-Lab-Hub. After you have latest updates online, go on your Pi, `cd` to your `Interactive-Lab-Hub` and use `git pull` to get updates from your own GitHub repo.

### Start brasinstorming ideas by reading: 
* [What do prototypes prototype?](https://www.semanticscholar.org/paper/What-do-Prototypes-Prototype-Houde-Hill/30bc6125fab9d9b2d5854223aeea7900a218f149)
* [Paper prototyping](https://www.uxpin.com/studio/blog/paper-prototyping-the-practical-beginners-guide/) is used by UX designers to quickly develop interface ideas and run them by people before any programming occurs. 
* [Cardboard prototypes](https://www.youtube.com/watch?v=k_9Q-KDSb9o) help interactive product designers to work through additional issues, like how big something should be, how it could be carried, where it would sit. 
* [Tips to Cut, Fold, Mold and Papier-Mache Cardboard](https://makezine.com/2016/04/21/working-with-cardboard-tips-cut-fold-mold-papier-mache/) from Make Magazine.
* [Surprisingly complicated forms](https://www.pinterest.com/pin/50032245843343100/) can be built with paper, cardstock or cardboard.  The most advanced and challenging prototypes to prototype with paper are [cardboard mechanisms](https://www.pinterest.com/helgangchin/paper-mechanisms/) which move and change. 
* [Dyson Vacuum Cardboard Prototypes](http://media.dyson.com/downloads/JDF/JDF_Prim_poster05.pdf)
<p align="center"><img src="https://dysonthedesigner.weebly.com/uploads/2/6/3/9/26392736/427342_orig.jpg"  width="200" > </p>

### Gathering materials for this lab:

* Cardboard (start collecting those shipping boxes!)
* Found objects and materials--like bananas and twigs.
* Cutting board
* Cutting tools
* Markers

(We do offer shared cutting board, cutting tools, and markers on the class cart during the lab, so do not worry if you don't have them!)

## Deliverables \& Submission for Lab 4

The deliverables for this lab are, writings, sketches, photos, and videos that show what your prototype:
* "Looks like": shows how the device should look, feel, sit, weigh, etc.
* "Works like": shows what the device can do.
* "Acts like": shows how a person would interact with the device.

For submission, the readme.md page for this lab should be edited to include the work you have done:
* Upload any materials that explain what you did, into your lab 4 repository, and link them in your lab 4 readme.md.
* Link your Lab 4 readme.md in your main Interactive-Lab-Hub readme.md. 
* Group members can turn in one repository, but make sure your Hub readme.md links to the shared repository.
* Labs are due on Mondays, make sure to submit your Lab 4 readme.md to Canvas.


## Lab Overview

A) [Capacitive Sensing](#part-a)

B) [OLED screen](#part-b) 

C) [Paper Display](#part-c)

D) [Materiality](#part-d)

E) [Servo Control](#part-e)

F) [Record the interaction](#part-f)

## The Report (Part 1: A-D, Part 2: E-F)

### Part A
### Capacitive Sensing, a.k.a. Human-Twizzler Interaction 

We want to introduce you to the [capacitive sensor](https://learn.adafruit.com/adafruit-mpr121-gator) in your kit. It's one of the most flexible input devices we are able to provide. At boot, it measures the capacitance on each of the 12 contacts. Whenever that capacitance changes, it considers it a user touch. You can attach any conductive material. In your kit, you have copper tape that will work well, but don't limit yourself! In the example below, we use Twizzlers--you should pick your own objects.


<p float="left">
<img src="https://cdn-learn.adafruit.com/guides/cropped_images/000/003/226/medium640/MPR121_top_angle.jpg?1609282424" height="150" />
<img src="https://cdn-shop.adafruit.com/1200x900/4401-01.jpg" height="150">
</p>

Plug in the capacitive sensor board with the QWIIC connector. Connect your Twizzlers with either the copper tape or the alligator clips (the clips work better). In this lab, we will continue to use the `circuitpython` virtual environment we created before. Activate `circuitpython` and `cd` to your Lab 4 folder to install the requirements by:

```
(circuitpython) pi@ixe00:~/Interactive-Lab-Hub/Lab 4 $ pip3 install -r requirements.txt
```

<img src="https://media.discordapp.net/attachments/679721816318803975/823299613812719666/PXL_20210321_205742253.jpg" width=400>
These Twizzlers are connected to pads 6 and 10. When you run the code and touch a Twizzler, the terminal will print out the following

```
(circuitpython) pi@ixe00:~/Interactive-Lab-Hub/Lab 4 $ python cap_test.py 
Twizzler 10 touched!
Twizzler 6 touched!
```

### Part B
### More sensors

#### Light/Proximity/Gesture sensor (APDS-9960)

We here want you to get to know this awesome sensor [Adafruit APDS-9960](https://www.adafruit.com/product/3595). It is capable of sensing proximity, light (also RGB), and gesture! 

<img src="https://cdn-shop.adafruit.com/970x728/3595-03.jpg" width=200>

Connect it to your pi with Qwiic connector and try running the three example scripts individually to see what the sensor is capable of doing!

```
(circuitpython) pi@ixe00:~/Interactive-Lab-Hub/Lab 4 $ python proximity_test.py
...
(circuitpython) pi@ixe00:~/Interactive-Lab-Hub/Lab 4 $ python gesture_test.py
...
(circuitpython) pi@ixe00:~/Interactive-Lab-Hub/Lab 4 $ python color_test.py
...
```

You can go the the [Adafruit GitHub Page](https://github.com/adafruit/Adafruit_CircuitPython_APDS9960) to see more examples for this sensor!

#### Rotary Encoder

A rotary encoder is an electro-mechanical device that converts the angular position to analog or digital output signals. The [Adafruit rotary encoder](https://www.adafruit.com/product/4991#technical-details) we ordered for you came with separated breakout board and encoder itself, that is, they will need to be soldered if you have not yet done so! We will be bringing the soldering station to the lab class for you to use, also, you can go to the MakerLAB to do the soldering off-class. Here is some [guidance on soldering](https://learn.adafruit.com/adafruit-guide-excellent-soldering/preparation) from Adafruit. When you first solder, get someone who has done it before (ideally in the MakerLAB environment). It is a good idea to review this material beforehand so you know what to look at.

<p float="left">
<img src="https://cdn-shop.adafruit.com/970x728/4991-01.jpg" height="200" />
<img src="https://cdn-shop.adafruit.com/970x728/377-02.jpg" height="200" />
<img src="https://cdn-shop.adafruit.com/970x728/4991-09.jpg" height="200">
</p>

Connect it to your pi with Qwiic connector and try running the example script, it comes with an additional button which might be useful for your design!

```
(circuitpython) pi@ixe00:~/Interactive-Lab-Hub/Lab 4 $ python encoder_test.py
```

You can go to the [Adafruit Learn Page](https://learn.adafruit.com/adafruit-i2c-qt-rotary-encoder/python-circuitpython) to learn more about the sensor! The sensor actually comes with an LED (neo pixel): Can you try lighting it up? 

#### Joystick

A [joystick](https://www.sparkfun.com/products/15168) can be used to sense and report the input of the stick for it pivoting angle or direction. It also comes with a button input!

<p float="left">
<img src="https://cdn.sparkfun.com//assets/parts/1/3/5/5/8/15168-SparkFun_Qwiic_Joystick-01.jpg" height="200" />
</p>

Connect it to your pi with Qwiic connector and try running the example script to see what it can do!

```
(circuitpython) pi@ixe00:~/Interactive-Lab-Hub/Lab 4 $ python joystick_test.py
```

You can go to the [SparkFun GitHub Page](https://github.com/sparkfun/Qwiic_Joystick_Py) to learn more about the sensor!

#### Distance Sensor

Earlier we have asked you to play with the proximity sensor, which is able to sense object within a short distance. Here, we offer [Qwiic Multi Distance Sensor](https://www.sparkfun.com/products/17072), which has a field of view of about 25° and is able to detect objects up to 3 meters away! 

<p float="left">
<img src="https://cdn.sparkfun.com//assets/parts/1/6/0/3/4/17072-Qwiic_Multi_Distance_Sensor_-_VL53L3CX-01.jpg" height="200" />
</p>

Connect it to your pi with Qwiic connector and try running the example script to see how it works!

```
(circuitpython) pi@ixe00:~/Interactive-Lab-Hub/Lab 4 $ python distance_test.py
```

You can go to the [SparkFun GitHub Page](https://github.com/sparkfun/Qwiic_VL53L1X_Py) to learn more about the sensor and see other examples!

### Part C
### Physical considerations for sensing

Usually, sensors need to positioned in specific locations or orientations to make them useful for their application. Now that you've tried a bunch of the sensors, pick one that you would like to use, and an application where you use the output of that sensor for an interaction. For example, you can use a distance sensor to measure someone's height if you position it overhead and get them to stand under it.

**\*\*\*Draw 5 sketches of different ways you might use your sensor, and how the larger device needs to be shaped in order to make the sensor useful.\*\*\***










**\*\*\*What are some things these sketches raise as questions? What do you need to physically prototype to understand how to answer those questions?\*\*\***

Idea 1:
The touch sensor that senses when the user, who is on a diet and refraining from the loaded sugary foods in the fridge, touches the fridge knob and promptly responds with warning messages!
![IMG_922A2BD49C77-1](https://user-images.githubusercontent.com/54753807/196012490-68d49b4e-5110-4363-b1bb-ef1f74f82c00.jpeg)


Question 1: How do we place our sensor so that it won’t impair the appearance of the fridge
Question 2: How do need find a good eating time for each person, and everyone is different

I think we have to try to place the sensor in different places of the fridge to see where is the least intrusive way to put our sensor without damaging the appearance of the fridge. We also need to do a lot of contextual inquiry to many users with a health professional to come up with a algorithm to find out the best eating time for different user.

Idea 2
We use the distance sensor to give interactive warnings to users who are moving around while using the Quest 2 VR headset. This sensor will interact with the user by promptly outputting a warning buzzer sound when the user is within 3 feet of an object. 
![IMG_20BCFB1E8EF6-1](https://user-images.githubusercontent.com/54753807/196012493-6b815fae-8d55-465c-b681-6aa0aa0bc8d4.jpeg)

Question 1: Where is a good position for users to wear it so it is comfortable.
Question 2: Is the sensor protected? How do we prevent it from exposing to physical damage?
Question 3: What area around the user is this sensor detecting? Is it really helpful, will it missing some area?
Question 4: What is the good threshold to alarm the user?

We can try different forms of the device, and try it on different positions of the user’s body to find out the area it is detecting.



Idea 3:
We use the rotary sensor to provide feedback to the user on the angular rotation and speed that the window blinds are rotating.
![IMG_D2B3CB6E4F93-1](https://user-images.githubusercontent.com/54753807/196012495-e19a9c59-be94-470b-b98b-a694abcd7260.jpeg)

Question 1: Where do we put the rotary sensor so the user can reach it while lying on bed?
Question 2: What is the equation mapping the rotary sensor to the blinds’ position? Should it be linear or some other equation?
Question 3: What feedback should we give to the user except moving the blinds.

We can try to put the sensor in different location, and try out different mapping equations, and try out different interactions to send feedback to the user(haptic feedback on the button, voice, vibration, etc)

Idea 4:
Using the joystick as an interactive device to control user movements in an interactive FPS video game. 
![IMG_1B187E335C3F-1](https://user-images.githubusercontent.com/54753807/196012503-b42721cb-31aa-4466-a60b-78c1c8c6a867.jpeg)

Question 1: What is the sensitivity of the cursor movement
Question 2: Can we add more feedback on the controller
Question 3: How do we place the joystick so that it won’t be damaged by user

We can detach the joystick from the motherboard, and make the joystick changeable. We also need to test different cursor movement, and try other interaction to give better experience(haptic feedback is pretty good on FPS games)

Idea 5:
Use the light sensor to warn the user of when he has stepped out of the well lit up “gaming environment” when using the Quest 2 VR headset. The sensor will detect when the user has stepped out into the dark and promptly respond with a warning feedback indicating to the user to return. Furthermore, it will also interact with the user by warning him that he is close to stepping out of bounds. 
![IMG_986DA6618D42-1](https://user-images.githubusercontent.com/54753807/196012506-2ee614c9-5e56-464e-abdf-75cd8c01ab38.jpeg)

Question 1: How to choose the right area to limit user’s safe area
Question 2: Where do we put the sensor so that it can detect more information and give feedback to the user

We can put the device in different positions both on the users, and in other areas.

**\*\*\*Pick one of these designs to prototype.\*\*\***

We chose our second idea to prototype:
The main purpose behind this interactive device is to use the distance sensor to give interactive warnings to users who are moving around while using the Quest 2 VR headset. This sensor will interact with the user by promptly outputting a warning buzzer sound when the user is within 3 feet of an object. 
![IMG_7242](https://user-images.githubusercontent.com/54753807/196012534-c36372a2-755e-471c-a032-c48bd97ae956.jpg)


After experimenting , we decided to put the device behind the user’s back, as it was less intrusive(the belly area is more sensitive than the back) and the Quest 2 VR has a visual sensor in the front. Furthermore,  it provides more information and less error (users can reach their hand forward and get in the way of the sensor, and have nothing behind them). Thus putting it behind provides more important information to enrich the user experience.

There is a video showing how you walk with it:
https://youtube.com/shorts/fKDY5vf9bCs?feature=share

### Part D

 
**\*\*\*Sketch 5 designs for how you would physically position your display and any buttons or knobs needed to interact with it.\*\*\***
![ff14-18](https://user-images.githubusercontent.com/54753807/196012547-0a9b9e69-f244-49f1-b3b8-89394a73364e.jpg)
![IMG_DDF71BF55E75-1](https://user-images.githubusercontent.com/54753807/196012548-6b146505-9516-496a-9170-66d7e9c727e0.jpeg)


**The display feedback from the sensors will be shown in the Users Quest 2 VR OS. It will show a dialog box with insightful information/feedback as well as an auditory warning.**

**\*\*\*What are some things these sketches raise as questions? What do you need to physically prototype to understand how to answer those questions?\*\*\***


Question 1: When connecting the pi to different sensors, how do we protect the cable from potential damage?
Question 2: What is the threshold to display the message
Question 3: We have two sensors, if both sensor are detecting potential danger(detect close object and at the edge of safe zone), which message should take the priority
Question 4: How do we merge multiple sensor data streams in a way that effectively provides interactive feedback for the user.

To better gauge our design, we will need to create a mini obstacle detection course for the device to test its sensor functionality and observe just how well both sensor types work together in providing valuable interaction with the user and his environment. 


**\*\*\*Pick one of these display designs to integrate into your prototype.\*\*\***
The light sensor and distance sensors will be our primary devices to enrich our user experience and interactions. 
![IMG_7245](https://user-images.githubusercontent.com/54753807/196012555-b5d418c1-cb33-4c30-94c9-fb825c593d79.jpg)
![IMG_7246](https://user-images.githubusercontent.com/54753807/196012556-f6807691-2ca0-46a0-9eab-c7155a2f8227.jpg)
![IMG_7247](https://user-images.githubusercontent.com/54753807/196012557-aee032f6-9140-4995-89ce-cb6c95ec698d.jpg)
![IMG_7248](https://user-images.githubusercontent.com/54753807/196012564-5b32c297-ad17-4b55-8be9-72c2cc9a7e7d.jpg)
![IMG_7249](https://user-images.githubusercontent.com/54753807/196012567-23f48896-f024-4897-a990-e07fca4fd149.jpg)


**\*\*\*Explain the rationale for the design.\*\*\*** (e.g. Does it need to be a certain size or form or need to be able to be seen from a certain distance?)

The main objective behind our devices is to provide a safe experience for a Quest 2 VR user who is blinded from the device. By providing a distance and light sensor, the device is able to be an “interactive eye” to the user by providing a running warning with distance measurements when the user is within 3 feet of an object. Similarly, we can mark up the user's environment with red tape on the ground and lit up the surroundings so that when the user exits the “safe zones”, they will be warned and can interact accordingly by navigating back. The display we used will be the VR headset, as the user will not be able to look at other screens while using it. The warning display will show in the headset display. 

**The display feedback from the sensors will be shown in the Users Quest 2 VR OS. It will show a dialog box with insightful information/feedback as well as an auditory warning.**


Build a cardboard prototype of your design.

**\*\*\*Document your rough prototype.\*\*\***

This is a video showing the final interaction
https://youtu.be/sUQUMoJSgdo

LAB PART 2

### Part 2

Following exploration and reflection from Part 1, complete the "looks like," "works like" and "acts like" prototypes for your design, reiterated below.

### Part E (Optional)
### Servo Control with Joystick

In the class kit, you should be able to find the [Qwiic Servo Controller](https://www.sparkfun.com/products/16773) and [Micro Servo Motor SG51](https://www.adafruit.com/product/2201). The Qwiic Servo Controller will need external power supply to drive, which are included in your kit. Connect the servo controller to the miniPiTFT through qwiic connector and connect the external battery to the 2-Pin JST port (ower port) on the servo controller. Connect your servo to channel 2 on the controller, make sure the brown is connected to GND and orange is connected to PWM.

<img src="Servo_Setup.jpg" width="400"/>

In this exercise, we will be using the nice [ServoKit library](https://learn.adafruit.com/16-channel-pwm-servo-driver/python-circuitpython) developed by Adafruit! We will continue to use the `circuitpython` virtual environment we created. Activate the virtual environment and make sure to install the latest required libraries by running:

```
(circuitpython) pi@ixe00:~/Interactive-Lab-Hub/Lab 4 $ pip3 install -r requirements.txt
```

A servo motor is a rotary actuator or linear actuator that allows for precise control of angular or linear position. The position of a servo motor is set by the width of an electrical pulse, that is, we can use PWM (pulse-width modulation) to set and control the servo motor position. You can read [this](https://learn.adafruit.com/adafruit-arduino-lesson-14-servo-motors/servo-motors) to learn a bit more about how exactly a servo motor works.

Now that you have a basic idea of what a servo motor is, look into the script `qwiic_servo_example.py` we provide. In line 14, you should see that we have set up the min_pulse and max_pulse corresponding to the servo turning 0 - 180 degree. Try running the servo example code now and see what happens:

```
(circuitpython) pi@ixe00:~/Interactive-Lab-Hub/Lab 4 $ python servo_test.py
```

It is also possible to control the servo using the sensors mentioned in as in part A and part B, and/or from some of the buttons or parts included in your kit, the simplest way might be to chain Qwiic buttons to the other end of the Qwiic OLED. Like this:

<p align="center"> <img src="chaining.png"  width="200" ></p>

You can then call whichever control you like rather than setting a fixed value for the servo. For more information on controlling Qwiic devices, Sparkfun has several python examples, such as [this](https://learn.sparkfun.com/tutorials/qwiic-joystick-hookup-guide/all#python-examples).

We encourage you to try using these controls, **while** paying particular attention to how the interaction changes depending on the position of the controls. For example, if you have your servo rotating a screen (or a piece of cardboard) from one position to another, what changes about the interaction if the control is on the same side of the screen, or the opposite side of the screen? Trying and retrying different configurations generally helps reveal what a design choice changes about the interaction -- _make sure to document what you tried_!

### Part F
### Record

Document all the prototypes and iterations you have designed and worked on! Again, deliverables for this lab are writings, sketches, photos, and videos that show what your prototype:
* "Looks like": shows how the device should look, feel, sit, weigh, etc.
* "Works like": shows what the device can do
* "Acts like": shows how a person would interact with the device
Iteration 1:
In our past design, the distance sensor only faced one direction. Therefore, it only detected objects at a certain angle. In this iteration, we decided to better our design by letting the user hold a joystick which can change the angle of the sensor using the servo.
![IMG_9503002D8C76-1](https://user-images.githubusercontent.com/54753807/196012594-d22e0fad-fc18-4c3a-a770-0f30a87e3534.jpeg)

Question 1: What is the limit of servo to place the sensor
Question 2: When the servo hits the limit angle, what feedback should we give to the user.

We have to have a mapping function, and test different feedback(vibration, visual warning) on our users.

Iteration 2:
We simply add one more feature of the joystick, when the user presses the joystick, the servo will automatically sweep up and down to provide a wider range for the sensor. 

Question 1: When the sensor is sweeping, what should the visual alarm display? The distance will be constantly changing, and it will be hard for users to understand.

Conclusion:
Looks like: Our product should be minimalist in design yet provide accurate readings for the user interaction. Ideally it should look very simple and be light weight. Also, it should feel reliable and safe to the user. Which means, it has to provide sufficient feedback and interaction to the user to enrich his/hers VR experience. 

Works like: As it works much like a guard, it will display object and location information/warning to the user while they are blinded by the Quest 2 VR set, and ensure the users safety and trust in their overall VR experience.

Acts like: The interaction between the device and the user should also be minimalistic, because it is designed to be used while wearing a VR headset. Ideally, the user should be able to tell they are interacting with the device but also benefit from the information it provides.
