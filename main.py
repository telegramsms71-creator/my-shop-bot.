import telebot
from telebot import types

# التوكن الخاص بك
BOT_TOKEN = "8851361153:AAHEmdqQqfNn9kDt2xHNinQneGa1MBI-9xU"
bot = telebot.TeleBot(BOT_TOKEN)

SUPPORT_USER = "@elegramSMS_Support20"
CHANNELS = [
    {"name": "ربح مجاني", "url": "https://t.me/freemoney20262", "id": "@freemoney20262"},
    {"name": "تعليمات", "url": "https://t.me/sms202622", "id": "@sms202622"},
    {"name": "تفعيلات", "url": "https://t.me/sms20262", "id": "@sms20262"}
]

def check_sub(user_id):
    for ch in CHANNELS:
        try:
            status = bot.get_chat_member(ch["id"], user_id).status
            if status not in ['member', 'administrator', 'creator']: return False
        except: return False
    return True

def show_main_menu(chat_id):
    markup = types.InlineKeyboardMarkup(row_width=2)
    buttons = [
        types.InlineKeyboardButton("📱 واتساب", callback_data="buy_whatsapp"),
        types.InlineKeyboardButton("🔵 فيسبوك", callback_data="buy_facebook"),
        types.InlineKeyboardButton("📸 إنستغرام", callback_data="buy_instagram"),
        types.InlineKeyboardButton("🎵 تيك توك", callback_data="buy_tiktok"),
        types.InlineKeyboardButton("✈️ تليجرام", callback_data="buy_telegram"),
        types.InlineKeyboardButton("⭐ متجر النجوم", callback_data="stars_shop"),
        types.InlineKeyboardButton("💳 طرق الدفع", callback_data="payment_methods")
    ]
    markup.add(*buttons)
    bot.send_message(chat_id, "🌐 **أهلاً بك في خدمة TELEGRAM SMS**\nاختر الخدمة المطلوبة:", reply_markup=markup)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    if not check_sub(message.from_user.id):
        markup = types.InlineKeyboardMarkup()
        for ch in CHANNELS: markup.add(types.InlineKeyboardButton(f"اشترك في {ch['name']} 📢", url=ch["url"]))
        markup.add(types.InlineKeyboardButton("تحققت من الاشتراك ✅", callback_data="check_join"))
        bot.send_message(message.chat.id, "⚠️ **يجب الاشتراك في قنواتنا أولاً:**", reply_markup=markup)
        return
    show_main_menu(message.chat.id)

@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == "check_join":
        if check_sub(call.from_user.id): show_main_menu(call.message.chat.id)
        else: bot.answer_callback_query(call.id, "لم تشترك في جميع القنوات بعد!", show_alert=True)
            
    elif call.data == "payment_methods":
        msg = (
            "💰 **طرق الدفع المتاحة:**\n\n"
            "💎 **TON:** `UQBEej0PxeZK8DyVwkAVQznE1FrMi0EbxxJSia7MhS4H1Co7`\n"
            "• **Polygon/BEP20:** `0xA7fE0a5Ae6Adcd5b47df238F836449b4d0866155`\n"
            "• **ERC20:** `0x8D7dDE7719e9d6D3e5175CE170Fae00372715493`\n"
            "• **TRC20:** `TRHUB8kuMpdCoDzST6c4AJ4cJdk6Ttoz97`\n\n"
            "🔹 **Cwallet ID:** `61824874`\n"
            "🔹 **FaucetPay Email:** `telegramsms71@gmail.com`\n\n"
            f"⚠️ *أرسل الإيصال للدعم:* {SUPPORT_USER}"
        )
        bot.send_message(call.message.chat.id, msg, parse_mode="Markdown")

    elif call.data == "stars_shop":
        msg = ("⭐ **متجر النجوم:**\nنجمة: 0.015$ | دب: 0.22$ | وردة: 0.32$ | كيكة: 0.7$ | خاتم: 1.2$\n" + f"للطلب: {SUPPORT_USER}")
        bot.send_message(call.message.chat.id, msg)

    elif call.data == "buy_telegram":
        msg = ("✈️ **أسعار تليجرام:**\nأمريكا: 20ن (0.25$) | مصر: 50ن (0.5$) | سوريا: 110ن (1.10$)\nالهند: 30ن (0.3$) | سلام مختلط: 28ن (0.28$)\n" + f"للطلب: {SUPPORT_USER}")
        bot.send_message(call.message.chat.id, msg)

    elif call.data == "buy_whatsapp":
        msg = "📱 **أسعار واتساب:**\nنيجيريا: 20ن | السودان: 15ن | فنزويلا: 25ن | أوكرانيا: 40ن\nجابون: 25ن | ألمانيا: 20ن | غانا: 15ن | مدغشقر: 30ن | فرنسا: 50ن"
        bot.send_message(call.message.chat.id, msg)

    elif call.data == "buy_facebook":
        msg = "🔵 **أسعار فيسبوك:**\nألمانيا: 20ن | مدغشقر: 20ن | السودان: 20ن | الأردن: 30ن | غانا: 25ن"
        bot.send_message(call.message.chat.id, msg)

    elif call.data == "buy_instagram":
        msg = "📸 **أسعار إنستغرام:**\nغانا: 25ن | الأردن: 30ن"
        bot.send_message(call.message.chat.id, msg)

    elif call.data == "buy_tiktok":
        msg = "🎵 **أسعار تيك توك:**\nالنرويج: 0.3 نجمة"
        bot.send_message(call.message.chat.id, msg)

    bot.answer_callback_query(call.id)

print("البوت يعمل الآن...")
bot.polling(none_stop=True)
