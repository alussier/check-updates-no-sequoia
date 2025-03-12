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
