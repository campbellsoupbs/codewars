def make_readable(seconds):
    if seconds < 60:
        sec = int(seconds)
        min = 0
        hour = 0
    elif seconds < 3600:
        min = int(seconds/60)
        sec = int(((seconds/60) - min)*60)
        hour = 0
    else:
        hour = int(seconds/3600)
        rawmin = ((seconds/3600) - hour)*60
        min = int(rawmin)
        sec = round((rawmin - min)*60)

    return f'{hour:02}:{min:02}:{sec:02}'