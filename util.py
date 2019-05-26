import time  # For current_time_ms


def current_time_ms():
    return int(round(time.time() * 1000))
