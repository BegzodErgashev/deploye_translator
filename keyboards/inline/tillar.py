from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
btn = InlineKeyboardMarkup(
    inline_keyboard=[
       [
           InlineKeyboardButton(text="๐บ๐ฟ O'zbek tili", callback_data="๐uz"),
           InlineKeyboardButton(text="๐ฌ๐ง Ingliz tili", callback_data="๐en"),
       ],
        [
            InlineKeyboardButton(text="๐ช๐ญ Arab tili", callback_data="๐ar"),
            InlineKeyboardButton(text="๐ฏ๐ต Yapon tili", callback_data="๐ja"),
        ],
        [
            InlineKeyboardButton(text="๐ฐ๐ท Koreys tili", callback_data="๐ko"),
            InlineKeyboardButton(text="๐จ๐ณ Xitoy tili", callback_data="๐zh"),
        ],
        [
            InlineKeyboardButton(text="๐ท๐บ Rus tili", callback_data="๐ru"),
            InlineKeyboardButton(text="๐ฎ๐น Fransuz tili", callback_data="๐fr"),
        ]
    ]
)
btn_two = InlineKeyboardMarkup(
    inline_keyboard=[
       [
           InlineKeyboardButton(text="๐บ๐ฟ O'zbek tili", callback_data="๐uz"),
           InlineKeyboardButton(text="๐ฌ๐ง Ingliz tili", callback_data="๐en"),
       ],
        [
            InlineKeyboardButton(text="๐ช๐ญ Arab tili", callback_data="๐ar"),
            InlineKeyboardButton(text="๐ฏ๐ต Yapon tili", callback_data="๐ja"),
        ],
        [
            InlineKeyboardButton(text="๐ฐ๐ท Koreys tili", callback_data="๐ko"),
            InlineKeyboardButton(text="๐จ๐ณ Xitoy tili", callback_data="๐zh"),
        ],
        [
            InlineKeyboardButton(text="๐ท๐บ Rus tili", callback_data="๐ru"),
            InlineKeyboardButton(text="๐ฎ๐น Fransuz tili", callback_data="๐fr"),
        ],
        [InlineKeyboardButton(text="๐ orqaga", callback_data="back")]
    ]
)