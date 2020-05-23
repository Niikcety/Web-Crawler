class CleanExit(object):
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, exc_tb):
        if exc_type is KeyboardInterrupt:
            print('Saving records and leaving.. \n Bye!')
            return
        return exc_type is None
