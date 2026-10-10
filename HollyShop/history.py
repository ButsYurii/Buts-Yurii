from datetime import datetime


history = []


def add_history(action):
    """Записує дію в історію магазину."""
    if not isinstance(action, str) or not  action.strip():
        return False

    record = {
        "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "action": action.strip(),
    }

    history.append(record)

    return True