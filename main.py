import telebot
from telebot import types

BOT_TOKEN = "8851361153:AAHEmdqQqfNn9kDt2xHNinQneGa1MBI-9xU"
bot = telebot.TeleBot(BOT_TOKEN)
SUPPORT_USER = "@elegramSMS_Support23"

# --- القنوات ---
CHANNELS_LIST = ["@freemoney20262", "@sms202622", "@sms20262"]

def is_subscribed(user_id):
    for ch in CHANNELS_LIST:
        try:
            member = bot.get_chat_member(ch, user_id)
            if member.status in ['left', 'kicked']: return False
        except: return False
    return True

def force_sub_markup():
    markup = types.InlineKeyboardMarkup()
    for ch in CHANNELS_LIST:
        markup.add(types.InlineKeyboardButton(f"اشترك في {ch} 📢", url=f"https://t.me/{ch.replace('@', '')}"))
    markup.add(types.InlineKeyboardButton("تحققت من الاشتراك ✅", callback_data="check_sub"))
    return markup

# --- القائمة الرئيسية ---
def main_menu(chat_id, message_id=None):
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(
        types.InlineKeyboardButton("✈️ تليجرام", callback_data="cat_tg"),
        types.InlineKeyboardButton("📱 واتساب", callback_data="cat_wa"),
        types.InlineKeyboardButton("🔵 فيسبوك", callback_data="cat_fb"),
        types.InlineKeyboardButton("📸 انستغرام", callback_data="cat_ig"),
        types.InlineKeyboardButton("🎵 تيك توك", callback_data="cat_tt"),
        types.InlineKeyboardButton("💳 طرق الدفع", callback_data="payment"),
        types.InlineKeyboardButton("📞 التواصل مع الدعم", url=f"https://t.me/{SUPPORT_USER.replace('@', '')}")
    )
    text = "🌐 **أهلاً بك في متجر TELEGRAM SMS**\nاختر الخدمة المطلوبة:"
    if message_id: bot.edit_message_text(text, chat_id, message_id, reply_markup=markup, parse_mode="Markdown")
    else: bot.send_message(chat_id, text, reply_markup=markup, parse_mode="Markdown")

@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    chat_id = call.message.chat.id
    if call.data == "check_sub":
        if is_subscribed(chat_id):
            bot.answer_callback_query(call.id, "تم التحقق!")
            main_menu(chat_id, call.message.message_id)
        else: bot.answer_callback_query(call.id, "لم تشترك في جميع القنوات!", show_alert=True)
    elif call.data == "back_main": main_menu(chat_id, call.message.message_id)
    
    # --- الأقسام الكاملة ---
    elif call.data == "cat_tg":
        text = "✈️ **تليجرام:** أمريكا 20ن | مصر 50ن | سوريا 110ن"
        bot.edit_message_text(text, chat_id, call.message.message_id, reply_markup=types.InlineKeyboardMarkup().add(types.InlineKeyboardButton("🔙 رجوع", callback_data="back_main")))
    elif call.data == "cat_wa":
        text = "📱 **واتساب:** نيجيريا 20ن | ألمانيا 20ن | السودان 15ن | فنزويلا 25ن | أوكرانيا 40ن"
        bot.edit_message_text(text, chat_id, call.message.message_id, reply_markup=types.InlineKeyboardMarkup().add(types.InlineKeyboardButton("🔙 رجوع", callback_data="back_main")))
    elif call.data == "cat_fb":
        text = "🔵 **فيسبوك:** ألمانيا 20ن | الأردن 30ن"
        bot.edit_message_text(text, chat_id, call.message.message_id, reply_markup=types.InlineKeyboardMarkup().add(types.InlineKeyboardButton("🔙 رجوع", callback_data="back_main")))
    elif call.data == "cat_ig":
        text = "📸 **انستغرام:** غانا 25ن | الأردن 30ن"
        bot.edit_message_text(text, chat_id, call.message.message_id, reply_markup=types.InlineKeyboardMarkup().add(types.InlineKeyboardButton("🔙 رجوع", callback_data="back_main")))
    elif call.data == "cat_tt":
        text = "🎵 **تيك توك:** النرويج 0.3 نجمة"
        bot.edit_message_text(text, chat_id, call.message.message_id, reply_markup=types.InlineKeyboardMarkup().add(types.InlineKeyboardButton("🔙 رجوع", callback_data="back_main")))
    
    elif call.data == "payment":
        text = (
            "💰 **طرق الدفع:**\n"
            "💎 TON: `UQBEej0PxeZK8DyVwkAVQznE1FrMi0EbxxJSia7MhS4H1Co7`\n"
            "🔹 USDT (Polygon/BEP20): `0xA7fE0a5Ae6Adcd5b47df238F836449b4d0866155`\n"
            "🔹 USDT (ERC20): `0x8D7dDE7719e9d6D3e5175CE170Fae00372715493`\n"
            "🔹 USDT (TRC20): `TRHUB8kuMpdCoDzST6c4AJ4cJdk6Ttoz97`\n"
            "🔹 Cwallet: `61824874`\n"
            "📧 FaucetPay: `telegramsms71@gmail.com`"
        )
        bot.edit_message_text(text, chat_id, call.message.message_id, parse_mode="Markdown", reply_markup=types.InlineKeyboardMarkup().add(types.InlineKeyboardButton("🔙 رجوع", callback_data="back_main")))

@bot.message_handler(commands=['start'])
def start(message):
    if not is_subscribed(message.chat.id):
        bot.send_message(message.chat.id, "⚠️ **اشترك في قنواتنا أولاً:**", reply_markup=force_sub_markup())
    else: main_menu(message.chat.id)

bot.polling(none_stop=True)
