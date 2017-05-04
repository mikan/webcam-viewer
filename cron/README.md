/cron
=====

cron scripts directory.

Sample `/etc/cron.d/webcam`:

```cron
SHELL=/bin/sh
PATH=/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin
10 * * * * motion /opt/git/webcam-viewer/cron/cleanup.py
0 8 * * * motion /opt/git/webcam-viewer/cron/backup-hourly.sh 08
5 8 * * * motion /opt/git/webcam-viewer/cron/backup-daily.sh
0 9 * * * motion /opt/git/webcam-viewer/cron/backup-hourly.sh 09
0 10 * * * motion /opt/git/webcam-viewer/cron/backup-hourly.sh 10
0 11 * * * motion /opt/git/webcam-viewer/cron/backup-hourly.sh 11
0 12 * * * motion /opt/git/webcam-viewer/cron/backup-hourly.sh 12
0 13 * * * motion /opt/git/webcam-viewer/cron/backup-hourly.sh 13
0 14 * * * motion /opt/git/webcam-viewer/cron/backup-hourly.sh 14
0 15 * * * motion /opt/git/webcam-viewer/cron/backup-hourly.sh 15
0 16 * * * motion /opt/git/webcam-viewer/cron/backup-hourly.sh 16
```

