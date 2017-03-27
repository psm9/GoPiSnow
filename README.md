# GoPiSnow
GoPiGo robot controlled by voice command hotwords detected by Snowboy

I'm very new at Github, Python, and the Raspberry Pi, so forgive me if this is a bit rough.
I saw an article in MagPi about controlling a Raspberry Pi using Alexa. In trying to set that up, I stumbled on this solution instead using [Snowboy](http://docs.kitt.ai/snowboy/)
The code I changed is quite simple - just a couple changes to Snowboy's demo code.

You'll need:
1. Raspbery Pi (I used a Raspbperry Pi 3)
2. A [GoPiGo from Dexter Industries](https://www.dexterindustries.com/gopigo/)
3. USB microphone. [I used this one](https://www.amazon.com/Kinobo-Microphone-Desktop-Recognition-Software/dp/B00IR8R7WQ/ref=lp_3032939011_1_1?srs=3032939011&ie=UTF8&qid=1490623374&sr=8-1). It works fair. Your mileage may vary.

Once, the GoPiGo is built, setup VNC.  I updated the Raspbian software and installed the [newer version of VNC Connect](https://www.raspberrypi.org/documentation/remote-access/vnc/).

More info on GoPiGo Python programming is [here](https://www.dexterindustries.com/GoPiGo/programming/python-programming-for-the-raspberry-pi-gopigo/)

Follow the instructions [here](http://docs.kitt.ai/snowboy/) to download and install Snowboy. Also, check out their [Github page](https://github.com/kitt-ai/snowboy).
In the downloads section, download and unpack the apppropriate tar file.  Then, follow the instructions to access the microphone.
They have a few demo python programs to play with, as well.

Once everything is installed, follow their instructions to train a voice model for your hotword(s) or play with their demo.py file or their demo2.py (for detecting 2 hotwords)

The GoPiSnow.py file is a minimally changed version of Snowboy's demo2.py.  The changes  are:
1. import the gopigo module and import sleep from time
2. define the variable "models" as a list of .pmdl files (as opposed to having to list them at the command line when running the program)
3. Several new functions defined to control various GoPiGo movements
4. The "Ding" and "Dong" callbacks have been redefined as a set listing the new GoPiGo functions

That's it. Once you have that working, it's pretty easy 
