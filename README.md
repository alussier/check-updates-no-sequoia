# check-updates-no-sequoia

generated with chatgpt o3-mini-high

This script checks for macOS updates, but filters out Sequoia.  Will modify to auto-update once I've tested it works with the next 14.x update

WARNING untested

## Installation
```
crontab -e
0 */6 * * * /opt/homebrew/bin/python3 /Users/adam/git/check-updates-no-sequoia/update_manager.py
```
