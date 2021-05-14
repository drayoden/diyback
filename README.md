### my personal backup script 

* linux ubuntu (PoP_OS!)
* python
* gsutil
* targz
* automated (cron)
* check gcs stroage for retention period (not required for beta)

---

##  sudo code:
- open json config file (if it exists) for config - crete objects:
    - sources
    - excludes
    - destination folder
    - temp folder
- check if folders exist (if not, create or fail gracefully):
    - temp folder (create if not)
    - gcs bucket/folder (fail gracefully)
- set archive filename (data/time).tar.gz
- open/create log file in local temp folder
- open/create archive file in local temp folder
- start backup process
- move tar.gz file and log file to gcs


## using rsync...
- assume local directory structure (assumes on weekly full backup, six differential backups):
  - .yodaback
    * \full
    * \d1, \d2, .. \d6
- script needs command-line arguments (single char): f|F (full backup) OR 1, 2... - 6 (d1, d2, ... d6) this will determine how rsync will react and which folder will be archived to gcs


## cron stuff I can never remember...
Example of job definition:
```
 .---------------- minute (0 - 59)
 |  .------------- hour (0 - 23)
 |  |  .---------- day of month (1 - 31)
 |  |  |  .------- month (1 - 12) OR jan,feb,mar,apr ...
 |  |  |  |  .---- day of week (0 - 6) (Sunday=0 or 7) OR sun,mon,tue,wed,thu,fri,sat
 |  |  |  |  |
 *  *  *  *  * user-name  command to be executed
```



