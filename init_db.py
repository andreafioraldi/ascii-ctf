import os


if __name__ == "__main__":
    db = os.environ.get('DATABASE_URL', None)
    if db is None:
        import chals
    else:
        path = db.split('///')[1]
        if not os.path.isfile(path):
            import chals
