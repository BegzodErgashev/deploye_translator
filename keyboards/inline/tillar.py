from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
btn = InlineKeyboardMarkup(
    inline_keyboard=[
       [
           InlineKeyboardButton(text="🇺🇿 O'zbek tili", callback_data="👍uz"),
           InlineKeyboardButton(text="🇬🇧 Ingliz tili", callback_data="👍en"),
       ],
        [
            InlineKeyboardButton(text="🇪🇭 Arab tili", callback_data="👍ar"),
            InlineKeyboardButton(text="🇯🇵 Yapon tili", callback_data="👍ja"),
        ],
        [
            InlineKeyboardButton(text="🇰🇷 Koreys tili", callback_data="👍ko"),
            InlineKeyboardButton(text="🇨🇳 Xitoy tili", callback_data="👍zh"),
        ],
        [
            InlineKeyboardButton(text="🇷🇺 Rus tili", callback_data="👍ru"),
            InlineKeyboardButton(text="🇮🇹 Fransuz tili", callback_data="👍fr"),
        ]
    ]
)
btn_two = InlineKeyboardMarkup(
    inline_keyboard=[
       [
           InlineKeyboardButton(text="🇺🇿 O'zbek tili", callback_data="👎uz"),
           InlineKeyboardButton(text="🇬🇧 Ingliz tili", callback_data="👎en"),
       ],
        [
            InlineKeyboardButton(text="🇪🇭 Arab tili", callback_data="👎ar"),
            InlineKeyboardButton(text="🇯🇵 Yapon tili", callback_data="👎ja"),
        ],
        [
            InlineKeyboardButton(text="🇰🇷 Koreys tili", callback_data="👎ko"),
            InlineKeyboardButton(text="🇨🇳 Xitoy tili", callback_data="👎zh"),
        ],
        [
            InlineKeyboardButton(text="🇷🇺 Rus tili", callback_data="👎ru"),
            InlineKeyboardButton(text="🇮🇹 Fransuz tili", callback_data="👎fr"),
        ],
        [InlineKeyboardButton(text="🔙 orqaga", callback_data="back")]
    ]
)