webcam-viewer
=============

A simple webcam viewer built with HTML and Python scripts.

## Key Features

* Live View
* Timelapse Recording and Comparing
* Motion Events Gathering

```
/
├── cgi-bin [/usr/lib/cgi-bin]
│   ├── mdevents.cgi (event list viewer cgi)
│   └── mdevents.py (mdevents.cgi functions)
├── conf [/etc/motion, /etc/apache2/conf-enabled]
│   ├── motion.conf (sample configuration file for motion)
│   └── serve-cgi-bin.conf (sample configuration file for mod_cgi)
├── cron
│   ├── backup-daily.sh (daily backup task)
│   ├── backup-hourly.sh (hourly backup task)
│   ├── cleanup.py (cleaner for old images)
│   └── thumb.py (thumbnail generator)
└── www [/var/www/html]
    ├── css
    │   ├── <lightbox>
    │   └── screen.css
    ├── img
    │   ├── close.png
    │   ├── loading.gif
    │   ├── next.png
    │   └── prev.png
    ├── js
    │   ├── <jquery>
    │   ├── <lightbox>
    │   └── label_updater.js
    ├── index.html
    ├── live1.html
    ├── live2.html
    ├── timelapse1.html
    └── timelapse2.html
```

## Requirements

* [motion](https://packages.debian.org/stable/motion)
* [apache2](https://packages.debian.org/stable/apache2)
* [python-pil](https://packages.debian.org/stable/python-pil)

## Included Libraries

* [jQuery 1.10.2](https://jquery.com/) (MIT License)
* [jQuery Blinds 0.9](http://www.littlewebthings.com/projects/blinds) (MIT License)
* [jQuery Lazy Load 1.9.1](http://www.appelsiini.net/projects/lazyload) (MIT License)
* [Lightbox 2.6](http://lokeshdhakar.com/projects/lightbox2/) (MIT License)

## License

webcam-viewer licensed under the [BSD 3-Clause License](LICENSE).

