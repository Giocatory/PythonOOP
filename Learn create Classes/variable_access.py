class Access:
    def __init__(self):
        self._Access__private = None
        self.public = 'public var'
        self._protected = 'protected var'

        self._access__private = None
        self.__private = 'private var'

    @property
    def protected(self):
        return self._protected

    @property
    def Access__private(self):
        return self._Access__private


give = Access()
print(give.public)
print(give.protected)
#  ERROR print(give.__private)
print(give.Access__private)
