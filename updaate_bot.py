
import time
from aiogram import  Bot, Dispatcher, types, executor
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.callback_data import CallbackData
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import requests
from bs4 import BeautifulSoup
import lxml

napr_callback = CallbackData('napr','pars')

bot = Bot(token='5577587269:AAEDbk_fSaro5v0wf8-4H6keer0xhIXRJWI')
dp = Dispatcher(bot,storage=MemoryStorage())



class Orderparser(StatesGroup):
    waiting_diraction = State()
    waiting_ball = State()

class SNYLSpars(StatesGroup):
    waiting_snils_dir = State()
    waiting_snils_num = State()

@dp.message_handler(commands='start')
async def start(message: types.Message):
    markup = InlineKeyboardMarkup(row_width=1)
    item1 = InlineKeyboardButton(text='Начать',callback_data='premenu2')
    markup.add(item1)
    await bot.send_message(message.from_user.id,'☀️\n Привет, я бот СПБГУТ для абитуриентов, настроен для программ обучения "Бакалавриат" и "Специалитет", которые поступают на бюджетной основе.\n \n Я помогу определить: \n     1) Cколько перед вами человек с оригиналом аттестата и согласием, у которых больше баллов, чем у вас \n     2) Найти себя в списке по СНИЛС \n \n Для повторного вызова этого сообщения, воспользуйтесь командой /start .Её вы можете найти, нажав по кнопке MENU',reply_markup=markup)

@dp.callback_query_handler(text='premenu', state='*')
async def start_menu(callback: types.CallbackQuery):
    markup = InlineKeyboardMarkup(row_width=2)
    item1 = InlineKeyboardButton(text='Поиск по СНИЛС 🔎',callback_data='SNYLS')
    item2 = InlineKeyboardButton(text='Подсчет мест 📋', callback_data='start1')
    markup.add(item1,item2)
    await bot.send_message(callback.message.chat.id, '📒 Меню | Выберете функцию:',reply_markup=markup)

@dp.callback_query_handler(text='premenu2', state='*')
async def start_menu(callback: types.CallbackQuery):
    markup = InlineKeyboardMarkup(row_width=2)
    item1 = InlineKeyboardButton(text='Поиск по СНИЛС 🔎',callback_data='SNYLS')
    item2 = InlineKeyboardButton(text='Подсчет мест 📋', callback_data='start1')
    markup.add(item1,item2)
    await bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.message_id, text = '📒 Меню | Выберете функцию:' ,reply_markup=markup)

#------------------------

@dp.callback_query_handler(text='SNYLS', state='*')
async def snyls(callback: types.CallbackQuery, state: FSMContext):
    await state.finish()
    markup = InlineKeyboardMarkup(row_width=1)
    item1 = InlineKeyboardButton(text='РТС  🟥 ', callback_data='snaprРТС')
    item2 = InlineKeyboardButton(text='ИСиТ 🟪', callback_data='snaprИСиТ')
    item3 = InlineKeyboardButton(text='ИКСС 🟧', callback_data='snaprИКСС')
    item4 = InlineKeyboardButton(text='ФПП 🟫', callback_data='snaprФПП')
    item5 = InlineKeyboardButton(text='⬅ Назад', callback_data='premenu2')
    markup.add(item1, item2, item3, item4,item5)
    await bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.message_id,text='Выбери факультет из предложенного списка:', reply_markup=markup)


@dp.callback_query_handler(Text(startswith='snapr'),state='*')
async def check_napr_snyls(callback: types.CallbackQuery):
    if callback.data == 'snaprРТС':
        markup2 = InlineKeyboardMarkup(row_width=1)
        item1 = InlineKeyboardButton(text='05.03.06', callback_data='000000194')
        item2 = InlineKeyboardButton(text='11.03.01', callback_data='000000198')
        item3 = InlineKeyboardButton(text='11.03.02', callback_data='000000202')
        item4 = InlineKeyboardButton(text='11.03.03', callback_data='000000206')
        item5 = InlineKeyboardButton(text='12.03.04', callback_data='000000210')
        item6 = InlineKeyboardButton(text='11.05.04', callback_data='000000214')
        item7 = InlineKeyboardButton(text='⬅ Назад', callback_data='SNYLS')

        markup2.add(item1,item2,item3,item4,item5,item6,item7)
        await bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.message_id,text='Выберите направление:',reply_markup=markup2)
        await SNYLSpars.waiting_snils_dir.set()
    elif callback.data == 'snaprИКСС':
        markup2 = InlineKeyboardMarkup(row_width=1)
        item1 = InlineKeyboardButton(text='09.03.01', callback_data='000000218')
        item2 = InlineKeyboardButton(text='09.03.04', callback_data='000000222')
        item3 = InlineKeyboardButton(text='10.03.01', callback_data='000000226')
        item4 = InlineKeyboardButton(text='11.03.02', callback_data='000000230')
        item5 = InlineKeyboardButton(text='12.03.03', callback_data='000000234')
        item6 = InlineKeyboardButton(text='10.05.02', callback_data='000000238')
        item7 = InlineKeyboardButton(text='11.05.04', callback_data='000000242')
        item8 = InlineKeyboardButton(text='⬅ Назад', callback_data='SNYLS')
        markup2.add(item1,item2,item3,item4,item5,item6,item7,item8)
        await bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.message_id,text='Выберите направление:',reply_markup=markup2)
        await SNYLSpars.waiting_snils_dir.set()
    elif callback.data == 'snaprИСиТ':
        markup2 = InlineKeyboardMarkup(row_width=1)
        item1 = InlineKeyboardButton(text='09.03.02 Интеллектуальные информационные системы и технологии', callback_data='000000246')
        item2 = InlineKeyboardButton(text='09.03.02 Прикладные информационные системы и технологии', callback_data='000000250')
        item3 = InlineKeyboardButton(text='09.03.02 Дизайн графических и пользовательских интерфейсов информационных систем', callback_data='000000254')
        item4 = InlineKeyboardButton(text='09.03.02 Системное и прикладное программирование информационных систем', callback_data='000000394')
        item5 = InlineKeyboardButton(text='27.03.04', callback_data='000000259')
        item6 = InlineKeyboardButton(text='⬅ Назад', callback_data='SNYLS')
        markup2.add(item1,item2,item3,item4,item5,item6)
        await bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.message_id,text='Выберите направление:',reply_markup=markup2)
        await SNYLSpars.waiting_snils_dir.set()
    elif callback.data == 'snaprФПП':
        markup2 = InlineKeyboardMarkup(row_width=1)
        item1 = InlineKeyboardButton(text='11.03.04', callback_data='000000263')
        item2 = InlineKeyboardButton(text='⬅ Назад', callback_data='SNYLS')
        markup2.add(item1,item2)
        await bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.message_id,text='Выберите направление:',reply_markup=markup2)
        await SNYLSpars.waiting_snils_dir.set()

@dp.callback_query_handler(Text(startswith='00000'),state= SNYLSpars.waiting_snils_dir)
async def choose_napr_snyls(callback: types.CallbackQuery, state: FSMContext):
    await state.update_data(choose_direction_snyls = callback.data)
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    await bot.edit_message_text(chat_id=callback.message.chat.id,message_id=callback.message.message_id,text='Теперь введите свой снилс, по форме 123-321-123 12')
    await SNYLSpars.waiting_snils_num.set()

@dp.message_handler(state=SNYLSpars.waiting_snils_num)
async def choose_nums(message: types.Message, state: FSMContext):
    await state.update_data(choose_num=message.text.lower())
    await message.answer('Ведется обработка данных 💬')
    user_data = await state.get_data()
    direction_snyls = user_data['choose_direction_snyls']
    snyls_num = user_data['choose_num']
    await start_parsing_snyls(snyls_num, direction_snyls, message)
    await state.finish()

#------------------------------------Подсчет мест

@dp.callback_query_handler(text='start1', state='*')
async def start_nachalo(callback: types.CallbackQuery, state: FSMContext):
    await state.finish()
    markup = InlineKeyboardMarkup(row_width=1)
    item1 = InlineKeyboardButton(text='РТС 🟥', callback_data='naprРТС')
    item2 = InlineKeyboardButton(text='ИСиТ 🟪', callback_data='naprИСиТ')
    item3 = InlineKeyboardButton(text='ИКСС 🟧', callback_data='naprИКСС')
    item4 = InlineKeyboardButton(text='ФПП 🟫', callback_data='naprФПП')
    item5 = InlineKeyboardButton(text='⬅ Назад', callback_data='premenu2')
    markup.add(item1, item2, item3, item4,item5)
    await bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.message_id,text='Выбери факультет из предложенного списка:', reply_markup=markup)

@dp.callback_query_handler(Text(startswith='napr'),state='*')
async def check_napr(callback: types.CallbackQuery):
    if callback.data == 'naprРТС':
        markup2 = InlineKeyboardMarkup(row_width=1)
        item1 = InlineKeyboardButton(text='05.03.06', callback_data='000000194')
        item2 = InlineKeyboardButton(text='11.03.01', callback_data='000000198')
        item3 = InlineKeyboardButton(text='11.03.02', callback_data='000000202')
        item4 = InlineKeyboardButton(text='11.03.03', callback_data='000000206')
        item5 = InlineKeyboardButton(text='12.03.04', callback_data='000000210')
        item6 = InlineKeyboardButton(text='11.05.04', callback_data='000000214')
        item7 = InlineKeyboardButton(text='⬅ Назад', callback_data='start1')
        markup2.add(item1,item2,item3,item4,item5,item6,item7)
        await bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.message_id,text='Выберите направление:',reply_markup=markup2)
        await Orderparser.waiting_diraction.set()
    elif callback.data == 'naprИКСС':
        markup2 = InlineKeyboardMarkup(row_width=1)
        item1 = InlineKeyboardButton(text='09.03.01', callback_data='000000218')
        item2 = InlineKeyboardButton(text='09.03.04', callback_data='000000222')
        item3 = InlineKeyboardButton(text='10.03.01', callback_data='000000226')
        item4 = InlineKeyboardButton(text='11.03.02', callback_data='000000230')
        item5 = InlineKeyboardButton(text='12.03.03', callback_data='000000234')
        item6 = InlineKeyboardButton(text='10.05.02', callback_data='000000238')
        item7 = InlineKeyboardButton(text='11.05.04', callback_data='000000242')
        item8 = InlineKeyboardButton(text='⬅ Назад', callback_data='start1')
        markup2.add(item1,item2,item3,item4,item5,item6,item7,item8)
        await bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.message_id,text='Выберите направление:',reply_markup=markup2)
        await Orderparser.waiting_diraction.set()
    elif callback.data == 'naprИСиТ':
        markup2 = InlineKeyboardMarkup(row_width=1)
        item1 = InlineKeyboardButton(text='09.03.02 Интеллектуальные информационные системы и технологии', callback_data='000000246')
        item2 = InlineKeyboardButton(text='09.03.02 Прикладные информационные системы и технологии', callback_data='000000250')
        item3 = InlineKeyboardButton(text='09.03.02 Дизайн графических и пользовательских интерфейсов информационных систем', callback_data='000000254')
        item4 = InlineKeyboardButton(text='09.03.02 Системное и прикладное программирование информационных систем', callback_data='000000394')
        item5 = InlineKeyboardButton(text='27.03.04', callback_data='000000259')
        item6 = InlineKeyboardButton(text='⬅ Назад', callback_data='start1')

        markup2.add(item1,item2,item3,item4,item5,item6)
        await bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.message_id,text='Выберите направление:',reply_markup=markup2)
        await Orderparser.waiting_diraction.set()
    elif callback.data == 'naprФПП':
        markup2 = InlineKeyboardMarkup(row_width=1)
        item1 = InlineKeyboardButton(text='11.03.04', callback_data='000000263')
        item2 = InlineKeyboardButton(text='⬅ Назад', callback_data='start1')
        markup2.add(item1,item2)
        await bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.message_id,text='Выберите направление:',reply_markup=markup2)
        await Orderparser.waiting_diraction.set()


@dp.callback_query_handler(Text(startswith='00000'),state= Orderparser.waiting_diraction)
async def choose_napr(callback: types.CallbackQuery, state: FSMContext):
    await state.update_data(choose_direction = callback.data)
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    msg = await bot.edit_message_text(chat_id=callback.message.chat.id,message_id=callback.message.message_id,text='Теперь введите сумму баллов, с учетом индивидуальных достижений')
    await Orderparser.waiting_ball.set()

@dp.message_handler(state=Orderparser.waiting_ball)
async def choose_ball(message: types.Message, state: FSMContext):
    await state.update_data(choose_ball=message.text.lower())
    await message.answer('Ведется обработка данных 💬')
    user_data = await state.get_data()
    direction = user_data['choose_direction']
    ball = user_data['choose_ball']
    await start_parsing(ball, direction, message)
    await state.finish()

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


async def start_parsing_snyls(snyls_num,direction_snyls,message):
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
            '1cunv_groupab': str(direction_snyls),
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
            pos = 0
            ab = list_tr_list[x]
            pos = ab[0]
            if ab[1] == str(snyls_num) and int(pos) <= int(count_finall_position):
                position = pos
                break
        markup = InlineKeyboardMarkup(row_width=1)
        item1 = InlineKeyboardButton(text='Меню 📒 ', callback_data='premenu')
        markup.add(item1)
        await message.answer('☑️ | Ваш СНИЛС: ' + str(snyls_num) + '\n Ваша позиция: ' + str(position) + '/' + str(count_finall_position),reply_markup=markup)

    except:
        markup1 = InlineKeyboardMarkup(row_width=2)
        item2 = InlineKeyboardButton(text='Заново 🔁', callback_data='SNYLS')
        item3 = InlineKeyboardButton(text='Меню 📒', callback_data='premenu2')
        markup1.add(item2,item3)
        await message.answer('❌ | Упс... Что-то пошло не так, попробуйте ещё раз, либо возвращайтесь в меню',reply_markup=markup1)


executor.start_polling(dp, skip_updates=True)