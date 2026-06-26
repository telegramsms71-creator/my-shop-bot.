import telebot
import sqlite3

# الإعدادات
BOT_TOKEN = "8851361153:AAE_adap5TIOw1mmG8RHZWsn1Bk80SyVx8c"
ADMIN_ID = "8767607098"
SUPPORT = "@elegramSMS_Support27"
SUPPORT_STARS = "@elegramSMS_Support27"
CHANNELS = ["@sms20262", "@sms202622", "@tanadolsms", "@freemoney20262"]

bot = telebot.TeleBot(BOT_TOKEN)

# تهيئة قاعدة البيانات
def init_db():
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS users (user_id INTEGER PRIMARY KEY)')
    conn.commit()
    conn.close()

def add_user(user_id):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('INSERT OR IGNORE INTO users (user_id) VALUES (?)', (user_id,))
    conn.commit()
    conn.close()

init_db()

# الخدمات
SERVICES_DATA = {
    "btn_tg": {"name": "✈️ تليجرام", "items": {"البرازيل": "0.50$", "كندا": "0.30$", "أمريكا": "0.40$", "سوريا": "1.10$", "ماينمار": "0.33$", "الهند": "0.40$", "إيران": "0.25$"}},
    "btn_fb": {"name": "🔵 فيسبوك", "items": {"غانا": "0.20$", "إندونيسيا": "0.15$", "زيمبابوي": "0.25$", "سودان": "0.15$"}},
    "btn_ig": {"name": "📸 إنستقرام", "items": {"غانا": "0.25$", "الأردن": "0.30$"}},
    "btn_tt": {"name": "🎵 تيك توك", "items": {"النرويج": "0.20$"}},
    "btn_apple": {"name": "🍎 أبل", "items": {"السودان": "0.30$", "زيمبابوي": "0.25$"}},
    "btn_payp": {"name": "💰 باي بال", "items": {"فنزويلا": "0.30$", "مصر": "0.40$"}},
    "btn_tinder": {"name": "🔥 Tinder", "items": {"إندونيسيا": "0.20$", "موزمبيق": "0.30$"}}
}

# قائمة الهدايا وطرق الدفع
GIFTS = {"gift_bear": {"name": "🧸 الدب", "price": "0.20$"}, "gift_rose": {"name": "🌹 الوردة", "price": "0.29$"}, "gift_cake": {"name": "🎂 الكيكة", "price": "0.54$"}, "gift_ring": {"name": "💍 الخاتم", "price": "1.10$"}}

PAYMENTS = {
    "TRC-20": "TRHUB8kuMpdCoDzST6c4AJ4cJdk6Ttoz97",
    "ERC-20": "0x8D7dDE7719e9d6D3e5175CE170Fae00372715493",
    "BEP-20": "0x8D7dDE7719e9d6D3e5175CE170Fae00372715493",
    "Polygon": "0xA7fE0a5Ae6Adcd5b47df238F836449b4d0866155",
    "TON": "UQBEej0PxeZK8DyVwkAVQznE1FrMiEbxxJSia7MhS4H1Co7",
    "C-Wallet": "61824874",
    "FaucetPay": "Telegramsms71@gmail.com"
}

def check_sub(user_id):
    for channel in CHANNELS:
        try:
            status = bot.get_chat_member(channel, user_id).status
            if status in ['left', 'kicked']: return False
        except: return False
    return True

def send_main_menu(m):
    add_user(m.chat.id)
    kb = telebot.types.InlineKeyboardMarkup()
    keys = list(SERVICES_DATA.keys())
    for i in range(0, len(keys), 2):
        if i + 1 < len(keys):
            kb.row(telebot.types.InlineKeyboardButton(SERVICES_DATA[keys[i]]["name"], callback_data=keys[i]),
                   telebot.types.InlineKeyboardButton(SERVICES_DATA[keys[i+1]]["name"], callback_data=keys[i+1]))
        else:
            kb.row(telebot.types.InlineKeyboardButton(SERVICES_DATA[keys[i]]["name"], callback_data=keys[i]))
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
    else: send_main_menu(m)

@bot.message_handler(commands=['broadcast'])
def broadcast(m):
    if str(m.chat.id) == ADMIN_ID:
        text = m.text.replace("/broadcast ", "")
        conn = sqlite3.connect('users.db')
        users = conn.execute('SELECT user_id FROM users').fetchall()
        conn.close()
        for user in users:
            try: bot.send_message(user[0], text)
            except: pass
        bot.send_message(m.chat.id, "✅ تم الإرسال للجميع.")

@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    cid, mid = call.message.chat.id, call.message.message_id
    if call.data == "check_sub":
        if check_sub(cid): bot.delete_message(cid, mid); send_main_menu(call.message)
        else: bot.answer_callback_query(call.id, "❌ لم تشترك بعد!")
    
    elif call.data == "btn_pay":
        kb = telebot.types.InlineKeyboardMarkup()
        for name, addr in PAYMENTS.items():
            kb.row(telebot.types.InlineKeyboardButton(f"نسخ {name}", callback_data=f"copy_{name}"))
        kb.row(telebot.types.InlineKeyboardButton("🔙 عودة", callback_data="back_main"))
        bot.edit_message_text("💳 **اضغط على اسم الطريقة لنسخ العنوان:**", cid, mid, reply_markup=kb)
        
    elif call.data.startswith("copy_"):
        name = call.data.split("_")[1]
        bot.answer_callback_query(call.id, f"عنوان {name}: {PAYMENTS[name]}", show_alert=True)

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
