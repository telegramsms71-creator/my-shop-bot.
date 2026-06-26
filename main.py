import telebot
from telebot import types

BOT_TOKEN = "8851361153:AAHEmdqQqfNn9kDt2xHNinQneGa1MBI-9xU"
bot = telebot.TeleBot(BOT_TOKEN)

SUPPORT_USER = "@elegramSMS_Support20"
BOT_URL = "https://t.me/your_bot_username" # ضع رابط البوت هنا

# دالة القائمة الرئيسية بشكلها الجديد
def show_main_menu(chat_id):
    markup = types.InlineKeyboardMarkup()
    markup.row(types.InlineKeyboardButton("📱 واتساب", callback_data="buy_whatsapp"), 
               types.InlineKeyboardButton("🔵 فيسبوك", callback_data="buy_facebook"))
    markup.row(types.InlineKeyboardButton("✈️ تليجرام", callback_data="buy_telegram"), 
               types.InlineKeyboardButton("📸 إنستغرام", callback_data="buy_instagram"))
    markup.row(types.InlineKeyboardButton("🎵 تيك توك", callback_data="buy_tiktok"), 
               types.InlineKeyboardButton("⭐ متجر النجوم", callback_data="stars_shop"))
    markup.row(types.InlineKeyboardButton("💳 طرق الدفع", callback_data="payment_methods"))
    markup.row(types.InlineKeyboardButton("📢 دعوة أصدقائك", url=BOT_URL), 
               types.InlineKeyboardButton("📞 تواصل مع الدعم", url=f"https://t.me/{SUPPORT_USER.replace('@', '')}"))
    
    text = "🌐 **أهلاً بك في متجر TELEGRAM SMS**\n\nخدماتنا توفر لك أفضل الأرقام لتفعيل حساباتك.\nاختر الخدمة من الأزرار بالأسفل:"
    bot.send_message(chat_id, text, parse_mode="Markdown", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == "payment_methods":
        msg = (
            "💰 **طرق الدفع المتوفرة:**\n\n"
            "💎 *محفظة TON:* `UQBEej0PxeZK8DyVwkAVQznE1FrMi0EbxxJSia7MhS4H1Co7`\n\n"
            "• *Polygon/BEP20:* `0xA7fE0a5Ae6Adcd5b47df238F836449b4d0866155`\n"
            "• *ERC20:* `0x8D7dDE7719e9d6D3e5175CE170Fae00372715493`\n"
            "• *TRC20:* `TRHUB8kuMpdCoDzST6c4AJ4cJdk6Ttoz97`\n\n"
            "🔹 *Cwallet ID:* `61824874`\n"
            "🔹 *FaucetPay Email:* `telegramsms71@gmail.com`\n\n"
            f"⚠️ *بعد التحويل، أرسل الإيصال للدعم:* {SUPPORT_USER}"
        )
        bot.send_message(call.message.chat.id, msg, parse_mode="Markdown")

    elif call.data == "buy_telegram":
        msg = (
            "✈️ **أسعار تليجرام:**\n\n"
            "| الدولة | السعر | النجوم |\n"
            "| :--- | :--- | :--- |\n"
            "| أمريكا | 0.25$ | 20ن |\n"
            "| مصر | 0.5$ | 50ن |\n"
            "| سوريا | 1.10$ | 110ن |\n"
            "| الهند | 0.3$ | 30ن |\n"
            "| مختلط | 0.28$ | 28ن |\n"
        )
        bot.send_message(call.message.chat.id, msg, parse_mode="Markdown")

    elif call.data == "buy_whatsapp":
        msg = (
            "📱 **أسعار واتساب:**\n\n"
            "نيجيريا: 20ن | السودان: 15ن | فنزويلا: 25ن | أوكرانيا: 40ن\n"
            "جابون: 25ن | ألمانيا: 20ن | غانا: 15ن | مدغشقر: 30ن | فرنسا: 50ن"
        )
        bot.send_message(call.message.chat.id, msg)

    elif call.data == "stars_shop":
        msg = (
            "⭐ **متجر النجوم:**\n\n"
            "🌟 نجمة: 0.015$ | 🧸 دب: 0.22$ | 🌹 وردة: 0.32$\n"
            "🎂 كيكة: 0.7$ | 💍 خاتم: 1.2$\n\n"
            f"لشراء النجوم تواصل مع: {SUPPORT_USER}"
        )
        bot.send_message(call.message.chat.id, msg)

    # باقي الأقسام (فيسبوك، انستا، تيك توك) بنفس الترتيب...
    bot.answer_callback_query(call.id)

@bot.message_handler(commands=['start'])
def start(message):
    show_main_menu(message.chat.id)

bot.polling(none_stop=True)
