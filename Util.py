class Util:
    @classmethod
    def equals(cls, obj: str, objt: str) -> bool:
        if obj.upper() == objt.upper():
            return True
        else:
            return False

    @classmethod
    def equals(cls, obj: object, objt: object) -> bool:
        if obj.__eq__(objt):
            return True
        else:
            return False
