import telebot

# الإعدادات
BOT_TOKEN = "8851361153:AAE_adap5TIOw1mmG8RHZWsn1Bk80SyVx8c"
ADMIN_ID = "8767607098"
SUPPORT = "@elegramSMS_Support23"
SUPPORT_STARS = "@elegramSMS_Support27"
CHANNELS = ["@sms20262", "@sms202622", "@tanadolsms", "@freemoney20262"]

bot = telebot.TeleBot(BOT_TOKEN)

# قائمة شاملة لكل الدول والخدمات
SERVICES_DATA = {
    "btn_tg": {"name": "✈️ تليجرام", "items": {"البرازيل": "0.50$", "كندا": "0.30$", "أمريكا": "0.40$", "سوريا": "1.10$", "ماينمار": "0.23$", "الهند": "0.18$", "إيران": "0.25$", "باكستان": "0.20$", "روسيا": "0.30$"}},
    "btn_fb": {"name": "🔵 فيسبوك", "items": {"ألمانيا": "0.20$", "السودان": "0.20$", "الأردن": "0.30$", "مصر": "0.40$", "العراق": "0.35$", "المغرب": "0.25$", "لبنان": "0.30$"}},
    "btn_ig": {"name": "📸 إنستقرام", "items": {"غانا": "0.25$", "الأردن": "0.30$", "المغرب": "0.40$", "تونس": "0.35$", "الجزائر": "0.30$", "ليبيا": "0.45$"}},
    "btn_tt": {"name": "🎵 تيك توك", "items": {"النرويج": "0.30$", "أمريكا": "0.35$", "تركيا": "0.25$", "السعودية": "0.50$", "الكويت": "0.60$"}},
    "btn_apple": {"name": "🍎 أبل", "items": {"السودان": "0.30$", "زيمبابوي": "0.25$", "نيجيريا": "0.45$", "كينيا": "0.35$", "جنوب أفريقيا": "0.40$"}},
    "btn_payp": {"name": "💰 باي بال", "items": {"فنزويلا": "0.30$", "مصر": "0.40$", "ليبيا": "0.50$", "اليمن": "0.60$", "عمان": "0.70$"}}
}

GIFTS = {
    "gift_bear": {"name": "🧸 الدب", "price": "0.20$"},
    "gift_rose": {"name": "🌹 الوردة", "price": "0.29$"},
    "gift_cake": {"name": "🎂 الكيكة", "price": "0.54$"},
    "gift_ring": {"name": "💍 الخاتم", "price": "1.10$"}
}

def check_sub(user_id):
    for channel in CHANNELS:
        try:
            status = bot.get_chat_member(channel, user_id).status
            if status in ['left', 'kicked']: return False
        except: return False
    return True

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

@bot.message_handler(commands=['start'])
def start(m):
    if not check_sub(m.chat.id):
        kb = telebot.types.InlineKeyboardMarkup()
        for ch in CHANNELS: kb.row(telebot.types.InlineKeyboardButton(f"اشترك في {ch}", url=f"https://t.me/{ch[1:]}"))
        kb.row(telebot.types.InlineKeyboardButton("✅ تحقق من الاشتراك", callback_data="check_sub"))
        bot.send_message(m.chat.id, "⚠️ **يجب عليك الاشتراك في القنوات أولاً:**", reply_markup=kb)
    else:
        send_main_menu(m)

@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    cid, mid = call.message.chat.id, call.message.message_id
    if call.data == "check_sub":
        if check_sub(cid): bot.delete_message(cid, mid); send_main_menu(call.message)
        else: bot.answer_callback_query(call.id, "❌ لم تشترك بعد!")
    
    elif call.data == "btn_pay":
        kb = telebot.types.InlineKeyboardMarkup()
        kb.row(telebot.types.InlineKeyboardButton("💎 TRC-20: TRHUB8kuMpdCoDzST6c4AJ4cJdk6Ttoz97", callback_data="none"))
        kb.row(telebot.types.InlineKeyboardButton("💎 ERC-20: 0x8D7dDE7719e9d6D3e5175CE170Fae00372715493", callback_data="none"))
        kb.row(telebot.types.InlineKeyboardButton("💎 BEP-20: 0x8D7dDE7719e9d6D3e5175CE170Fae00372715493", callback_data="none"))
        kb.row(telebot.types.InlineKeyboardButton("💎 TON: UQBEej0PxeZK8DyVwkAVQznE1FrMiEbxxJSia7MhS4H1Co7", callback_data="none"))
        kb.row(telebot.types.InlineKeyboardButton("🏦 C-Wallet: 61824874", callback_data="none"))
        kb.row(telebot.types.InlineKeyboardButton("🏦 FaucetPay: Telegramsms71@gmail.com", callback_data="none"))
        kb.row(telebot.types.InlineKeyboardButton("🔙 عودة", callback_data="back_main"))
        bot.edit_message_text("💳 **طرق الدفع:**", cid, mid, reply_markup=kb)

    elif call.data in SERVICES_DATA:
        kb = telebot.types.InlineKeyboardMarkup()
        items = list(SERVICES_DATA[call.data]["items"].items())
        for i in range(0, len(items), 2):
            if i + 1 < len(items):
                kb.row(telebot.types.InlineKeyboardButton(f"{items[i][0]} | {items[i][1]}", callback_data="buy_action"),
                       telebot.types.InlineKeyboardButton(f"{items[i+1][0]} | {items[i+1][1]}", callback_data="buy_action"))
            else:
                kb.row(telebot.types.InlineKeyboardButton(f"{items[i][0]} | {items[i][1]}", callback_data="buy_action"))
        kb.row(telebot.types.InlineKeyboardButton("🔙 عودة", callback_data="back_main"))
        bot.edit_message_text(f"📍 **{SERVICES_DATA[call.data]['name']} - اختر الدولة:**", cid, mid, reply_markup=kb)

    elif call.data == "star_shop":
        kb = telebot.types.InlineKeyboardMarkup()
        items = list(GIFTS.items())
        for i in range(0, len(items), 2):
            if i + 1 < len(items):
                kb.row(telebot.types.InlineKeyboardButton(f"{items[i][1]['name']} | {items[i][1]['price']}", callback_data="buy_action"),
                       telebot.types.InlineKeyboardButton(f"{items[i+1][1]['name']} | {items[i+1][1]['price']}", callback_data="buy_action"))
            else:
                kb.row(telebot.types.InlineKeyboardButton(f"{items[i][1]['name']} | {items[i][1]['price']}", callback_data="buy_action"))
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

bot.polling(none_stop=True)
