import telebot
from telebot import types
import os

# إعداد البوت
BOT_TOKEN = os.getenv('8851361153:AAHuWsxPX3S6bDt3mixzL5OzvidSqWSShQM')
bot = telebot.TeleBot(BOT_TOKEN)

# بيانات الدعم والقنوات
SUPPORT_USER = "@elegramSMS_Support20"
CHANNELS = [
    {"name": "ربح مجاني", "url": "https://t.me/freemoney20262", "id": "@freemoney20262"},
    {"name": "تعليمات", "url": "https://t.me/sms202622", "id": "@sms202622"},
    {"name": "تفعيلات", "url": "https://t.me/sms20262", "id": "@sms20262"}
]

# دالة التحقق من الاشتراك
def check_sub(user_id):
    for ch in CHANNELS:
        try:
            status = bot.get_chat_member(ch["id"], user_id).status
            if status not in ['member', 'administrator', 'creator']:
                return False
        except:
            return False
    return True

# القائمة الرئيسية
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
        for ch in CHANNELS:
            markup.add(types.InlineKeyboardButton(f"اشترك في {ch['name']} 📢", url=ch["url"]))
        markup.add(types.InlineKeyboardButton("تحققت من الاشتراك ✅", callback_data="check_join"))
        bot.send_message(message.chat.id, "⚠️ **عذراً، يجب عليك الاشتراك في قنواتنا أولاً:**", reply_markup=markup)
        return
    show_main_menu(message.chat.id)

@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == "check_join":
        if check_sub(call.from_user.id):
            bot.answer_callback_query(call.id, "شكراً لاشتراكك!")
            show_main_menu(call.message.chat.id)
        else:
            bot.answer_callback_query(call.id, "لم تشترك في جميع القنوات بعد!", show_alert=True)
            
    elif call.data == "payment_methods":
        msg = (
            "💰 **طرق الدفع المتاحة:**\n\n"
            "💎 **محفظة TON:**\n`UQBEej0PxeZK8DyVwkAVQznE1FrMi0EbxxJSia7MhS4H1Co7`\n\n"
            "• **Polygon:** `0xA7fE0a5Ae6Adcd5b47df238F836449b4d0866155`\n"
            "• **BEP20:** `0xA7fE0a5Ae6Adcd5b47df238F836449b4d0866155`\n"
            "• **ERC20:** `0x8D7dDE7719e9d6D3e5175CE170Fae00372715493`\n"
            "• **TRC20:** `TRHUB8kuMpdCoDzST6c4AJ4cJdk6Ttoz97`\n\n"
            "🔹 **Cwallet ID:** `61824874`\n"
            "🔹 **FaucetPay Email:** `telegramsms71@gmail.com`\n\n"
            f"⚠️ *بعد التحويل، أرسل الإيصال للدعم:* {SUPPORT_USER}"
        )
        bot.send_message(call.message.chat.id, msg, parse_mode="Markdown")

    elif call.data == "stars_shop":
        msg = (
            "⭐ **متجر النجوم والهدايا:**\n\n"
            "🌟 النجمة الواحدة: 0.015$\n"
            "🧸 دب: 0.22$ | 🌹 وردة: 0.32$\n"
            "🎂 كيكة: 0.7$ | 💍 خاتم: 1.2$\n\n"
            f"للطلب، تواصل مع الدعم: {SUPPORT_USER}"
        )
        bot.send_message(call.message.chat.id, msg)

    elif call.data == "buy_telegram":
        msg = (
            "✈️ **أسعار تليجرام:**\n\n"
            "🇺🇸 أمريكا: 0.25$ (20ن)\n"
            "🇪🇬 مصر: 0.5$ (50ن)\n"
            "🇸🇾 سوريا: 1.10$ (110ن)\n"
            "🇮🇳 الهند: 0.3$ (30ن)\n"
            "✨ سلام مختلط: 0.28$ (28ن)\n\n"
            f"للطلب تواصل مع الدعم: {SUPPORT_USER}"
        )
        bot.send_message(call.message.chat.id, msg)

    elif call.data == "buy_whatsapp":
        msg = "📱 **أسعار واتساب:**\n\nنيجيريا: 0.2$ (20ن) | السودان: 0.15$ (15ن)\nفنزويلا: 0.25$ (25ن) | أوكرانيا: 0.4$ (40ن)\nجابون: 0.25$ (25ن) | ألمانيا: 0.2$ (20ن)\nغانا: 0.15$ (15ن) | مدغشقر: 0.3$ (30ن)\nفرنسا: 0.5$ (50ن)"
        bot.send_message(call.message.chat.id, msg)

    elif call.data == "buy_facebook":
        msg = "🔵 **أسعار فيسبوك:**\n\nألمانيا: 0.2$ (20ن)\nمدغشقر: 0.2$ (20ن)\nالسودان: 0.2$ (20ن)\nالأردن: 0.3$ (30ن)\nغانا: 0.25$ (25ن)"
        bot.send_message(call.message.chat.id, msg)

    elif call.data == "buy_instagram":
        msg = "📸 **أسعار إنستغرام:**\n\nغانا: 0.25$ (25ن)\nالأردن: 0.3$ (30ن)"
        bot.send_message(call.message.chat.id, msg)

    elif call.data == "buy_tiktok":
        msg = "🎵 **أسعار تيك توك:**\n\nالنرويج: 0.3$ (0.3ن)"
        bot.send_message(call.message.chat.id, msg)

    bot.answer_callback_query(call.id)

bot.polling(none_stop=True)
