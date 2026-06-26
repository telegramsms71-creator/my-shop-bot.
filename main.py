import telebot

# الإعدادات
BOT_TOKEN = "8851361153:AAE_adap5TIOw1mmG8RHZWsn1Bk80SyVx8c"
ADMIN_ID = 8767607098
SUPPORT = "@elegramSMS_Support23"
CHANNELS = ["@sms20262", "@sms202622", "@tanadolsms", "@freemoney20262"]

bot = telebot.TeleBot(BOT_TOKEN)
users_db = set()

# قائمة الخدمات
SERVICES = {
    "btn_tg": {"name": "✈️ تليجرام", "items": {
        "البرازيل": "0.50$", "كندا": "0.30$", "أمريكا": "0.40$", "سوريا": "1.10$",
        "ماينمار": "0.23$", "الهند": "0.18$", "إيران": "0.25$"
    }},
    "btn_fb": {"name": "🔵 فيسبوك", "items": {"ألمانيا": "0.20$", "السودان": "0.20$", "الأردن": "0.30$"}},
    "btn_ig": {"name": "📸 إنستقرام", "items": {"غانا": "0.25$", "الأردن": "0.30$"}},
    "btn_tt": {"name": "🎵 تيك توك", "items": {"النرويج": "0.30$", "أمريكا": "0.35$"}},
    "btn_apple": {"name": "🍎 أبل", "items": {"السودان": "0.30$", "زيمبابوي": "0.25$"}},
    "btn_payp": {"name": "💰 باي بال", "items": {"فنزويلا": "0.30$", "مصر": "0.40$"}}
}

PAYMENT_TEXT = """💳 **| جميع طرق الدفع المعتمدة:**
💎 **Crypto:**
• USDT (TRC-20): `TRHUB8kuMpdCoDzST6c4AJ4cJdk6Ttoz97`
• USDT (ERC-20): `0x8D7dDE7719e9d6D3e5175CE170Fae00372715493`
• USDT (BEP-20): `0x8D7dDE7719e9d6D3e5175CE170Fae00372715493`
• USDT (Polygon): `0xA7fE0a5Ae6Adcd5b47df238F836449b4d0866155`
• TON Network: `UQBEej0PxeZK8DyVwkAVQznE1FrMiEbxxJSia7MhS4H1Co7`

🏦 **محافظ إلكترونية:**
• C-Wallet: `61824874`
• FaucetPay: `Telegramsms71@gmail.com`
"""

def check_sub(user_id):
    for ch in CHANNELS:
        try:
            if bot.get_chat_member(ch, user_id).status in ['left', 'kicked']: return False
        except: return False
    return True

def send_main_menu(m):
    kb = telebot.types.InlineKeyboardMarkup()
    # استخدام kb.row لضمان كل زر في سطر منفصل
    for key, val in SERVICES.items():
        kb.row(telebot.types.InlineKeyboardButton(val["name"], callback_data=key))
    kb.row(telebot.types.InlineKeyboardButton("💳 طرق الدفع", callback_data="btn_pay"))
    kb.row(telebot.types.InlineKeyboardButton("📞 الدعم الفني", url=f"https://t.me/{SUPPORT[1:]}"))
    
    text = f"✨ **أهلاً بك في المتجر الرسمي**\n\n🆔 **معرفك:** `{m.chat.id}`\n💰 **رصيدك:** `0.00$`\n---\nاختر من القائمة أدناه:"
    bot.send_message(m.chat.id, text, reply_markup=kb, parse_mode="Markdown")

@bot.message_handler(commands=['start'])
def start(m):
    users_db.add(m.chat.id)
    if check_sub(m.chat.id): send_main_menu(m)
    else:
        kb = telebot.types.InlineKeyboardMarkup()
        for ch in CHANNELS: kb.row(telebot.types.InlineKeyboardButton(f"اشترك في {ch}", url=f"https://t.me/{ch[1:]}"))
        kb.row(telebot.types.InlineKeyboardButton("🔄 تحقق من الاشتراك", callback_data="check_sub"))
        bot.send_message(m.chat.id, "⚠️ **يجب الاشتراك في القنوات أولاً:**", reply_markup=kb)

@bot.message_handler(commands=['broadcast'])
def broadcast(m):
    if m.chat.id == ADMIN_ID:
        msg = m.text.replace("/broadcast ", "")
        for user in users_db:
            try: bot.send_message(user, f"🔔 **إشعار من الإدارة:**\n{msg}")
            except: pass

@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    cid, mid = call.message.chat.id, call.message.message_id
    if call.data == "check_sub":
        if check_sub(cid): bot.delete_message(cid, mid); send_main_menu(call.message)
    
    elif call.data.startswith("order_"):
        data = call.data.split("_")
        price_usdt = data[2].replace("$", "")
        price_stars = int(float(price_usdt) * 100)
        
        text = f"📄 **تفاصيل الطلب:**\n\n🏷 **الخدمة:** `{data[1]}`\n💳 **السعر:** `{price_usdt} USDT / ⭐ {price_stars} نجمة`\n\nاختر طريقة الشراء:"
        kb = telebot.types.InlineKeyboardMarkup()
        kb.row(telebot.types.InlineKeyboardButton("💳 شراء بـ USDT", url=f"https://t.me/{SUPPORT[1:]}"))
        kb.row(telebot.types.InlineKeyboardButton("🌟 شراء بالنجوم", url=f"https://t.me/{SUPPORT[1:]}"))
        kb.row(telebot.types.InlineKeyboardButton("🔙 عودة", callback_data="back_main"))
        bot.edit_message_text(text, cid, mid, reply_markup=kb, parse_mode="Markdown")
        
    elif call.data in SERVICES:
        srv = SERVICES[call.data]
        kb = telebot.types.InlineKeyboardMarkup()
        for c, p in srv["items"].items(): kb.row(telebot.types.InlineKeyboardButton(f"{c} | {p}", callback_data=f"order_{c}_{p}"))
        kb.row(telebot.types.InlineKeyboardButton("🔙 عودة", callback_data="back_main"))
        bot.edit_message_text(f"🛍 **خدمات {srv['name']}**", cid, mid, reply_markup=kb)
        
    elif call.data == "btn_pay":
        kb = telebot.types.InlineKeyboardMarkup(); kb.row(telebot.types.InlineKeyboardButton("🔙 عودة", callback_data="back_main"))
        bot.edit_message_text(PAYMENT_TEXT, cid, mid, reply_markup=kb, parse_mode="Markdown")
    
    elif call.data == "back_main":
        bot.delete_message(cid, mid); send_main_menu(call.message)

bot.polling(none_stop=True)
