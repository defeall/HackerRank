import re
def fun(s):
    if(bool(re.findall(r'[A-Za-z0-9-_]+[@]{1}[A-Za-z0-9]+[.][a-zA-Z]',s))==True):
        if(len(s[s.index('.')+1:])<4 and s.count('@')==1):
            return True
        else:
            return False
    else:
        return False

def filter_mail(emails):
    return list(filter(fun, emails))

if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)
