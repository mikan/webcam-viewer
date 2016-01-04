/cron
=====

cron scripts directory.

Sample crontab:

```
10 * * * * /<path_to_cron_dir>/mdclean.py
0 8 * * * /<path_to_cron_dir>/backup-hourly.sh 08
5 8 * * * /<path_to_cron_dir>/backup-daily.sh
0 9 * * * /<path_to_cron_dir>/backup-hourly.sh 09
0 10 * * * /<path_to_cron_dir>/backup-hourly.sh 10
0 11 * * * /<path_to_cron_dir>/backup-hourly.sh 11
0 12 * * * /<path_to_cron_dir>/backup-hourly.sh 12
0 13 * * * /<path_to_cron_dir>/backup-hourly.sh 13
0 14 * * * /<path_to_cron_dir>/backup-hourly.sh 14
0 15 * * * /<path_to_cron_dir>/backup-hourly.sh 15
0 16 * * * /<path_to_cron_dir>/backup-hourly.sh 16
```
