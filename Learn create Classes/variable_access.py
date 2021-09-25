class Access:
    def __init__(self):
        self.public = 'public var'
        self._protected = 'protected var'

        self._access__private = None
        self.__private = 'private var'

give = Access()
print(give.public)
print(give._protected)
#  ERROR print(give.__private)
print(give._access__private)
