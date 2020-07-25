from html.parser import HTMLParser
class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Start :", tag)
        if(attrs!=[]):
            for i in range(len(attrs)):
                print('->',attrs[i][0],'>',attrs[i][1])
    
    def handle_endtag(self, tag):
        print("End   :", tag)
    def handle_startendtag(self, tag, attrs):
        print( "Empty :", tag)
        if(attrs!=[]):
            for i in range(len(attrs)):
                print('->',attrs[i][0],'>',attrs[i][1])
b=0
n=int(input())
for i in range(n):
    a=input()
    if('<!--' in a):
        b=b+1
    if '-->' in a:
        b=b-1
    if(b>0):
        continue
    parser = MyHTMLParser()
    parser.feed(a)
