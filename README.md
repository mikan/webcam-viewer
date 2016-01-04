webcam-viewer
=============

A simple webcam viewer built by HTML, CGI, and some script files.


```
/
├── cgi-bin [/usr/lib/cgi-bin]
│   ├── mdevents.cgi (event list viewer cgi)
│   └── mdevents.py (mdevents.cgi functions)
├── conf [/etc/motion]
│   ├── motion.conf (sample configuration file for motion)
│   └── serve-cgi-bin.conf (sample configuration file for mod_cgi)
├── cron
│   ├── backup-daily.sh (daily backup task)
│   ├── backup-hourly.sh (hourly backup task)
│   ├── cleanup.py (cleaner for old images)
│   └── thumb.py (thubnail generator)
└── www [/var/www/html]
    ├── css
    │   ├── lightbox.css
    │   └── screen.css
    ├── img
    │   ├── close.png
    │   ├── loading.gif
    │   ├── next.png
    │   └── prev.png
    ├── js
    │   ├── <jquery>
    │   ├── <lightbox>
    │   ├── <unslider>
    │   └── label_updater.js
    ├── index.html
    ├── live1.html
    ├── live2.html
    ├── timelapse1.html
    └── timelapse2.html
```

