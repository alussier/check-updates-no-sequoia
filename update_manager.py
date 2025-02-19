#!/usr/bin/env python3
import subprocess
import sys
import shutil

def get_update_list():
    """
    Retrieves the list of available updates using the 'softwareupdate -l' command.
    """
    try:
        result = subprocess.run(
            ["/usr/sbin/softwareupdate", "-l"],
            capture_output=True,
            text=True,
            check=True
        )
    except subprocess.CalledProcessError as e:
        print("Error listing updates:", e)
        sys.exit(1)
    return result.stdout

def parse_updates(output, blocked_pattern):
    """
    Parses the output of 'softwareupdate -l' and returns a list of update labels
    that do NOT contain the blocked pattern.
    """
    eligible_updates = []
    # The update lines typically start with an asterisk (*)
    for line in output.splitlines():
        line = line.strip()
        if line.startswith("*"):
            # Remove the '*' and any extra whitespace.
            update_label = line.lstrip("* ").strip()
            if blocked_pattern in update_label:
                print(f"Skipping blocked update: {update_label}")
            else:
                print(f"Found eligible update: {update_label}")
                eligible_updates.append(update_label)
    return eligible_updates

def show_sticky_notification(title, message):
    """
    Uses terminal-notifier to display a sticky macOS notification.
    The '-timeout 0' argument makes the notification persist until dismissed.
    FIXME the above is not true, set terminal-notifier notifications to be alerts
    """
    try:
        subprocess.run(
            ["/opt/homebrew/bin/terminal-notifier", "-title", title, "-message", message, "-timeout", "0"],
            check=True
        )
    except subprocess.CalledProcessError as e:
        print("Error showing notification:", e)

def main():
    # Define the blocked pattern (e.g., a major upgrade to macOS "Sequoia 15").
    BLOCKED_PATTERN = "Sequoia 15"  # Adjust this string if needed

    print("Checking for available updates...")
    output = get_update_list()

    if "No new software available" in output:
        print("No updates available.")
        show_sticky_notification("Software Update Alert", "No new updates available.")
        return

    eligible_updates = parse_updates(output, BLOCKED_PATTERN)

    if eligible_updates:
        # Create a message listing the eligible updates.
        update_message = "Available update" + ("s: " if len(eligible_updates) > 1 else ": ") + ", ".join(eligible_updates)
        show_sticky_notification("Software Update Alert", update_message)
    else:
        print("No eligible updates found for notification.")
        show_sticky_notification("Software Update Alert", "No eligible updates available.")

if __name__ == "__main__":
    if not sys.platform.startswith("darwin"):
        print("This script is intended to run on macOS.")
        sys.exit(1)
    main()
