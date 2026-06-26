import telebot
from telebot import types

BOT_TOKEN = "8851361153:AAHfG-uIBWfHfuYD79iVK6oKRWbg-20ytH4"
bot = telebot.TeleBot(BOT_TOKEN)

SUPPORT = "@elegramSMS_Support23"

# --- دالة عرض الأرقام والأسعار (بتنسيق متباعد) ---
def show_details(call, title, content):
    text = f"💎 **{title}**:\n\n{content}\n\n⚠️ *يرجى التواصل مع الدعم لإتمام الطلب.*"
    kb = types.InlineKeyboardMarkup()
    kb.add(types.InlineKeyboardButton("📞 التواصل مع الدعم", url=f"https://t.me/{SUPPORT[1:]}"))
    kb.add(types.InlineKeyboardButton("🔙 رجوع", callback_data="back_main"))
    bot.edit_message_text(text, call.message.chat.id, call.message.message_id, reply_markup=kb, parse_mode="Markdown")

# --- قائمة طرق الدفع (بفواصل متباعدة) ---
def send_payment_methods(call):
    text = """💳 **طرق الدفع المتوفرة:**

🔹 **C-Wallet:**
`61824874`

🔹 **FaucetPay:**
`Telegramsms71@gmail.com`

🔹 **TON Network:**
`UQBEej0PxeZK8DyVwkAVQznE1FrMiEbxxJSia7MhS4H1Co7`

🔹 **USDT Polygon:**
`0xA7fE0a5Ae6Adcd5b47df238F836449b4d0866155`

🔹 **USDT BEP20:**
`0xA7fE0a5Ae6Adcd5b47df238F836449b4d0866155`

🔹 **USDT ERC20:**
`0x8D7dDE7719e9d6D3e5175CE170Fae00372715493`

🔹 **USDT TRC20:**
`TRHUB8kuMpdCoDzST6c4AJ4cJdk6Ttoz97`"""
    kb = types.InlineKeyboardMarkup(); kb.add(types.InlineKeyboardButton("🔙 رجوع", callback_data="back_main"))
    bot.edit_message_text(text, call.message.chat.id, call.message.message_id, reply_markup=kb, parse_mode="Markdown")

@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == "btn_tg":
        show_details(call, "Telegram", "• USA: 0.25$\n\n• Egypt: 0.50$\n\n• Syria: 1.10$\n\n• India: 0.30$")
    elif call.data == "btn_tinder":
        show_details(call, "Tinder", "• Indonesia: 0.20$\n\n• Mozambique: 0.30$")
    elif call.data == "btn_fb":
        show_details(call, "Facebook", "• Germany: 0.20$\n\n• Sudan: 0.20$\n\n• Jordan: 0.30$\n\n• Ghana: 0.25$")
    elif call.data == "btn_ig":
        show_details(call, "Instagram", "• Ghana: 0.25$\n\n• Jordan: 0.30$")
    elif call.data == "btn_tt":
        show_details(call, "TikTok", "• Norway: 0.30$")
    elif call.data == "btn_goog":
        show_details(call, "Google", "• Venezuela: 0.20$")
    elif call.data == "btn_apple":
        show_details(call, "Apple", "• Sudan: 0.30$\n\n• Zimbabwe: 0.25$")
    elif call.data == "btn_pay":
        send_payment_methods(call)
    elif call.data == "back_main":
        send_main_menu(call)

def send_main_menu(call):
    kb = types.InlineKeyboardMarkup(row_width=2)
    kb.add(
        types.InlineKeyboardButton("🔥 Tinder", callback_data="btn_tinder"),
        types.InlineKeyboardButton("✈️ Telegram", callback_data="btn_tg"),
        types.InlineKeyboardButton("🔵 Facebook", callback_data="btn_fb"),
        types.InlineKeyboardButton("📸 Instagram", callback_data="btn_ig"),
        types.InlineKeyboardButton("🎵 TikTok", callback_data="btn_tt"),
        types.InlineKeyboardButton("🔍 Google", callback_data="btn_goog"),
        types.InlineKeyboardButton("🍎 Apple", callback_data="btn_apple"),
        types.InlineKeyboardButton("💳 طرق الدفع", callback_data="btn_pay")
    )
    bot.edit_message_text("🌐 **القائمة الرئيسية - اختر الخدمة:**", call.message.chat.id, call.message.message_id, reply_markup=kb, parse_mode="Markdown")

@bot.message_handler(commands=['start'])
def start(m):
    kb = types.InlineKeyboardMarkup(row_width=2)
    kb.add(
        types.InlineKeyboardButton("🔥 Tinder", callback_data="btn_tinder"),
        types.InlineKeyboardButton("✈️ Telegram", callback_data="btn_tg"),
        types.InlineKeyboardButton("🔵 Facebook", callback_data="btn_fb"),
        types.InlineKeyboardButton("📸 Instagram", callback_data="btn_ig"),
        types.InlineKeyboardButton("🎵 TikTok", callback_data="btn_tt"),
        types.InlineKeyboardButton("🔍 Google", callback_data="btn_goog"),
        types.InlineKeyboardButton("🍎 Apple", callback_data="btn_apple"),
        types.InlineKeyboardButton("💳 طرق الدفع", callback_data="btn_pay")
    )
    bot.send_message(m.chat.id, "مرحباً بك! اختر الخدمة:", reply_markup=kb)

bot.polling(none_stop=True)
