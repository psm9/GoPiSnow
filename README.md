# GoPiSnow
GoPiGo robot controlled by voice command hotwords detected by Snowboy

I'm very new at Github, Python, and the Raspberry Pi, so forgive me if this is a bit rough.
I saw an article in MagPi about controlling a Raspberry Pi using Alexa. In trying to set that up, I stumbled on thiss ssolution instead using [Snowboy](http://docs.kitt.ai/snowboy/)
The code I changed is quite simple - just a couple changes to Snowboy's demo code.

You'll need:
1. Raspbery Pi (I used a Raspbperry Pi 3)
2. A [GoPiGo from Dexter Industries](https://www.dexterindustries.com/gopigo/)
3. USB microphone. [I used this one](https://www.amazon.com/Kinobo-Microphone-Desktop-Recognition-Software/dp/B00IR8R7WQ/ref=lp_3032939011_1_1?srs=3032939011&ie=UTF8&qid=1490623374&sr=8-1). It works fair. Your mileage may vary.

Once, the GoPiGo is built, setup VNC.  I updated the Raspbian software and installed the [newer version of VNC Connect](https://www.raspberrypi.org/documentation/remote-access/vnc/).

Follow the instructions [here](http://docs.kitt.ai/snowboy/) to download and install Snowboy.
In the downloads section, download and unpack the apppropriate tar file
