import re

def getcards(text):
    text = text.replace('\n', ' ').replace('\r', '')
    card = re.findall(r"[0-9]+", text)
    if not card or len(card) < 3:
        return
    cc, mes, ano, cvv = (card + [None] * 4)[:4]
    if len(card) == 3:
        if len(card[1]) == 3:
            mes, ano, cvv = card[2][:2], card[2][2:], card[1]
        else:
            mes, ano, cvv = card[1][:2], card[1][2:], card[2]
    else:
        if len(card[1]) == 3:
            mes, ano, cvv = card[2], card[3], card[1]
        else:
            mes, ano, cvv = card[1], card[2], card[3]
        if len(mes) == 2 and (mes > '12' or mes < '01'):
            mes, ano = ano, mes
    if (cc[0] == '3' and len(cc) != 15) or (len(cc) != 16) or (int(cc[0]) not in [3, 4, 5, 6]):
        return
    if len(mes) not in [2, 4] or (len(mes) == 2 and (mes > '12' or mes < '01')):
        return
    if len(ano) not in [2, 4] or (len(ano) == 2 and ano < '21') or (len(ano) == 4 and ano < '2021') or (len(ano) == 2 and ano > '29') or (len(ano) == 4 and ano > '2029'):
        return
    if (cc[0] == '3' and len(cvv) != 4) or (len(cvv) != 3):
        return
    return cc, mes, ano, cvv
