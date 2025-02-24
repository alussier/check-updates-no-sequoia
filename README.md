# check-updates-no-sequoia

This script checks for macOS updates, but filters out Sequoia.

> [!CAUTION]
> generated with ChatGPT (o3-mini-high)

> [!CAUTION]
> untested until next 14.x update comes out

## Installation
```
crontab -e
0 */6 * * * /opt/homebrew/bin/python3 /Users/adam/git/check-updates-no-sequoia/update_manager.py
```
