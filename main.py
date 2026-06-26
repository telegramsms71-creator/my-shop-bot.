import telebot

# إعدادات البوت الأساسية
BOT_TOKEN = "8851361153:AAE_adap5TIOw1mmG8RHZWsn1Bk80SyVx8c"
BOT_USERNAME = "sms2221bot"
SUPPORT = "@elegramSMS_Support27"
bot = telebot.TeleBot(BOT_TOKEN)

# الروابط والبيانات
CHANNELS = {
    "act": "https://t.me/sms20262",
    "ins": "https://t.me/sms202622",
    "ex": "https://t.me/tanadolsms",
    "pro": "https://t.me/freemoney20262"
}

SERVICES = {
    "btn_tg": {"name": "✈️ تليجرام", "items": {"البرازيل": "0.50$", "كندا": "0.30$", "أمريكا": "0.40$", "سوريا": "1.10$", "مصر": "0.50$", "نيجيريا": "0.40$"}},
    "btn_fb": {"name": "🔵 فيسبوك", "items": {"ألمانيا": "0.20$", "السودان": "0.20$", "الأردن": "0.30$", "مصر": "0.25$"}},
    "btn_ig": {"name": "📸 إنستقرام", "items": {"غانا": "0.25$", "الأردن": "0.30$", "السعودية": "0.40$"}},
    "btn_tt": {"name": "🎵 تيك توك", "items": {"النرويج": "0.30$", "أمريكا": "0.35$"}},
    "btn_apple": {"name": "🍎 أبل", "items": {"السودان": "0.30$", "زيمبابوي": "0.25$"}},
    "btn_paypal": {"name": "💰 باي بال", "items": {"فنزويلا": "0.30$", "مصر": "0.40$"}}
}

PAYMENT_TEXT = """💳 **| جميع طرق الدفع المعتمدة:**

💎 **العملات الرقمية (Crypto):**
• USDT (TRC-20): `TRHUB8kuMpdCoDzST6c4AJ4cJdk6Ttoz97`
• USDT (ERC-20): `0x8D7dDE7719e9d6D3e5175CE170Fae00372715493`
• USDT (Polygon): `0xA7fE0a5Ae6Adcd5b47df238F836449b4d0866155`
• TON Network: `UQBEej0PxeZK8DyVwkAVQznE1FrMiEbxxJSia7MhS4H1Co7`

🏦 **محافظ إلكترونية:**
• C-Wallet (ID): `61824874`
• FaucetPay (Email): `Telegramsms71@gmail.com`

⚠️ *يرجى إرسال صورة الإيصال للدعم الفني بعد التحويل.*"""

def send_main_menu(m):
    kb = telebot.types.InlineKeyboardMarkup(row_width=2)
    for key, val in SERVICES.items():
        kb.add(telebot.types.InlineKeyboardButton(val["name"], callback_data=key))
    kb.add(
        telebot.types.InlineKeyboardButton("✅ تفعيلات", url=CHANNELS["act"]),
        telebot.types.InlineKeyboardButton("📖 تعليمات", url=CHANNELS["ins"]),
        telebot.types.InlineKeyboardButton("🔄 تبادل إحالات", url=CHANNELS["ex"]),
        telebot.types.InlineKeyboardButton("💰 ربح", url=CHANNELS["pro"]),
        telebot.types.InlineKeyboardButton("⭐️ متجر النجوم", callback_data="btn_stars"),
        telebot.types.InlineKeyboardButton("💳 طرق الدفع", callback_data="btn_pay"),
        telebot.types.InlineKeyboardButton("📞 الدعم الفني", url=f"https://t.me/{SUPPORT[1:]}"),
        telebot.types.InlineKeyboardButton("🎁 رابط دعوتك", callback_data="btn_ref")
    )
    bot.send_message(m.chat.id, "✨ **أهلاً بك في المتجر الرسمي**\nاختر الخدمة المطلوبة:", reply_markup=kb, parse_mode="Markdown")

@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    cid, mid = call.message.chat.id, call.message.message_id
    if call.data == "btn_ref":
        bot.send_message(cid, f"🎁 **رابط الدعوة الخاص بك:**\n`https://t.me/{BOT_USERNAME}?start={cid}`")
    elif call.data == "back_main":
        bot.delete_message(cid, mid); send_main_menu(call.message)
    elif call.data in SERVICES:
        srv = SERVICES[call.data]
        kb = telebot.types.InlineKeyboardMarkup(row_width=1)
        for country, price in srv["items"].items():
            kb.add(telebot.types.InlineKeyboardButton(f"{country} | {price}", callback_data="order"))
        kb.add(telebot.types.InlineKeyboardButton("🔙 عودة", callback_data="back_main"))
        bot.edit_message_text(f"🛍 **خدمات {srv['name']}**", cid, mid, reply_markup=kb)
    elif call.data == "btn_pay":
        kb = telebot.types.InlineKeyboardMarkup(); kb.add(telebot.types.InlineKeyboardButton("🔙 عودة", callback_data="back_main"))
        bot.edit_message_text(PAYMENT_TEXT, cid, mid, reply_markup=kb, parse_mode="Markdown")
    elif call.data == "btn_stars":
        kb = telebot.types.InlineKeyboardMarkup(); kb.add(telebot.types.InlineKeyboardButton("🔙 عودة", callback_data="back_main"))
        bot.edit_message_text("⭐️ **متجر النجوم:**\n\n🍰 كيكة | `0.55$`\n💍 خاتم | `1.10$`\n🌹 وردة | `0.29$`\n🐻 دب | `0.20$`\n💎 نجمة | `0.015$`", cid, mid, reply_markup=kb, parse_mode="Markdown")

@bot.message_handler(commands=['start'])
def start(m): send_main_menu(m)

bot.remove_webhook()
bot.polling(none_stop=True)
