import telebot

# الإعدادات الأساسية
BOT_TOKEN = "8851361153:AAE_adap5TIOw1mmG8RHZWsn1Bk80SyVx8c"
SUPPORT = "@elegramSMS_Support27"        # دعم USDT العام
SUPPORT_STARS = "@elegramSMS_Support27"   # دعم النجوم المخصص

bot = telebot.TeleBot(BOT_TOKEN)

# الخدمات الأساسية (تظهر في صفين)
SERVICES = [
    ("btn_tg", "✈️ تليجرام"), ("btn_fb", "🔵 فيسبوك"),
    ("btn_ig", "📸 إنستقرام"), ("btn_tt", "🎵 تيك توك"),
    ("btn_apple", "🍎 أبل"), ("btn_payp", "💰 باي بال")
]

# الهدايا والأسعار المطلوبة
GIFTS = {
    "gift_bear": {"name": "🧸 الدب", "price": "0.20$"},
    "gift_rose": {"name": "🌹 الوردة", "price": "0.29$"},
    "gift_cake": {"name": "🎂 الكيكة", "price": "0.54$"},
    "gift_ring": {"name": "💍 الخاتم", "price": "1.10$"}
}

def send_main_menu(m):
    kb = telebot.types.InlineKeyboardMarkup()
    
    # 1. الخدمات في صفين (تصميم احترافي)
    for i in range(0, len(SERVICES), 2):
        kb.row(telebot.types.InlineKeyboardButton(SERVICES[i][1], callback_data=SERVICES[i][0]),
               telebot.types.InlineKeyboardButton(SERVICES[i+1][1], callback_data=SERVICES[i+1][0]))
    
    # 2. أزرار إضافية (متجر النجوم + الدعم)
    kb.row(telebot.types.InlineKeyboardButton("⭐ متجر النجوم", callback_data="star_shop"),
           telebot.types.InlineKeyboardButton("📞 الدعم الفني", url=f"https://t.me/{SUPPORT[1:]}"))
    
    text = "✨ **أهلاً بك في المتجر الرسمي**\nاختر الخدمة أو متجر النجوم:"
    bot.send_message(m.chat.id, text, reply_markup=kb, parse_mode="Markdown")

@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    cid, mid = call.message.chat.id, call.message.message_id
    
    # متجر النجوم (عرض الأسعار)
    if call.data == "star_shop":
        kb = telebot.types.InlineKeyboardMarkup()
        for g_id, g_info in GIFTS.items():
            kb.row(telebot.types.InlineKeyboardButton(f"{g_info['name']} | {g_info['price']}", callback_data=f"buy_{g_id}"))
        kb.row(telebot.types.InlineKeyboardButton("🔙 عودة", callback_data="back_main"))
        bot.edit_message_text("⭐ **متجر النجوم - اختر الهدية:**", cid, mid, reply_markup=kb)

    # طلب الهدية (توجيه لدعم النجوم 27)
    elif call.data.startswith("buy_"):
        gift_name = GIFTS[call.data.replace("buy_", "")]["name"]
        kb = telebot.types.InlineKeyboardMarkup()
        kb.row(telebot.types.InlineKeyboardButton("✅ طلب الهدية (دعم النجوم)", url=f"https://t.me/{SUPPORT_STARS[1:]}"))
        kb.row(telebot.types.InlineKeyboardButton("🔙 عودة للمتجر", callback_data="star_shop"))
        bot.edit_message_text(f"تواصل مع الدعم لإتمام طلب **{gift_name}**:", cid, mid, reply_markup=kb, parse_mode="Markdown")

    # التعامل مع الخدمات الأساسية
    elif call.data in [s[0] for s in SERVICES]:
        kb = telebot.types.InlineKeyboardMarkup()
        kb.row(telebot.types.InlineKeyboardButton("💳 شراء بـ USDT", url=f"https://t.me/{SUPPORT[1:]}"))
        kb.row(telebot.types.InlineKeyboardButton("🌟 شراء بالنجوم", url=f"https://t.me/{SUPPORT_STARS[1:]}"))
        kb.row(telebot.types.InlineKeyboardButton("🔙 عودة", callback_data="back_main"))
        bot.edit_message_text("اختر وسيلة الشراء:", cid, mid, reply_markup=kb)

    # العودة للقائمة الرئيسية
    elif call.data == "back_main":
        bot.delete_message(cid, mid)
        send_main_menu(call.message)

@bot.message_handler(commands=['start'])
def start(m):
    send_main_menu(m)

# التشغيل
print("البوت يعمل الآن...")
bot.polling(none_stop=True)
