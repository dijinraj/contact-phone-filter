import vobject
f = open('original.vcf', 'rb') # all contacts exported from gmail or from other place
d = {}
cards = []
for c in vobject.readComponents(f):
    card = vobject.vCard()
    for x in c.getChildren():
    	# print x.prettyPrint();
        if not x.name[0] == 'X':
                card.add(x)
    cards.append(card)
    # break;

f.close()
f = open('onlyphone.vcf', 'wb')
for card in cards:
        if not d.has_key(str(card)):
                # print  dir(card)
                # print card.prettyPrint();
                # print card.getChildren();
                if card.getChildValue('tel'):
                    # print card.getChildValue('tel');
                    # print card.getChildValue('fn');
                    d[str(card)] = card
                    f.write(card.serialize())
f.close()