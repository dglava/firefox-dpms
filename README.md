# Firefox-DPMS
Disables DPMS (screen blanking) when Firefox is playing back video.

I couldn't find a way to make Firefox suspend the DPMS settings when
it was playing back videos on website (YouTube for example). This
accomplishes exactly that, but in a hacky way.

It works by checking if there are audio streams coming from Firefox
with Pulseaudio. The idea is that when you're watching videos, audio
is also present. When it detects Firefox audio, it turns DPMS off and
restores it again when Firefox's audio disappears, i.e.: the video
is closed.

#### How to install
Run `$ python setup.py install`   
It requires [python-pulse-control](https://github.com/mk-fg/python-pulse-control)
and obviously Pulseaudio.
Arch Linux users can install it from the provided PKGBUILD.

#### How to use
Run `$ firefox-dpms`

or

Enable the systemd user service `$ systemctl --user enable firefox-dpms`
