def on_palindroom(s):
    if len(s) <= 1:
        return True
    else:
        return s[0] == s[-1] and on_palindroom(s[1:-1])


s = 'kuulilennuteetunneliluuk'
if on_palindroom(s):
    print(s + ' on palindroom!')
else:
    print(s + ' ei ole palindroom!')