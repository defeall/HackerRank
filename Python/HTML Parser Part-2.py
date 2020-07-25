from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_comment(self, data):
        if('<!--' in data and '-->' in html):
            print("Single-line Comment  :", data)
        else:
            print("Multi-line Comment  :", data)
    def handle_data(self, data):
        print("Data     :", data)
html = ""       
for i in range(int(input())):
    html += input().rstrip()
    html += '\n'
    
parser = MyHTMLParser()
parser.feed(html)
parser.close()
