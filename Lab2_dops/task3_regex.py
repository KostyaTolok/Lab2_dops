import re


def main():
    mail = input("Email: ")

    if re.fullmatch(r'^[\w\\.-]+@[\w\\.-]+(\.[\w]+)+$', mail):
        print("Email is valid")
    else:
        print("Email isn't valid")

    num = input("Число: ")
    if re.fullmatch(r'^[0-9]*[.,]?[0-9]+$', num):
        print("Number is valid")
    else:
        print("Number isn't valid")

    pattern = (r'^'
               r'((?P<scheme>.+?)://)?'
               r'((?P<user>.+?)(:(?P<password>.*?))?@)?'
               r'(?P<host>.*?)'
               r'(:(?P<port>\d+?))?'
               r'(?P<path>/.*?)?'
               r'(?P<query>[?].*?)?'
               r'$'
               )

    url = input("Введите url: ")

    regex = re.compile(pattern)
    m = regex.match(url)
    match = m.groupdict() if m is not None else None
    print(match)

    html_tag = input("Html tag:")
    html_match = re.search(r'^<(?P<first_name>[\w]+)(\s[\w]+=.+)*>(?P<data>[\w]+)</(?P<second_name>[\w]+)>$', html_tag)
    if html_match is not None and html_match.group("first_name") == html_match.group("second_name"):
        print(html_match.group("data"))
    else:
        print("Html isn't valid")



main()
