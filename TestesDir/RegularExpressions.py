import re


class RegularExpression:
    def __init__(self):
        pass

    @classmethod
    def is_email(cls, email: str) -> bool:
        pattern = ""
        # f"^(?(\")(\".+?(?<!\\)\"@)|(([0-9a-z]((\.(?!\.))|[-!#\$%&'\*\+/=\?\^`{}|~\w])*)(?<=[0-9a-z])@))(?([)([(\d{
        # 1,3}.){3}\d{1,3}])|(([0-9a-z][-0-9a-z]*[0-9a-z]*.)+[a-z0-9][-a-z0-9]{0,22}[a-z0-9]))$"
        try:
            email.split('@')
            return True
        except RegularExpression:
            return False
