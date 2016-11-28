import urllib

def output_boosters(file_name, boosters):
    body = _generate_body(boosters)
    with file(file_name, 'w') as f:
        f.write('<html><body>%s</body>' % body)

def _generate_body(boosters):
    body = ''
    for i, b in enumerate(boosters):
        body += _generate_booster_body(i + 1, b)
    return body

def _generate_booster_body(i, booster):
    res = ''
    res += '<h2>Booster %d</h2>' % i
    for card in booster.cards():
        res += '%s' % _generate_card_repr(card)
    res += '<br>'
    return res

def _generate_card_repr(card):
    image_url = 'http://gatherer.wizards.com/Handlers/Image.ashx?name=%s&type=card'\
                % urllib.quote(card.name())
    return '<img src=%s>' % image_url
