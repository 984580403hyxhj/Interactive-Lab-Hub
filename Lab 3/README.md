
**NAMES OF COLLABORATORS HERE**

Akhil Uddandam, au83@cornell.edu
Jingze Xue, jx288

[![Watch the video](https://user-images.githubusercontent.com/1128669/135009222-111fe522-e6ba-46ad-b6dc-d1633d21129c.png)](https://www.youtube.com/embed/Q8FWzLMobx0?start=19)

In this lab, we want you to design interaction with a speech-enabled device--something that listens and talks to you. This device can do anything *but* control lights (since we already did that in Lab 1).  First, we want you first to storyboard what you imagine the conversational interaction to be like. Then, you will use wizarding techniques to elicit examples of what people might say, ask, or respond.  We then want you to use the examples collected from at least two other people to inform the redesign of the device.

We will focus on **audio** as the main modality for interaction to start; these general techniques can be extended to **video**, **haptics** or other interactive mechanisms in the second part of the Lab.

## Prep for Part 1: Get the Latest Content and Pick up Additional Parts 

### Pick up Web Camera If You Don't Have One

Students who have not already received a web camera will receive their [IMISES web cameras](https://www.amazon.com/Microphone-Speaker-Balance-Conference-Streaming/dp/B0B7B7SYSY/ref=sr_1_3?keywords=webcam%2Bwith%2Bmicrophone%2Band%2Bspeaker&qid=1663090960&s=electronics&sprefix=webcam%2Bwith%2Bmicrophone%2Band%2Bsp%2Celectronics%2C123&sr=1-3&th=1) on Thursday at the beginning of lab. If you cannot make it to class on Thursday, please contact the TAs to ensure you get your web camera. 

### Get the Latest Content

As always, pull updates from the class Interactive-Lab-Hub to both your Pi and your own GitHub repo. There are 2 ways you can do so:

**\[recommended\]**Option 1: On the Pi, `cd` to your `Interactive-Lab-Hub`, pull the updates from upstream (class lab-hub) and push the updates back to your own GitHub repo. You will need the *personal access token* for this.

```
pi@ixe00:~$ cd Interactive-Lab-Hub
pi@ixe00:~/Interactive-Lab-Hub $ git pull upstream Fall2022
pi@ixe00:~/Interactive-Lab-Hub $ git add .
pi@ixe00:~/Interactive-Lab-Hub $ git commit -m "get lab3 updates"
pi@ixe00:~/Interactive-Lab-Hub $ git push
```

Option 2: On your your own GitHub repo, [create pull request](https://github.com/FAR-Lab/Developing-and-Designing-Interactive-Devices/blob/2022Fall/readings/Submitting%20Labs.md) to get updates from the class Interactive-Lab-Hub. After you have latest updates online, go on your Pi, `cd` to your `Interactive-Lab-Hub` and use `git pull` to get updates from your own GitHub repo.

## Part 1.

### Text to Speech 

In this part of lab, we are going to start peeking into the world of audio on your Pi! 

We will be using the microphone and speaker on your webcamera. In the home directory of your Pi, there is a folder called `text2speech` containing several shell scripts. `cd` to the folder and list out all the files by `ls`:

```
pi@ixe00:~/text2speech $ ls
Download        festival_demo.sh  GoogleTTS_demo.sh  pico2text_demo.sh
espeak_demo.sh  flite_demo.sh     lookdave.wav
```

You can run these shell files by typing `./filename`, for example, typing `./espeak_demo.sh` and see what happens. Take some time to look at each script and see how it works. You can see a script by typing `cat filename`. For instance:

```
pi@ixe00:~/text2speech $ cat festival_demo.sh 
#from: https://elinux.org/RPi_Text_to_Speech_(Speech_Synthesis)#Festival_Text_to_Speech

echo "Just what do you think you're doing, Dave?" | festival --tts
```

Now, you might wonder what exactly is a `.sh` file? Typically, a `.sh` file is a shell script which you can execute in a terminal. The example files we offer here are for you to figure out the ways to play with audio on your Pi!

You can also play audio files directly with `aplay filename`. Try typing `aplay lookdave.wav`.

\*\***Write your own shell file to use your favorite of these TTS engines to have your Pi greet you by name.**\*\*

(This shell file should be saved to your own repo for this lab.)
https://github.com/984580403hyxhj/Interactive-Lab-Hub/blob/Fall2022/Lab%203/my_text_to_speech.sh
https://youtube.com/shorts/8eZ6nFbNR-0?feature=share

Bonus: If this topic is very exciting to you, you can try out this new TTS system we recently learned about: https://github.com/rhasspy/larynx

### Speech to Text

Now examine the `speech2text` folder. We are using a speech recognition engine, [Vosk](https://alphacephei.com/vosk/), which is made by researchers at Carnegie Mellon University. Vosk is amazing because it is an offline speech recognition engine; that is, all the processing for the speech recognition is happening onboard the Raspberry Pi. 

In particular, look at `test_words.py` and make sure you understand how the vocab is defined. 
Now, we need to find out where your webcam's audio device is connected to the Pi. Use `arecord -l` to get the card and device number:
```
pi@ixe00:~/speech2text $ arecord -l
**** List of CAPTURE Hardware Devices ****
card 1: Device [Usb Audio Device], device 0: USB Audio [USB Audio]
  Subdevices: 1/1
  Subdevice #0: subdevice #0
```
The example above shows a scenario where the audio device is at card 1, device 0. Now, use `nano vosk_demo_mic.sh` and change the `hw` parameter. In the case as shown above, change it to `hw:1,0`, which stands for card 1, device 0.  

Now, look at which camera you have. Do you have the cylinder camera (likely the case if you received it when we first handed out kits), change the `-r 16000` parameter to `-r 44100`. If you have the IMISES camera, check if your rate parameter says `-r 16000`. Save the file using Write Out and press enter.

Then try `./vosk_demo_mic.sh`

\*\***Write your own shell file that verbally asks for a numerical based input (such as a phone number, zipcode, number of pets, etc) and records the answer the respondent provides.**\*\*
https://github.com/984580403hyxhj/Interactive-Lab-Hub/blob/Fall2022/Lab%203/ask_phone_num.sh

https://youtube.com/shorts/5IlWVPzUXFc?feature=share

### Serving Pages

In Lab 1, we served a webpage with flask. In this lab, you may find it useful to serve a webpage for the controller on a remote device. Here is a simple example of a webserver.

```
pi@ixe00:~/Interactive-Lab-Hub/Lab 3 $ python server.py
 * Serving Flask app "server" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 162-573-883
```
From a remote browser on the same network, check to make sure your webserver is working by going to `http://<YourPiIPAddress>:5000`. You should be able to see "Hello World" on the webpage.

### Storyboard

Storyboard and/or use a Verplank diagram to design a speech-enabled device. (Stuck? Make a device that talks for dogs. If that is too stupid, find an application that is better than that.) 

\*\***Post your storyboard and diagram here.**\*\*

Write out what you imagine the dialogue to be. Use cards, post-its, or whatever method helps you develop alternatives or group responses. 

User: “I want to make hotpot Steve, what do I need?’
Device: here is what you need for hotpot, hotpot sause, meat slice, and cabbage
User: Great, I have those. How do I begin?
Device: add a lot of water and the sause in the pot, let it heat for 10 minutes, until the water is boiling
User: Okay, the water is boiling. Please remind me to check back in 10 minutes.
Device:will remind you in ten minutes… beep beep beep, ten minutes reminder
User: Thanks for the reminder, Steve. What do I do next?
Device:Now, Add the cabbage, and the meet slice. Then wait for 5 more minutes, the hotpodt is ready
User: Great. Thank you so much Steve. This looks delicious.




\*\***Please describe and document your process.**\*\*

Our device, Steve, gives the user instructions on how to cook popular dishes. When asked, the devices interact with the user by listing out the required ingredients for cooking. After confirming with the user that all the ingredients are available, the device begins instructing the user step by step on how to cook the dish, even setting alarms or reminders to completion. The user will also be able to check whether he has performed an instruction correctly by using the webcam which will use computer vision to confirm with the user whether a step has been completed correctly or not. 

### Acting out the dialogue

Find a partner, and *without sharing the script with your partner* try out the dialogue you've designed, where you (as the device designer) act as the device you are designing.  Please record this interaction (for example, using Zoom's record feature).

\*\***Describe if the dialogue seemed different than what you imagined when it was acted out, and how.**\*\*

https://youtube.com/shorts/HyjFpaaj6jE?feature=share


### Wizarding with the Pi (optional)
In the [demo directory](./demo), you will find an example Wizard of Oz project. In that project, you can see how audio and sensor data is streamed from the Pi to a wizard controller that runs in the browser.  You may use this demo code as a template. By running the `app.py` script, you can see how audio and sensor data (Adafruit MPU-6050 6-DoF Accel and Gyro Sensor) is streamed from the Pi to a wizard controller that runs in the browser `http://<YouPiIPAddress>:5000`. You can control what the system says from the controller as well!

\*\***Describe if the dialogue seemed different than what you imagined, or when acted out, when it was wizarded, and how.**\*\*

The dialogue seemed different then anticipated as there was lag between the conversations and sometimes left the user confused on to whether or not the device was still functioning. Also the interaction was set up to go in one direction as there was a clear line or path to guiding the interactions. We will need to fix this by creating a flowchart or decision tree to guide the conversation which can go in many different directions. This will make our system much more like an AI system. 




# Lab 3 Part 2

For Part 2, you will redesign the interaction with the speech-enabled device using the data collected, as well as feedback from part 1.

## Prep for Part 2

1. What are concrete things that could use improvement in the design of your device? For example: wording, timing, anticipation of misunderstandings...]

Fault tolerance, when the system doesn’t recognize the user input, it should tell the user. Otherwise it would cause more confusion and misinterpretation of interactive data. This can be achieved by changing the dialog and adding more dialog interactions that ask the user such as, “Did you mean…..” to account for any sensory errors. 

Through more interaction with the user, in part 1, we noticed that simply telling the user what to do still causes a lot of uncertainty to the users. Thus we can add more interactions to confirm users’ intentions and actions. This can be achieved by using the webcam, the system can tell what the users are doing, and give them feedback based on their physical action. This cumulative detection of visual and auditory data, will enhance our devices predictive accuracy and overall interaction with the user.

In part 1, the users told us that the lag time was too long between interactions. The long wait time is not only annoying, but it also concerns the users whether the system is functioning properly and diminishes the simple interaction emulation of real life conversation. However, it is hard for us to change the lag time, due to both human and technical reasons, we can add other interactions to fill the gap in the waiting space, to tell users the system is working properly. This can be done by adding more adaptive interactions into the dialog.


2. What are other modes of interaction _beyond speech_ that you might also use to clarify how to interact?

To enhance our user interactions, we will also be using webcams while complementing our auditory sensors. Instead of only taking speech information from the users, we will use the webcams to input video information and provide a more accurate predictive model to access actions and provide an overall better user interaction. This also makes the system more efficient and trustworthy to the user as it acts similar to that of a human interaction (ie eyes and mouth interactions).





3. Make a new storyboard, diagram and/or script based on these reflections.
Script:

 

*Above is the flowchart or decision tree we modeled our system to follow. This is a revised interaction map to our part 1 prototype and includes a complete interaction diagram.

Storyboard:



## Prototype your system

The system should:
* use the Raspberry Pi 
* use one or more sensors
* require participants to speak to it. 


*Document how the system works*
*Include videos or screencaptures of both the system and the controller.*

To enable this interaction, we used the raspberry pi as our computer and the webcam to output speech as well as input visual information. We used a flowchart to map the computer interaction with the user’s input and guide the conversation. The device will recognize user voice input, and return a desired cooking recipe. Users can use the webcam to seek additional help.

More details are in this video(both videos are unscripted and the later was enhanced after taking into account feedback from our first user).

https://youtu.be/VOHNcTz0-Z8
https://youtu.be/fxbCMFr4iBE

## Test the system
Try to get at least two people to interact with your system. (Ideally, you would inform them that there is a wizard _after_ the interaction, but we recognize that can be hard.)







Answer the following:

### What worked well about the system and what didn't?

The dialog worked well, I think using jokes to fill the gap between processing really makes the interaction more interesting and avoids awkward lagging. Also the dialog covers both tester’s normal behavior which is good.

What didn’t work is that although we designed the interaction with the cameras, the users are not aware of it. They just used it as a speaker. Also when giving instructions about how to make food, the users don’t really know when the instructions ends. To fix these, we changed the script for the second tester, to remind them they can use the camera to check their status.

### What worked well about the controller and what didn't?

\*\**your answer here*\*\*
Other than not telling our first tester about how to use the camera, it is very intuitive to use, the second tester immediately knew how to use it(it is intuitive to face the front of the carema to the food they are making)

What didn’t work is that we forgot sometimes during cooking, the users don’t have a hand available to hold the camera. One possible way to fix it is to fix the camera on top of the stove. When the user asks for carema help, it will turn on automatically.


### What lessons can you take away from the WoZ interactions for designing a more autonomous version of the system?

\*\**your answer here*\*\*
Having a flowchart is very important to cover a lot more user interactions.
Fault tolerance is very important, and it should be added in a flexible way, since we cannot predict what the user will interact with the system.

### How could you use your system to create a dataset of interaction? What other sensing modalities would make sense to capture?

To future enhance our system, we can collect a dataset which includes user preferences of food, cooking styles, allergies tolerance, etc to provide more valuable information the next time. We can also learn from the speech2Text and webcam assessing errors to enhance our predictive model and provide more accurate feedback. We can also collect data when users are confused and seek help from the camera.


Heat sensor, motion sensor, and weight sensor can also be used to expand this device into a smart kitchen, which keeps track of the heat on the stove, motion of the user, and weight on the stove respectively. 
With all these sensors, we can help the user to make food in a more accurate and effective way (measuring the substances added into the pot, adjusting the heat automatically, etc). Furthermore, we can also use it to ensure better kitchen safety by making sure the stove is not on for a long time etc using the added sensors.
