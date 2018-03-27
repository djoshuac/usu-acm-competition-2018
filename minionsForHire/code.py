import re

n = int(input())

tag = r'<([/]{0,1}[ \w]+)>'
phone = r'<[ ]*phone[ ]*>[ ]*[0-9]{3}-[0-9]{3}-[0-9]{4}[ ]*</[ ]*phone[ ]*>'
email = r'<[ ]*email[ ]*>[ ]*[_A-Za-z0-9]+@[A-Za-z]+[.][A-Za-z]{2,3}[ ]*</[ ]*email[ ]*>'



stack = []
totalPhone = 0
totalEmail = 0
foundPhone = 0
foundEmail = 0
for _ in range(n):
    tmp = input()
    if re.search(tag, tmp):
        m = re.findall(tag, tmp)
        for t in m:
            if t[0] == '/':
                t = t[1:].strip()
                if len(stack) <= 0 or t != stack.pop():
                    print("False")
                    exit()

            else:
                if t.strip() == "phone":
                    totalPhone += 1
                elif t.strip() == "email":
                    totalEmail += 1
                stack.append(t.strip())
    if re.search(phone, tmp):
        foundPhone += len(re.findall(phone, tmp))
    if re.search(email, tmp):
        foundEmail += len(re.findall(email, tmp))
if foundPhone == totalPhone and foundEmail == totalEmail and len(stack) == 0:
    print("True")
else:
    print("False")