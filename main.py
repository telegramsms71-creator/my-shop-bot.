import telebot
from telebot import types

BOT_TOKEN = "8851361153:AAHEmdqQqfNn9kDt2xHNinQneGa1MBI-9xU"
bot = telebot.TeleBot(BOT_TOKEN)
SUPPORT_USER = "@elegramSMS_Support23"

# القنوات المطلوبة للاشتراك الإجباري
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

# القائمة الرئيسية (SERVICE MENU)
def main_menu(chat_id, message_id=None):
    markup = types.InlineKeyboardMarkup(row_width=1)
    markup.add(
        types.InlineKeyboardButton("📱 WhatsApp", callback_data="cat_wa"),
        types.InlineKeyboardButton("✈️ Telegram", callback_data="cat_tg"),
        types.InlineKeyboardButton("🔵 Facebook", callback_data="cat_fb"),
        types.InlineKeyboardButton("📸 Instagram", callback_data="cat_ig"),
        types.InlineKeyboardButton("🎵 TikTok", callback_data="cat_tt"),
        types.InlineKeyboardButton("💳 طرق الدفع", callback_data="payment")
    )
    text = "─── 〈 🌐 SERVICE MENU 〉 ───\n\nSelect a service or country 💎"
    if message_id: bot.edit_message_text(text, chat_id, message_id, reply_markup=markup, parse_mode="Markdown")
    else: bot.send_message(chat_id, text, reply_markup=markup, parse_mode="Markdown")

@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    chat_id = call.message.chat.id
    msg_id = call.message.message_id
    
    if call.data == "check_sub":
        if is_subscribed(chat_id): main_menu(chat_id, msg_id)
        else: bot.answer_callback_query(call.id, "اشترك في القنوات أولاً!", show_alert=True)
        
    elif call.data == "back_main": main_menu(chat_id, msg_id)
    
    # أقسام الخدمات
    elif call.data == "cat_wa":
        markup = types.InlineKeyboardMarkup(row_width=2)
        markup.add(types.InlineKeyboardButton("🇳🇬 نيجيريا", callback_data="buy_done"), types.InlineKeyboardButton("🇩🇪 ألمانيا", callback_data="buy_done"), 
                   types.InlineKeyboardButton("🇸🇩 السودان", callback_data="buy_done"), types.InlineKeyboardButton("🔙 رجوع", callback_data="back_main"))
        bot.edit_message_text("📱 **WhatsApp Services:**", chat_id, msg_id, reply_markup=markup)
        
    elif call.data == "cat_tg":
        markup = types.InlineKeyboardMarkup(row_width=2)
        markup.add(types.InlineKeyboardButton("🇺🇸 أمريكا", callback_data="buy_done"), types.InlineKeyboardButton("🇪🇬 مصر", callback_data="buy_done"), 
                   types.InlineKeyboardButton("🇸🇾 سوريا", callback_data="buy_done"), types.InlineKeyboardButton("🔙 رجوع", callback_data="back_main"))
        bot.edit_message_text("✈️ **Telegram Services:**", chat_id, msg_id, reply_markup=markup)

    elif call.data == "cat_fb":
        markup = types.InlineKeyboardMarkup(row_width=2)
        markup.add(types.InlineKeyboardButton("🇩🇪 ألمانيا", callback_data="buy_done"), types.InlineKeyboardButton("🇯🇴 الأردن", callback_data="buy_done"), 
                   types.InlineKeyboardButton("🔙 رجوع", callback_data="back_main"))
        bot.edit_message_text("🔵 **Facebook Services:**", chat_id, msg_id, reply_markup=markup)
        
    elif call.data == "cat_ig":
        markup = types.InlineKeyboardMarkup(row_width=2)
        markup.add(types.InlineKeyboardButton("🇬🇭 غانا", callback_data="buy_done"), types.InlineKeyboardButton("🇯🇴 الأردن", callback_data="buy_done"), 
                   types.InlineKeyboardButton("🔙 رجوع", callback_data="back_main"))
        bot.edit_message_text("📸 **Instagram Services:**", chat_id, msg_id, reply_markup=markup)
        
    elif call.data == "cat_tt":
        markup = types.InlineKeyboardMarkup(row_width=1)
        markup.add(types.InlineKeyboardButton("🇳🇴 النرويج", callback_data="buy_done"), types.InlineKeyboardButton("🔙 رجوع", callback_data="back_main"))
        bot.edit_message_text("🎵 **TikTok Services:**", chat_id, msg_id, reply_markup=markup)

    elif call.data == "payment":
        text = ("💳 **Payment Methods:**\n\n"
                "💎 TON: `UQBEej0PxeZK8DyVwkAVQznE1FrMi0EbxxJSia7MhS4H1Co7`\n"
                "🔹 Polygon/BEP20: `0xA7fE0a5Ae6Adcd5b47df238F836449b4d0866155`\n"
                "🔹 ERC20: `0x8D7dDE7719e9d6D3e5175CE170Fae00372715493`\n"
                "🔹 TRC20: `TRHUB8kuMpdCoDzST6c4AJ4cJdk6Ttoz97`\n"
                "🔹 Cwallet ID: `61824874`\n"
                "📧 FaucetPay: `telegramsms71@gmail.com`")
        bot.edit_message_text(text, chat_id, msg_id, parse_mode="Markdown", reply_markup=types.InlineKeyboardMarkup().add(types.InlineKeyboardButton("🔙 رجوع", callback_data="back_main")))
        
    elif call.data == "buy_done":
        bot.answer_callback_query(call.id, "أرسل كود الخدمة للدعم!")
        bot.send_message(chat_id, f"✅ تواصل مع الدعم لإتمام طلبك:\n{SUPPORT_USER}")

@bot.message_handler(commands=['start'])
def start(message):
    if not is_subscribed(message.chat.id):
        bot.send_message(message.chat.id, "⚠️ **يجب الاشتراك في القنوات أولاً:**", reply_markup=force_sub_markup())
    else: main_menu(message.chat.id)

bot.polling(none_stop=True)
