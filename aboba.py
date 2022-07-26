import re
import datetime
import time

s = input('Input: ')
s = s.lower()
months = ['январ', 'феврал', 'март', 'апрел', 'мая', 'июн', 'июл', 'август', 'сентябр', 'октябр', 'ноябр', 'декабр']
days = ['понедельник', 'вторник', 'сред', 'четверг', 'пятниц', 'суббот', 'воскресень','будня', 'выходны']
dayp = ['понедельник', 'вторник', 'среда', 'четверг', 'пятница', 'суббота', 'воскресенье', 'по будням', 'по выходным']
wrsut = ['утром', 'днем', 'вечером', 'ночью']
year = 'года'
W1 = 'в '
repeat = ['каждый', 'каждую', 'по']
repeat1 = ['ежедневно', 'еженедельно', 'ежемесячно', 'ежегодно']
stepm = 'через'
step = ['минут', 'час', 'дн', 'недель', 'месяц', 'год', 'лет']
nxt = ['завтра', 'послезавтра', 'на следующей неделе', 'в следующем месяце', 'в следующем году']

nxts = 0
i = 0
l = 0
povt = 0
sts = 0
delta = 0
dwo = 0
t = 0
pog = 0
nxtm = 0
rept = 0
errors = 0
x = 0
z = 0
ds = 0
ms = 0
time = datetime.datetime.now()
k1 = len(months)
k2 = len(days)
k3 = len(repeat)
k4 = len(repeat1)
k5 = len(step)
k6 = len(nxt)
k7 = len(wrsut)

mp = 0
hp = 0
dp = 0
wdp = 0
mop = 0
yp = 0

fff1 = False
fff2 = False
fff3 = False
fff4 = False

while i <= k1:
    if i != k1:
        if months[i] in s:
            mon = re.findall(r'(?<=\s)\d{1,2}\s' + months[i] + '.{0,2}', s)
            mon1 = " ".join(mon)
            d1 = re.findall(r'\d{1,2}', mon1)
            dp = " ".join(d1)
            mop = i
            s = s.replace(mon1, '')
            errors = errors + 1
            ms = ms + 1
            break
        else:
            i = i + 1
    else:
        break

i = 0

while i < k2:
    if days[i] in s:
        if W1 in s:
            dw = re.findall(r'.\s' + days[i] + '.{0,1}', s)
            dw1 = " ".join(dw)
            if W1 in dw1:
                dwo = i
                dw2 = re.findall(days[i], dw1)
                dwp = " ".join(dw2)
                s = s.replace(dw1, '')
                ds = ds + 1
                errors += 1
                break
            else:
                while l < k3:
                    if repeat[l] in s:
                        rep = re.findall(repeat[l] + '\s' + days[i]+ '.{0,2}', s)
                        rep1 = " ".join(rep)
                        if repeat[l] in rep1:
                            dwo = i
                            povt = 1
                            repp = repeat[l] + ' ' + days[i]
                            s = s.replace(rep1, '')
                            ds = ds + 1
                            errors = ds + 1
                            z = z + 1
                            break
                    else:
                        l = l + 1
                break
        else:
            while l < k3:
                if repeat[l] in s:
                    rep = re.findall(repeat[l] + '\s' + days[i]+ '.{0,2}', s)
                    rep1 = " ".join(rep)
                    if repeat[l] in rep1:
                        dwo = i
                        povt = 1
                        repp = repeat[l] + ' ' + days[i]
                        s = s.replace(rep1, '')
                        ds = ds + 1
                        errors = ds + 1
                        z = z + 1
                        break
                    break
                else:
                    l = l + 1
            break
    else:
        i = i + 1

i = 0

while i < k4:
    if repeat1[i] in s:
        povt = i
        s = s.replace(repeat1[i], '')
        z = z + 1
        break
    else:
        i = i + 1

i = 0

if stepm in s:
    while i < k5:
        st = re.findall(stepm + r'\s{0,1}\d{0,2}\s' + step[i] + '.{0,2}', s)
        st1 = " ".join(st)
        if step[i] in st1:
            if re.search(r'\s\d{1,2}\s', st1):
                st2 = re.findall(r'\s\d{1,2}\s', st1)
                delta = " ".join(st2)
                sts = sts + 1
                t = i
                s = s.replace(st1, '')
                break
            else:
                delta = 1
                sts = sts + 1
                t = i
                s = s.replace(st1, '')
                break
        else:
            i = i + 1

i = 0

while i < k6:
    if ' ' + nxt[i] in s:
        nxtm = i
        nxts = nxts + 1
        s = s.replace(nxt[i], '')
    else:
        i = i + 1

i = 0

while i < k7:
    if wrsut[i] in s:
        s = s.replace(wrsut[i], '')
        if i == 0:
            fff1 = True
        elif i == 1:
            fff2 = True
        elif i == 2:
            fff3 = True
        else:
            fff4 = True
    i += 1

i = 0
 

if year in s:
    y1 = re.findall(r'(?<=\s)\d{2,4}\s' + year, s)
    y2 = " ".join(y1)
    yx = re.findall(r'\d{2,4}', y2)
    yp = " ".join(yx)
    s = s.replace(" ".join(y1), '')

if ':' in s:
    if W1 in s:
        tw = re.findall(r'.\s' + '\d{2}.\d{2}', s)
        tw1 = " ".join(tw)
        if W1 in tw1:
            time = re.findall(r'\d{2}.\d{2}', s)
            tt = " ".join(time)
            hour = re.findall(r'\d{2}.', tt)
            hour1 = " ".join(hour)
            hx = re.findall(r'\d{2}', hour1)
            hp = " ".join(hx)
            minute = re.findall(r'.\d{2}', tt)
            minute1 = " ".join(minute)
            mx = re.findall(r'\d{2}', minute1)
            mp = " ".join(mx)
            s = s.replace(W1 + tt, '')
            x = x + 1
            errors += 1
        else:
            time = re.findall(r'\d{2}.\d{2}', s)
            tt = " ".join(time)
            hour = re.findall(r'\d{2}.', tt)
            hour1 = " ".join(hour)
            hx = re.findall(r'\d{2}', hour1)
            hp = " ".join(hx)
            minute = re.findall(r'.\d{2}', tt)
            minute1 = " ".join(minute)
            mx = re.findall(r'\d{2}', minute1)
            mp = " ".join(mx)
            s = s.replace(tt, '')
            x = x + 1
    else:
        time = re.findall(r'\d{2}.\d{2}', s)
        tt = " ".join(time)
        hour = re.findall(r'\d{2}.', tt)
        hour1 = " ".join(hour)
        hx = re.findall(r'\d{2}', hour1)
        hp = " ".join(hx)
        minute = re.findall(r'.\d{2}', tt)
        minute1 = " ".join(minute)
        mx = re.findall(r'\d{2}', minute1)
        mp = " ".join(mx)
        s = s.replace(tt, '')
        x = x + 1

delta = int(delta)

if dwo < 14 and dwo > 8:
    dwo = dwo % 7
elif dwo == 14 or dwo == 16:
    dwo = 7
elif dwo == 15 or dwo == 17:
    dwo = 8

if ms == 1:
    mop = mop + 1

if sts > 0:
    if t == 0:
        if time.minute + delta > 60:
            mp = (time.minute + delta % 60) % 60
            hp = time.hour + (time.minute + delta) // 60
            x = x + 6
        else:
            mp = (time.minute + (delta % 60)) % 60
            x = x + 4
    elif t == 1:
        x = x + 5
        if time.hour + delta > 24:
            dp = (time.day + 1) % 31
            hp = (time.hour + delta) % 24
        else:
            hp = (time.hour + delta) % 24
    elif t == 2:
        if (time.month % 2 == 1 and time.month <= 7) or (time.month % 2 == 0 and time.month > 7):
            if time.day + delta > 31:
                dp = (time.day + delta) % 31
                pog = (time.day + delta) // 31
            else:
                dp = time.day + delta
        elif time.month == 2:
            if time.day + delta > 28:
                dp = (time.day + delta) % 28
                pog = (time.day + delta) // 28
            else:
                dp = time.day + delta
        else:
            if time.day + delta > 30:
                dp = (time.day + delta) % 30
                pog = (time.day + delta) // 30
            else:
                dp = time.day + delta
        wdp = time.isoweekday() + delta % 7
    elif t == 3:
        if time.month % 2 == 1:
            dp = (time.day + 7) % 31
        elif time.month == 12:
            dp = ((time.day + 7) % 31)
        elif time.month == 2:
            dp = (time.day + 7) % 28
        else:
            dp = (time.day + 7) % 30
    elif t == 4:
        mop = (time.month + delta) % 12
    elif t == 5:
        kkk = datetime.datetime.today()
        kkk = str(kkk)
        yp = int(kkk[0:4])
        yp = yp + delta
    elif t == 6:
        yp = time.year + delta

if nxts != 0:
    if nxtm == 0:
        dp = time.day + 1
        wdp = (time.isoweekday() + 1) % 7
    elif nxtm == 1:
        dp = time.day + 2
        wdp = (time.isoweekday() + 2) % 7
    elif nxtm == 3:
        mop = (time.month + 1) % 12
    elif nxtm == 4:
        yp = time.year + 1

if x == 0:
    hp = time.hour
    mp = time.minute
    if fff1 == True:
        hp = '06'
    elif fff2 == True:
        hp = '12'
    elif fff3 == True:
        hp = '18'
    elif fff4 == True:
        hp = '00'
elif x == 4:
    hp = time.hour
elif x == 6:
    x = 0
elif x == 1:
    x = 0
else:
    mp = time.minute

if nxts == 1 and nxtm > 1:
    dwo = time.isoweekday()

if ds == 0 and z != 0:
    dwo = time.isoweekday()
if dp == 0:
    kkk = datetime.datetime.today()
    kkk = str(kkk)
    dp = int(kkk[8:10])
if mop == 0:
    kkk = datetime.datetime.today()
    kkk = str(kkk)
    mop = int(kkk[5:7])
if yp == 0:
    kkk = datetime.datetime.today()
    kkk = str(kkk)
    yp = int(kkk[0:4])

if sts != 0:
    print(f'STATUS:SUCCESS, TEXT: {s}, TIME: hour: {hp}, minute: {mp}, '
          f'DATE: day: {dp}, month: {(mop+pog) % 12}, year: {yp} ', 1)
elif z != 0:
    if povt == 0:
        print(
            f'STATUS:SUCCESS, TEXT: {s}, PARAMS: Repetition rate: {repeat1[povt]}, TIME: hour: {hp}, minute: {mp}', 2)
    elif povt == 1 and dwo < 7:
        print(
            f'STATUS:SUCCESS, TEXT: {s}, PARAMS: Repetition rate: {repeat1[povt]}, Day of the week: {dayp[dwo]}, TIME: '
            f'hour: {hp}, minute: {mp}', 3)
    elif povt == 1 and dwo >= 7:
        print(
            f'STATUS:SUCCESS, TEXT: {s}, PARAMS: Repetition rate: {repeat1[povt]}, {dayp[dwo]}, TIME: '
            f'hour: {hp}, minute: {mp}', 4)
    elif povt == 2:
        print(
            f'STATUS:SUCCESS, TEXT: {s}, PARAMS: Repetition rate: {repeat1[povt]}, Day of the week: {dayp[dwo]}, TIME: '
            f'hour: {hp}, minute: {mp}, DATE: day: {dp}', 5)
    elif povt == 3:
        print(
            f'STATUS:SUCCESS, TEXT: {s}, PARAMS: Repetition rate: {repeat1[povt]}, Day of the week: {dayp[dwo]}, TIME: '
            f'hour: {hp}, minute: {mp}, DATE: day: {dp}, month: {mop}', 6)
elif nxts != 0:
    print(f'STATUS:SUCCESS, TEXT: {s}, TIME: hour: {hp}, minute: {mp} '
          f'DATE: day: {dp}, month: {mop}, year: {yp}', 7)
elif errors >= 1 and ds == 1:
    print(f'STATUS:SUCCESS, TEXT: {s}, PARAMS: Day of the week: {dayp[dwo]}, TIME: hour: {hp}, minute: {mp}', 8)
elif errors >= 1:
    print(f'STATUS:SUCCESS, TEXT: {s}, TIME: hour: {hp}, minute: {mp}, '
          f'DATE: day: {dp}, month: {mop}, year: {yp}', 9)
else:
    print('STATUS:ERROR')
