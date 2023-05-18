





async def start_parsing(ball,direction,message):
    try:
        k = 0
        cookies = {
            'top100_id': 't1.-1.1257815121.1659005952933',
            '_ym_d': '1659005953',
            '_ym_uid': '1659005953948842883',
            'PHPSESSID': '56utcnrn697iuaulmjoppls601',
            '_ym_isad': '2',
            '_ym_visorc': 'w',
            'last_visit': '1661173520897%3A%3A1661184320897',
            't3_sid_-1': 's1.351532153.1661183531566.1661184320907.7.7.25.1',
        }

        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
            'Cache-Control': 'max-age=0',
            'Connection': 'keep-alive',
            # Requests sorts cookies= alphabetically
            # 'Cookie': 'top100_id=t1.-1.1257815121.1659005952933; _ym_d=1659005953; _ym_uid=1659005953948842883; PHPSESSID=56utcnrn697iuaulmjoppls601; _ym_isad=2; _ym_visorc=w; last_visit=1661173520897%3A%3A1661184320897; t3_sid_-1=s1.351532153.1661183531566.1661184320907.7.7.25.1',
            'Origin': 'http://priem.sut.ru',
            'Referer': 'http://priem.sut.ru/konkursnie-otbori',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
        }

        data = {
            'general': '101',
            'education_base_to': '3',
            'training_form': '4',
            'training_type': '4',
            '1cunv_groupab': str(direction),
            'action': 'get_result',
            'rekzach': '1',
        }

        response = requests.post('http://priem.sut.ru/konkursnie-otbori', cookies=cookies, headers=headers, data=data,
                                 verify=False)
        soup = BeautifulSoup(response.text, 'lxml')
        name_direction = soup.find('th', colspan="10").text
        prikaz_ = soup.find_all('th')
        prikaz = []
        for name in prikaz_:
            prikaz.append(name.text)
        prikaz = str(prikaz[-1])
        all_td = soup.find_all('td')
        tr_list = []
        for tr in all_td:
            tr_list.append(tr.text)
        count_finall_position = tr_list[3]
        if tr_list[0] == 'Общее количество мест для приема:':
            tr_list = tr_list[6:]
        else:
            tr_list = tr_list

        if prikaz == 'Приказ о зачислении':
            zip_tr_list = zip(*[iter(tr_list)] * 10)
            list_tr_list = list(zip_tr_list)
        else:
            zip_tr_list = zip(*[iter(tr_list)] * 9)
            list_tr_list = list(zip_tr_list)
            k += 1
        l = 0
        for x in range(int(count_finall_position)):
            ab = list_tr_list[x]
            if int(ab[2]) >= int(ball) and ab[6] == 'Да' and ab[7] == 'Да' and k == 1:
                l += 1
            elif int(ab[2]) >= int(ball) and ab[7] == 'Да' and ab[8] == 'Да' and k == 0:
                l += 1
        before = int(count_finall_position) - l
        if before < 0:
            before = 0
        else:
            before = before
        after = l + 1
        markup = InlineKeyboardMarkup(row_width=1)
        item1 = InlineKeyboardButton(text='Меню 📒',callback_data='premenu')
        markup.add(item1)
        if before > 0:
            await message.answer('☑️ | '+str(name_direction) + 'Ваш балл: ' + str(ball) + ', если вы подадите оригинал и согласие, то будете на '+str(after) + ' месте из '+ str(count_finall_position) + '. Запас в  ' + str(before- 1)+ ' свободных мест для вас, удачи !'+'\n P.S /// Данная программа считает худший исход',reply_markup=markup)
        else:
            await message.answer('К сожалению с вашим баллом ' + str(ball) + ' вы вне конкурса на бюджетные места ;(',reply_markup=markup)
    except:
        markup1= InlineKeyboardMarkup(row_width=2)
        item2 = InlineKeyboardButton(text='Заново 🔁',callback_data='start1')
        item3 = InlineKeyboardButton(text = 'Меню 📒', callback_data= 'premenu2')
        markup1.add(item2,item3)
        await message.answer('❌ | Данные введены не корректно, либо не работает сайт. Попробуйте ещё раз, либо возвращайтесь в меню:',reply_markup=markup1)