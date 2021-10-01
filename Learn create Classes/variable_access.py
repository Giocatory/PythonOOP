class Access:
    def __init__(self):
        self.public = 'public var'
        self._protected = 'protected var'

        self._access__private = None
        self.__private = 'private var'

    @property
    def protected(self):
        return self._protected

    @property
    def access__private(self):
        return self._access__private


give = Access()
print(give.public)
print(give.protected)
#  ERROR print(give.__private)
print(give.access__private)
