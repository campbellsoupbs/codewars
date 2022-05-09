import re

def domain_name(url):
    pass

    x = re.findall(r'\.(.*)\.|//(.*)\.', url)
    return x

#Not finished