from distutils.core import setup

setup(
    name = "Firefox-DPMS",
    version = "0.1.0",
    author = "Dino Duratović",
    author_email = "dinomol@mail.com",
    url = "https://github.com/dglava/firefox-dpms",
    description = "Disables DPMS when Firefox is playing video",
    license = "GNU GPLv3",
    install_requires = ["pulsectl"],

    scripts = ["bin/firefox-dpms"],
    data_files = [("/usr/lib/systemd/user", ["data/firefox-dpms.service"])]
    )
