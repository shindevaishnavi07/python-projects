import pyshorteners

url = input('Enter the url:')


def shortenurl(url):
    s = pyshorteners.Shortener()
    print(s.tinyurl.short(url))

shortenurl(url)

# This are some  url  to copy in output for  page.
'''
https://maps.google.com/
https://youtube.com/
https://instagram.com/
https://chat.openai.com/
'''