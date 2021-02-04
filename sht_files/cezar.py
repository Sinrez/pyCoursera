def code(text, key = 1):
    res = ''
    for c in text:
        res += text[(text.index(c) + key) % len(text)]
    return res



# text_007 = code("Агент 007, срочно выйдите на связь")
# print(text_007)