import telebot

# الإعدادات
BOT_TOKEN = "8851361153:AAE_adap5TIOw1mmG8RHZWsn1Bk80SyVx8c"
SUPPORT = "@elegramSMS_Support27"        # دعم USDT العام
SUPPORT_STARS = "@elegramSMS_Support27"   # دعم النجوم

bot = telebot.TeleBot(BOT_TOKEN)

# الخدمات والهدايا
SERVICES_DATA = {
    "btn_tg": {"name": "✈️ تليجرام", "items": {"البرازيل": "0.50$", "كندا": "0.30$", "أمريكا": "0.40$"}},
    "btn_fb": {"name": "🔵 فيسبوك", "items": {"ألمانيا": "0.20$", "السودان": "0.20$", "الأردن": "0.30$"}},
    "btn_ig": {"name": "📸 إنستقرام", "items": {"غانا": "0.25$", "الأردن": "0.30$"}},
    "btn_tt": {"name": "🎵 تيك توك", "items": {"النرويج": "0.30$", "أمريكا": "0.35$"}},
    "btn_apple": {"name": "🍎 أبل", "items": {"السودان": "0.30$", "زيمبابوي": "0.25$"}},
    "btn_payp": {"name": "💰 باي بال", "items": {"فنزويلا": "0.30$", "مصر": "0.40$"}}
}

GIFTS = {
    "gift_bear": {"name": "🧸 الدب", "price": "0.20$"},
    "gift_rose": {"name": "🌹 الوردة", "price": "0.29$"},
    "gift_cake": {"name": "🎂 الكيكة", "price": "0.54$"},
    "gift_ring": {"name": "💍 الخاتم", "price": "1.10$"}
}

def send_main_menu(m):
    kb = telebot.types.InlineKeyboardMarkup()
    keys = list(SERVICES_DATA.keys())
    for i in range(0, len(keys), 2):
        kb.row(telebot.types.InlineKeyboardButton(SERVICES_DATA[keys[i]]["name"], callback_data=keys[i]),
               telebot.types.InlineKeyboardButton(SERVICES_DATA[keys[i+1]]["name"], callback_data=keys[i+1]))
    
    kb.row(telebot.types.InlineKeyboardButton("⭐ متجر النجوم", callback_data="star_shop"),
           telebot.types.InlineKeyboardButton("💳 طرق الدفع", callback_data="btn_pay"))
    kb.row(telebot.types.InlineKeyboardButton("📞 الدعم الفني", url=f"https://t.me/{SUPPORT[1:]}"))
    bot.send_message(m.chat.id, "✨ **أهلاً بك في المتجر الرسمي**", reply_markup=kb)

@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    cid, mid = call.message.chat.id, call.message.message_id
    
    # كل طرق الدفع في أزرار منفصلة لضمان عدم التلاصق
    if call.data == "btn_pay":
        kb = telebot.types.InlineKeyboardMarkup()
        kb.row(telebot.types.InlineKeyboardButton("💎 TRC-20: TRHUB8kuMpdCoDzST6c4AJ4cJdk6Ttoz97", callback_data="none"))
        kb.row(telebot.types.InlineKeyboardButton("💎 ERC-20: 0x8D7dDE7719e9d6D3e5175CE170Fae00372715493", callback_data="none"))
        kb.row(telebot.types.InlineKeyboardButton("💎 BEP-20: 0x8D7dDE7719e9d6D3e5175CE170Fae00372715493", callback_data="none"))
        kb.row(telebot.types.InlineKeyboardButton("💎 Polygon: 0xA7fE0a5Ae6Adcd5b47df238F836449b4d0866155", callback_data="none"))
        kb.row(telebot.types.InlineKeyboardButton("💎 TON: UQBEej0PxeZK8DyVwkAVQznE1FrMiEbxxJSia7MhS4H1Co7", callback_data="none"))
        kb.row(telebot.types.InlineKeyboardButton("🏦 C-Wallet: 61824874", callback_data="none"))
        kb.row(telebot.types.InlineKeyboardButton("🏦 FaucetPay: Telegramsms71@gmail.com", callback_data="none"))
        kb.row(telebot.types.InlineKeyboardButton("🔙 عودة", callback_data="back_main"))
        bot.edit_message_text("💳 **جميع طرق الدفع المعتمدة:**", cid, mid, reply_markup=kb)

    elif call.data in SERVICES_DATA:
        kb = telebot.types.InlineKeyboardMarkup()
        for country, price in SERVICES_DATA[call.data]["items"].items():
            kb.row(telebot.types.InlineKeyboardButton(f"{country} | {price}", callback_data="buy_action"))
        kb.row(telebot.types.InlineKeyboardButton("🔙 عودة", callback_data="back_main"))
        bot.edit_message_text("📍 **اختر الدولة:**", cid, mid, reply_markup=kb)

    elif call.data == "star_shop":
        kb = telebot.types.InlineKeyboardMarkup()
        for g_id, g_info in GIFTS.items():
            kb.row(telebot.types.InlineKeyboardButton(f"{g_info['name']} | {g_info['price']}", callback_data="buy_action"))
        kb.row(telebot.types.InlineKeyboardButton("🔙 عودة", callback_data="back_main"))
        bot.edit_message_text("⭐ **متجر النجوم:**", cid, mid, reply_markup=kb)

    elif call.data == "buy_action":
        kb = telebot.types.InlineKeyboardMarkup()
        kb.row(telebot.types.InlineKeyboardButton("💳 شراء بـ USDT", url=f"https://t.me/{SUPPORT[1:]}"))
        kb.row(telebot.types.InlineKeyboardButton("🌟 شراء بالنجوم", url=f"https://t.me/{SUPPORT_STARS[1:]}"))
        kb.row(telebot.types.InlineKeyboardButton("🔙 عودة", callback_data="back_main"))
        bot.edit_message_text("✅ **اختر وسيلة الشراء:**", cid, mid, reply_markup=kb)

    elif call.data == "back_main":
        bot.delete_message(cid, mid); send_main_menu(call.message)

@bot.message_handler(commands=['start'])
def start(m):
    send_main_menu(m)

bot.polling(none_stop=True)
