# BigClock-lib v2
This repo was archived on 2022-10-11. I didn't have any intention of coming back to it as I'd mostly been satisfied with a working clock.

However, in recent weeks I've been picking up and improving many of my abandoned projects. This is one of them. 

I have a bunch of Raspberry Pi Pico boards laying around and I genuinely enjoy working with the RP2040, so I've decided to use this over the [Adafruit Metro M4 Express Airlift](https://www.digikey.com/en/products/detail/adafruit-industries-llc/4000/10123799) I'd been using.

Anywho, between when I last worked on this, and now, I've picked up quite the distaste for Python. Micro/CircuitPython is amazing, but it's just not for me, so I've stuck with C++.

This code is pretty much just a trimmed down version of the Arduino stopwatch from the original version, then modified to function as a clock.

The RPi synchronizes with an NTP server every 5 minutes as I've found the internal clock to drift several seconds out of sync in this short time period -- you could pretty easily hack an RTC into this code, but I don't feel like dealing with that, so this "good-enough" solution prevails.

My original construction had the LEDs for segment 1 in a different order than the rest. I've fixed that for this version as it allows for less awful code.

---

I originally gathered the files from Ivan Miranda's website. However, it looks as though the video is no longer available, so I'll link to an [archive of the webpage](https://web.archive.org/web/20210126233712/https://ivanmiranda.com/pages/diy-big-digital-clock). I've also gone ahead and created an [archive of the STL and F3D files](https://www.archi.vet/archives/big-clock-ivan-miranda/).