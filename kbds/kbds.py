from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                           InlineKeyboardMarkup, InlineKeyboardButton)
from aiogram.utils.keyboard import ReplyKeyboardBuilder

start_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Ру"),
            KeyboardButton(text="Eng"),
        ],
        {
            KeyboardButton(text="Кырг"),
            KeyboardButton(text="China"),
        }
    ],
    resize_keyboard=True,
)

to_main = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='На главную',
                                                                      callback_data='to_main')]])

info = InlineKeyboardMarkup(
    keyword=[
        [
            InlineKeyboardButton(text='Услуги'),
            InlineKeyboardButton(text='Каталог')
        ],

    ]
)
