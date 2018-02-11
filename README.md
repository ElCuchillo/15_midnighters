# Night Owls Detector

The script finds out Devman's Night Owls, the users on Devman who send solutions for checking after 24:00 by theirs local time.
Time period after midnight is set by default in a variable <night_hours> as 6 hours, i.e. Night Owls are those users, who made 
their attempts after 24:00 till 6:00.


# Quickstart

Example of script launch on Linux, Python 3.5:

```bash

$ python3 seek_dev_nighters.py
```

Note, the script needs python module 'pytz' to work. It would be installed by command:

```bash

$ pip3 instal pytz
```

# Output example

```
DEVMAN's Night Owls, who made their attmepts since 24:00 till 6:00 are:

pspiskunov at 2018-02-11 02:16 MSK+0300, timezone Europe/Moscow
pspiskunov at 2018-02-11 01:59 MSK+0300, timezone Europe/Moscow
pspiskunov at 2018-02-11 00:55 MSK+0300, timezone Europe/Moscow
id2794684 at 2018-02-10 01:59 MSK+0300, timezone Europe/Moscow
id460393476 at 2018-02-09 02:18 MSK+0300, timezone Europe/Moscow
id357826325 at 2018-02-09 00:24 MSK+0300, timezone Europe/Moscow
id357826325 at 2018-02-09 00:12 MSK+0300, timezone Europe/Moscow
e519a120ae824df4 at 2018-02-09 00:03 MSK+0300, timezone Europe/Moscow
krasavets at 2018-02-08 05:32 MSK+0300, timezone Europe/Moscow
krasavets at 2018-02-08 02:12 MSK+0300, timezone Europe/Moscow
RomanGagarin at 2018-02-08 02:07 MSK+0300, timezone Europe/Moscow
RomanGagarin at 2018-02-08 02:02 MSK+0300, timezone Europe/Moscow
RomanGagarin at 2018-02-08 01:54 MSK+0300, timezone Europe/Moscow
RomanGagarin at 2018-02-08 01:49 MSK+0300, timezone Europe/Moscow
RomanGagarin at 2018-02-08 01:13 MSK+0300, timezone Europe/Moscow
ld38475474 at 2018-02-08 02:58 +05+0500, timezone Asia/Yekaterinburg
ld38475474 at 2018-02-08 02:33 +05+0500, timezone Asia/Yekaterinburg
evgen_sobolev at 2018-02-08 00:08 MSK+0300, timezone Europe/Moscow
krasavets at 2018-02-07 03:36 MSK+0300, timezone Europe/Moscow
krasavets at 2018-02-07 03:22 MSK+0300, timezone Europe/Moscow
igorzakhar at 2018-02-07 00:08 MSK+0300, timezone Europe/Moscow
ld38475474 at 2018-02-07 02:01 +05+0500, timezone Asia/Yekaterinburg
ld38475474 at 2018-02-07 01:15 +05+0500, timezone Asia/Yekaterinburg
ld38475474 at 2018-02-07 00:29 +05+0500, timezone Asia/Yekaterinburg
krasavets at 2018-02-06 02:49 MSK+0300, timezone Europe/Moscow
krasavets at 2018-02-06 02:33 MSK+0300, timezone Europe/Moscow
krasavets at 2018-02-06 02:18 MSK+0300, timezone Europe/Moscow
d1ggerr at 2018-02-05 05:41 MSK+0300, timezone Europe/Moscow
krasavets at 2018-02-05 03:31 MSK+0300, timezone Europe/Moscow
krasavets at 2018-02-05 03:04 MSK+0300, timezone Europe/Moscow
ld38475474 at 2018-02-05 04:24 +05+0500, timezone Asia/Yekaterinburg
IvanKumeyko at 2018-02-05 00:18 MSK+0300, timezone Europe/Moscow
OlegBoliuk at 2018-02-04 02:51 MSK+0300, timezone Europe/Moscow
OlegBoliuk at 2018-02-04 02:29 MSK+0300, timezone Europe/Moscow
OlegBoliuk at 2018-02-04 01:10 MSK+0300, timezone Europe/Moscow
OlegBoliuk at 2018-02-04 01:06 MSK+0300, timezone Europe/Moscow
OlegBoliuk at 2018-02-04 01:00 MSK+0300, timezone Europe/Moscow
OlegBoliuk at 2018-02-04 00:32 MSK+0300, timezone Europe/Moscow
SlavaSlz at 2018-02-04 01:30 +07+0700, timezone Asia/Novosibirsk
SlavaSlz at 2018-02-04 01:18 +07+0700, timezone Asia/Novosibirsk
IvanKumeyko at 2018-02-03 00:57 MSK+0300, timezone Europe/Moscow
apaticmail at 2018-02-03 00:32 MSK+0300, timezone Europe/Moscow
apaticmail at 2018-02-03 00:09 MSK+0300, timezone Europe/Moscow
igorzakhar at 2018-02-03 00:00 MSK+0300, timezone Europe/Moscow
```

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
