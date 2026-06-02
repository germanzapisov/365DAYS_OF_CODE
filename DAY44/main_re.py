
import re

text = "zapisov@mail.com"

print(re.fullmatch(r'[\w\.-]+@\w+\.\w+', text))
print(re.search(r'\.\w+$', text))
print(re.search(r'^\w+', text))

print(re.sub('mail.com', 'gmail.com',text))

mail_pattern = re.compile(r"[\w+\.-]+@\w+\.\w+")
mail = re.split('@', text)
print(mail)


print(mail_pattern.fullmatch(text).group())

print(re.findall(r'\w+', text))

print(re.escape(text))

print(re.match('\w+',text).end())

group_text = 'hello im developer btw'

group_one = re.search(r"(\w+)", group_text)
print(group_one.groups())
