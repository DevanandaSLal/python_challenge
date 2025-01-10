def validate_html(html_string):
    l = []
    import re


    pattern = re.compile(r'<[^>]+>|[^<>]+')


    tags = ['<html>', '</html>', '<body>', '</body>', '<head>', '</head>',
              '<title>','</title>', '<h1>', '</h1>', '<p>', '</p>', '<b>',
            '</b>']


    for i in pattern.findall(html_string):
        if i.startswith('<') and i.endswith('>'):
            if i in tags:
                if i.startswith('</'):
                    if not l or l[-1] != i.replace('/', ''):
                        return False
                    l.pop()
                else:
                    l.append(i)



    return len(l) == 0



html_1 = "<p>Hello World!"
html_2 = "<p>Hello World!</p>"
html_3 = "<p>Hello <b>World</b>!</p>"
html_4 = "<p>Hello <b>World</p>!</b>"

print(validate_html(html_1))
print(validate_html(html_2))
print(validate_html(html_3))
print(validate_html(html_4))
