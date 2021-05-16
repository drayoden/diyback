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
* edit "user" crontab: `crontab -e`
* python:
```
chmod +x <python file>
* * * * * <pwd>/path/python-job.py
# current crontab for backup:
05 3 * * * /home/sysadm/.local/bin/yodaback.py >> /home/sysadm/.local/bin/yodaback.log
```

---

### using rsync...
- initial run -> establish local backup folder (config.json) - verify/create
- configr.json:
    * last full backup (name or date or ?) -- lastfull
    * last diff backup (name or date or number or ?) -- lastdiff
    * number of diff backups (static) -- diffbacks
    * sources need path AND name for rsync function
    * excludes can now be moved to the rsync phase of the process. tar file creatation can just backup the full or diff folder without excludes.
- script needs logic to determine which type of backup (full/diff). this will determine how rsync will react and which incremental folder will be archived to gcs. this can be determined using the lastdiff and diffbacks from configr.json 

## sudo code (rsync version):
- open json config file (if it exists) for config - crete objects:
    - sources:
        * for each source create `<localarch>/<full|dx>/<name>/`
    - excludes - create temporary ./exfile.txt file 
    - gcs destination folder (verify)
    - temp folder create
- set archive/log filename `<date>-<time><f|d>.<tar.gz|log>` -- 'f' -> full OR 'd' -> diff
- open/create log file in local temp folder
- open/create archive file in local temp folder
- start backup process
- move tar.gz file and log file to gcs


- rsycn tests:
    * `--delete-before` -- will exclude any file/folder that has been deleted
        ```
        - used for full backup:
        rsync -a /home/sysadm/data/diyback/test/ /home/sysadm/.yodabak/full/ --delete-before

        - used for diff backup:
        rsync -a --compare-dest=/home/sysadm/.yodabak/full/ /home/sysadm/data/diyback/test/ /home/sysadm/.yodabak/d4/ --delete-before

        - exclude all node_modules directories:
        rsync -a --exclude=node_modules test/ /home/sysadm/.yodabak/full

        - previous plus exclude .git direcotories:
        rsync -a --exclude=node_modules --exclude=.git test/ /home/sysadm/.yodabak/full

        - use a input file to exclude files and directories:
        rsync -a --exclude-from='./exfile.txt' test/ /home/sysadm/.yodabak/full

        ``` 
- some other commands I forget or didn't know about:
    * `touch -t 2104210000 f5.txt ` -- crete a file with a specific date
    * `ls -lt` or `ls -ltr` -- sort files by date
    * `tar -tvf <filename>.tar.gz` -- list tar.gz file contents


