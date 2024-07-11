from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def make_row_keybord(buttons: list[str]) -> ReplyKeyboardMarkup:
    row = [KeyboardButton(text=button) for button in buttons]
    return ReplyKeyboardMarkup(keyboard=[row], resize_keyboard=True)

    #return ReplyKeyboardMarkup(keyboard=[row], resize_keyboard=True)
    #return ReplyKeyboardMarkup(keyboard=[buttons], resize_keyboard=True)
