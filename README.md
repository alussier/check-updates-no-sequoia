# check-updates-no-sequoia

This script checks for macOS updates, but filters out Sequoia.

> [!CAUTION]
> generated with ChatGPT (o3-mini-high)

This script checks for macOS (including Safari etc.) updates and automatically installs them, but filters out Sequoia.

## Installation
ex: run every 6 hours
```
crontab -e
0 */6 * * * /opt/homebrew/bin/python3 /Users/adam/git/check-updates-no-sequoia/update_manager.py
```

## You have new mail.
```
You have new mail.
❯ mail
Mail version 8.1 6/6/93.  Type ? for help.
"/var/mail/adam": 1 message 1 new
>N  1 adam@Adams-Air.local  Tue Mar 11 18:07  18/753   "Cron <adam@Adams-Air>"
? p
To: adam@Adams-Air.localdomain adam@Adams-Air.localdomain
Subject: Re: Cron <adam@Adams-Air> /opt/homebrew/bin/python3 /Users/adam/git/check-updates-no-sequoia/update_manager.py

? d
? q
```