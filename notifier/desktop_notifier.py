from plyer import notification

def send_desktop_alert(title, message):
    notification.notify(
        title=title,
        message=message,
        timeout=10  # seconds
    )
