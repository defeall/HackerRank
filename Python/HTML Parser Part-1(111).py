from html.parser import HTMLParser

n = int(input())

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Start :",tag)
        for element in attrs:
            print('->',element[0],'>',element[1])
    def handle_endtag(self,tag):
        print ("End   :",tag)
    def handle_startendtag(self, tag, attrs):
        print("Empty :",tag)
        for element in attrs:
            print('->',element[0],'>',element[1])
parser = MyHTMLParser()            
for i in range(n):
    parser.feed(input())
