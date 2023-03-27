def main(seconds):
    negative = seconds < 0
    seconds = abs(seconds)
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = seconds % 60
    if negative:
        return f"-{hours:01}:{minutes:02}:{seconds:02}"
    else:
        return f"{hours:01}:{minutes:02}:{seconds:02}"
