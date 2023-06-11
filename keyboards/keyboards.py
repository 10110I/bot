from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup

from lexicon.lexicon_ru import LEXICON_RU
from lexicon.callback_data import callback_data


#button_1: KeyboardButton = KeyboardButton(text=LEXICON_RU['rock'])
#button_2: KeyboardButton = KeyboardButton(text=LEXICON_RU['scissors'])
#button_3: KeyboardButton = KeyboardButton(text=LEXICON_RU['paper'])

# Создаем игровую клавиатуру с кнопками "Камень 🗿",
# "Ножницы ✂" и "Бумага 📜" как список списков
#game_kb: ReplyKeyboardMarkup = ReplyKeyboardMarkup(
                                    #keyboard=[[button_1],
                                             # [button_2],
                                          #    [button_3]],
                                   # resize_keyboard=True)



btn_1_1: InlineKeyboardButton = InlineKeyboardButton(text=LEXICON_RU['/start'], callback_data=callback_data['menu'])

start_kb: InlineKeyboardMarkup = InlineKeyboardMarkup(keyboard= [[btn_1_1]], row_width=1)



# ртс
btn2_1 = InlineKeyboardButton(text='05.03.06', callback_data=callback_data['05.03.06'])
btn2_2 = InlineKeyboardButton(text='11.03.01', callback_data=callback_data['11.03.01'])
btn2_3 = InlineKeyboardButton(text='11.03.02_rtc', callback_data=callback_data['11.03.02_rtc'])
btn2_4 = InlineKeyboardButton(text='11.03.03', callback_data=callback_data['11.03.03'])
btn2_5 = InlineKeyboardButton(text='12.03.04', callback_data=callback_data['12.03.04'])
btn2_6 = InlineKeyboardButton(text='11.05.04', callback_data=callback_data['11.05.04_rtc'])
btn2_7 = InlineKeyboardButton(text=LEXICON_RU['back'], callback_data=callback_data['napr'])
rtc_kb: InlineKeyboardMarkup = InlineKeyboardMarkup(keyboard = [[btn2_1],[btn2_2],[btn2_3],[btn2_4],[btn2_5],[btn2_6],[btn2_7]], row_width=1)


btn3_1 = InlineKeyboardButton(text=LEXICON_RU["RTC"], callback_data='---')
btn3_2 = InlineKeyboardButton(text=LEXICON_RU["ISIT"], callback_data='---')
btn3_3 = InlineKeyboardButton(text=LEXICON_RU["IKSS"], callback_data='---')
btn3_4 = InlineKeyboardButton(text=LEXICON_RU["FPP"], callback_data='---')
btn3_5 = InlineKeyboardButton(text=LEXICON_RU["back"], callback_data=callback_data['---'])

choise_napr: InlineKeyboardMarkup = InlineKeyboardMarkup(keyboard = [[btn3_1],[btn3_2],[btn3_3],[btn3_4],[btn3_5]], row_width=1)

#ikss

btn4_1 = InlineKeyboardButton(text='09.03.01', callback_data=callback_data['09.03.01'])
btn4_2 = InlineKeyboardButton(text='09.03.04', callback_data=callback_data['09.03.04'])
btn4_3 = InlineKeyboardButton(text='10.03.01', callback_data=callback_data['10.03.01'])
btn4_4 = InlineKeyboardButton(text='11.03.02_ikss', callback_data=callback_data['11.03.02_ikss'])
btn4_5 = InlineKeyboardButton(text='12.03.03', callback_data=callback_data['12.03.03'])
btn4_6 = InlineKeyboardButton(text='10.05.02', callback_data=callback_data['10.05.02'])
btn4_7 = InlineKeyboardButton(text='11.05.04_ikss', callback_data=callback_data['11.05.04_ikss'])
btn4_8 = InlineKeyboardButton(text=LEXICON_RU["back"], callback_data='napr')

ikss_kb: InlineKeyboardMarkup= InlineKeyboardMarkup(keyboard = [[btn4_1],[btn4_2],[btn4_3],[btn4_4],[btn4_5],[btn4_6],[btn4_7],[btn4_8]],row_width=1)