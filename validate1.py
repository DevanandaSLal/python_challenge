def validate_html(html_string):
    import re
    stack = []


    pattern = re.compile(r'<(/?)(\w+)>')


    for match in pattern.findall(html_string):
        slash, tag = match

        if not slash:
            stack.append(tag)
        else:
            if not stack or stack[-1] != tag:
                return False
            stack.pop()


    return len(stack) == 0


# Test cases
html_1 = "<p>Hello World!"
html_2 = "<p>Hello World!</p>"
html_3 = "<p>Hello <b>World</b>!</p>"
html_4 = "<p>Hello <b>World</p>!</b>"

print(validate_html(html_1))
print(validate_html(html_2))
print(validate_html(html_3))
print(validate_html(html_4))
