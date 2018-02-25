# Night Owls Detector

The script finds out Devman's Night Owls, the users on Devman who send solutions for checking after 24:00 by theirs local time.
Time period after midnight is set by default in a variable <night_hours> as 6 hours, i.e. Night Owls are those users, who made 
their attempts after 24:00 till 6:00.


# Quickstart

Example of script launch on Linux, Python 3.5:

```bash

$ python3 seek_dev_nighters.py
```

Note, the script needs additional python modules to work. It would be installed by command:

```bash

$ pip3 install -r requirements.txt
```

# Output example

```
DEVMAN's Night Owls, who made their attmepts since 24:00 till 6:00 are:

IvanKumeyko:
   2018/02/05 00:18 MSK+0300
   2018/02/03 00:57 MSK+0300

OlegBoliuk:
   2018/02/04 02:51 MSK+0300
   2018/02/04 02:29 MSK+0300
   2018/02/04 01:10 MSK+0300
   2018/02/04 01:06 MSK+0300
   2018/02/04 01:00 MSK+0300
   2018/02/04 00:32 MSK+0300

RomanGagarin:
   2018/02/08 02:07 MSK+0300
   2018/02/08 02:02 MSK+0300
   2018/02/08 01:54 MSK+0300
   2018/02/08 01:49 MSK+0300
   2018/02/08 01:13 MSK+0300

SlavaSlz:
   2018/02/04 01:30 +07+0700
   2018/02/04 01:18 +07+0700

apaticmail:
   2018/02/12 01:23 MSK+0300
   2018/02/12 01:06 MSK+0300
   2018/02/03 00:32 MSK+0300

d1ggerr:
   2018/02/05 05:41 MSK+0300

e519a120ae824df4:
   2018/02/09 00:03 MSK+0300

evgen_sobolev:
   2018/02/08 00:08 MSK+0300

id2794684:
   2018/02/10 01:59 MSK+0300

id357826325:
   2018/02/09 00:24 MSK+0300
   2018/02/09 00:12 MSK+0300

id460393476:
   2018/02/09 02:18 MSK+0300

id93321377:
   2018/02/12 01:46 MSK+0300

igorzakhar:
   2018/02/07 00:08 MSK+0300

krasavets:
   2018/02/08 05:32 MSK+0300
   2018/02/08 02:12 MSK+0300
   2018/02/07 03:36 MSK+0300
   2018/02/07 03:22 MSK+0300
   2018/02/06 02:49 MSK+0300
   2018/02/06 02:33 MSK+0300
   2018/02/06 02:18 MSK+0300
   2018/02/05 03:31 MSK+0300
   2018/02/05 03:04 MSK+0300

ld38475474:
   2018/02/08 02:58 +05+0500
   2018/02/08 02:33 +05+0500
   2018/02/07 02:01 +05+0500
   2018/02/07 01:15 +05+0500
   2018/02/07 00:29 +05+0500
   2018/02/05 04:24 +05+0500

pspiskunov:
   2018/02/11 02:16 MSK+0300
   2018/02/11 01:59 MSK+0300
   2018/02/11 00:55 MSK+0300
```

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
