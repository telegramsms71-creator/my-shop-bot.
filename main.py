import telebot

BOT_TOKEN = "8851361153:AAE_adap5TIOw1mmG8RHZWsn1Bk80SyVx8c"
SUPPORT = "@elegramSMS_Support23"
SUPPORT_STARS = "@elegramSMS_Support27"
CHANNELS = ["@sms20262", "@sms202622", "@tanadolsms", "@freemoney20262"]

bot = telebot.TeleBot(BOT_TOKEN)

SERVICES = {
    "btn_tg": {"name": "✈️ تليجرام", "items": {"البرازيل": "0.50$", "كندا": "0.30$", "أمريكا": "0.40$", "سوريا": "1.10$"}},
    "btn_fb": {"name": "🔵 فيسبوك", "items": {"ألمانيا": "0.20$", "السودان": "0.20$", "الأردن": "0.30$"}},
    "btn_ig": {"name": "📸 إنستقرام", "items": {"غانا": "0.25$", "الأردن": "0.30$"}},
    "btn_tt": {"name": "🎵 تيك توك", "items": {"النرويج": "0.30$", "أمريكا": "0.35$"}},
    "btn_apple": {"name": "🍎 أبل", "items": {"السودان": "0.30$", "زيمبابوي": "0.25$"}},
    "btn_payp": {"name": "💰 باي بال", "items": {"فنزويلا": "0.30$", "مصر": "0.40$"}}
}

def send_main_menu(m):
    kb = telebot.types.InlineKeyboardMarkup()
    for key, val in SERVICES.items():
        kb.row(telebot.types.InlineKeyboardButton(val["name"], callback_data=key))
    # تصميم الأزرار الثنائية كما في الصورة
    kb.row(telebot.types.InlineKeyboardButton("📖 تعليمات", callback_data="none"),
           telebot.types.InlineKeyboardButton("✅ تفعيلات", callback_data="none"))
    kb.row(telebot.types.InlineKeyboardButton("💰 ربح", callback_data="none"),
           telebot.types.InlineKeyboardButton("🔄 تبادل إحالات", callback_data="none"))
    kb.row(telebot.types.InlineKeyboardButton("💳 طرق الدفع", callback_data="btn_pay"),
           telebot.types.InlineKeyboardButton("⭐ متجر النجوم", callback_data="none"))
    kb.row(telebot.types.InlineKeyboardButton("🎁 رابط دعوتك", callback_data="none"),
           telebot.types.InlineKeyboardButton("📞 الدعم الفني", url=f"https://t.me/{SUPPORT[1:]}"))
    bot.send_message(m.chat.id, "✨ **أهلاً بك في المتجر الرسمي**\nاختر الخدمة:", reply_markup=kb)

@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    cid, mid = call.message.chat.id, call.message.message_id
    
    if call.data == "btn_pay":
        kb = telebot.types.InlineKeyboardMarkup()
        kb.row(telebot.types.InlineKeyboardButton("💎 USDT(TRC20): TRHUB8kuMpdCoDzST6c4AJ4cJdk6Ttoz97", callback_data="none"))
        kb.row(telebot.types.InlineKeyboardButton("💎 USDT(ERC20): 0x8D7dDE7719e9d6D3e5175CE170Fae00372715493", callback_data="none"))
        kb.row(telebot.types.InlineKeyboardButton("💎 USDT(BEP20): 0x8D7dDE7719e9d6D3e5175CE170Fae00372715493", callback_data="none"))
        kb.row(telebot.types.InlineKeyboardButton("💎 TON: UQBEej0PxeZK8DyVwkAVQznE1FrMiEbxxJSia7MhS4H1Co7", callback_data="none"))
        kb.row(telebot.types.InlineKeyboardButton("🏦 C-Wallet: 61824874", callback_data="none"))
        kb.row(telebot.types.InlineKeyboardButton("🔙 عودة", callback_data="back_main"))
        bot.edit_message_text("💳 **طرق الدفع (اضغط للنسخ):**", cid, mid, reply_markup=kb)

    elif call.data.startswith("order_"):
        data = call.data.split("_")
        text = f"📄 **الخدمة:** {data[1]}\n💰 **السعر:** {data[2]}"
        kb = telebot.types.InlineKeyboardMarkup()
        kb.row(telebot.types.InlineKeyboardButton("💳 شراء بـ USDT", url=f"https://t.me/{SUPPORT[1:]}"))
        kb.row(telebot.types.InlineKeyboardButton("🌟 شراء بالنجوم", url=f"https://t.me/{SUPPORT_STARS[1:]}"))
        kb.row(telebot.types.InlineKeyboardButton("🔙 عودة", callback_data="back_main"))
        bot.edit_message_text(text, cid, mid, reply_markup=kb)

    elif call.data in SERVICES:
        kb = telebot.types.InlineKeyboardMarkup()
        for c, p in SERVICES[call.data]["items"].items():
            kb.row(telebot.types.InlineKeyboardButton(f"{c} | {p}", callback_data=f"order_{c}_{p}"))
        kb.row(telebot.types.InlineKeyboardButton("🔙 عودة", callback_data="back_main"))
        bot.edit_message_text("اختر الدولة:", cid, mid, reply_markup=kb)
        
    elif call.data == "back_main":
        bot.delete_message(cid, mid); send_main_menu(call.message)

bot.polling(none_stop=True)
