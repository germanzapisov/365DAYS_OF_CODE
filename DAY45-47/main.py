import re

class ReplaceText:
    def __init__(self, text, text_two):
        self.__text = text
        self.__text_two = text_two

    def replacer_email(self):
        pattern = r"[\w\.-]+@\w+\.\w{2,}"
        email = re.compile(pattern).findall(self.__text)
        return f"email: {email}"

    def replacer_password(self):
        pattern = r"[\w\-]{8,}"
        password = re.compile(pattern).findall(self.__text_two)
        return f"password: {password}"

text = "gera@gmail.com"
text_two = "Example-Password1311"
replace = ReplaceText(text, text_two)

print(replace.replacer_email())
print(replace.replacer_password())