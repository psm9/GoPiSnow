# GoPiSnow
GoPiGo robot controlled by voice command hotwords detected by Snowboy

I'm only a few months into using Python, and the Raspberry Pi and haven't used Github before, so forgive me if this is a bit rough.

I saw an article in MagPi about controlling a Raspberry Pi using Alexa. In trying to set that up, I stumbled on this solution instead using [Snowboy](http://docs.kitt.ai/snowboy/).
The code I changed is quite simple - just a couple changes to Snowboy's demo code.

You'll need:
1. Raspbery Pi (I used a Raspbperry Pi 3)
2. A [GoPiGo from Dexter Industries](https://www.dexterindustries.com/gopigo/)
3. USB microphone. [I used this one](https://www.amazon.com/Kinobo-Microphone-Desktop-Recognition-Software/dp/B00IR8R7WQ/ref=lp_3032939011_1_1?srs=3032939011&ie=UTF8&qid=1490623374&sr=8-1). It works fair. Your mileage may vary.

Once, the GoPiGo is built, setup VNC.  I updated the Raspbian software and installed the [newer version of VNC Connect](https://www.raspberrypi.org/documentation/remote-access/vnc/).

More info on GoPiGo Python programming is [here](https://www.dexterindustries.com/GoPiGo/programming/python-programming-for-the-raspberry-pi-gopigo/)

[Snowboy's Github page](https://github.com/kitt-ai/snowboy) is here. For the Raspberry pi, scroll down to "Precompiled Node Module" and follow the instructions.  Scroll down a bit more to "Dependencies" and install the necessary software.

Snowboy has further [documentation here](http://docs.kitt.ai/snowboy/).  They have a few demo python programs to play with, as well.

Once everything is installed, follow their instructions to train a voice model for your hotword(s) or play with their demo.py file or their demo2.py (for detecting 2 hotwords).

The GoPiSnow.py file is a minimally changed version of Snowboy's demo2.py.  The changes  are:
1. Import the gopigo module and import sleep from time - (Lines 4 and 5)
2. Define the variable "models" as a list of .pmdl files, as opposed to having to list them at the command line when running the program. (Line 21). Make sure you include the correct folder/file path
3. Several new functions defined to control various GoPiGo movements ("lefter", "righter", "dance",etc...) (Lines 23-86)
4. Commands to enable and reset the servo(for a camera) (Lines 93-94)
5. Adjust Snowboy's sensitivity. This part was trial and error to find a number minimize false positives, but also doesn't miss many commands. (Line 96)
6. Redefining "callbacks" as a set listing the new GoPiGo functions, instead of Snowboy's "Ding"/"Dong" commands (Line 98)

In order for it to work, you'll have to have downloaded and extracted all of the Snowboy files. Make sure the GoPiSnow.py file is in the same folder as snowboydecoder.py and snowboydetect.py. Make sure you have the right file paths for the hotword models (the pmdll files).

That's it. Just hit F5 and off you go.

Once you have this figured out, I would imagine you can control almost anything  a Raspberry Pi can do with a Snowboy Hotword
