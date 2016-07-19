def checkio(*args):
    try:
        return max(args) - min(args)
    except ValueError:
        return 0
