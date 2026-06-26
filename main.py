import telebot
from telebot import types

BOT_TOKEN = "8851361153:AAHfG-uIBWfHfuYD79iVK6oKRWbg-20ytH4"
bot = telebot.TeleBot(BOT_TOKEN)

SUPPORT = "@elegramSMS_Support27"

# --- دالة عرض الأرقام والأسعار ---
def show_details(call, title, content):
    text = f"💎 **{title}**:\n\n{content}\n\n⚠️ *يرجى التواصل مع الدعم لإتمام الطلب.*"
    kb = types.InlineKeyboardMarkup()
    kb.add(types.InlineKeyboardButton("📞 التواصل مع الدعم", url=f"https://t.me/{SUPPORT[1:]}"))
    kb.add(types.InlineKeyboardButton("🔙 رجوع", callback_data="back_main"))
    bot.edit_message_text(text, call.message.chat.id, call.message.message_id, reply_markup=kb, parse_mode="Markdown")

# --- دالة عرض متجر النجوم ---
def show_stars(call):
    text = "⭐️ **متجر النجوم:**\n\n• النجمة الواحدة: `0.015$`\n\n• دب: `0.2$`\n\n• وردة: `0.29$`\n\n• كيكة: `0.55$`\n\n• خاتم: `1.1$`"
    kb = types.InlineKeyboardMarkup()
    kb.add(types.InlineKeyboardButton("📞 التواصل مع الدعم", url=f"https://t.me/{SUPPORT[1:]}"))
    kb.add(types.InlineKeyboardButton("🔙 رجوع", callback_data="back_main"))
    bot.edit_message_text(text, call.message.chat.id, call.message.message_id, reply_markup=kb, parse_mode="Markdown")

# --- دالة عرض طرق الدفع ---
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
        show_details(call, "Telegram", "• USA: 0.25$\n\n• Egypt: 0.50$\n\n• Syria: 1.10$")
    elif call.data == "btn_tinder":
        show_details(call, "Tinder", "• Indonesia: 0.20$\n\n• Mozambique: 0.30$")
    elif call.data == "btn_stars":
        show_stars(call)
    elif call.data == "btn_pay":
        send_payment_methods(call)
    elif call.data == "back_main":
        send_main_menu(call.message)

def send_main_menu(m):
    kb = types.InlineKeyboardMarkup(row_width=2)
    kb.add(
        types.InlineKeyboardButton("🔥 Tinder", callback_data="btn_tinder"),
        types.InlineKeyboardButton("✈️ Telegram", callback_data="btn_tg"),
        types.InlineKeyboardButton("⭐️ متجر النجوم", callback_data="btn_stars"),
        types.InlineKeyboardButton("💳 طرق الدفع", callback_data="btn_pay"),
        types.InlineKeyboardButton("📞 الدعم الفني", url=f"https://t.me/{SUPPORT[1:]}")
    )
    # تعديل: نستخدم edit إذا كانت رسالة موجودة، أو send إذا كانت جديدة
    if hasattr(m, 'message_id'):
        bot.edit_message_text("🌐 **القائمة الرئيسية - اختر الخدمة:**", m.chat.id, m.message_id, reply_markup=kb, parse_mode="Markdown")
    else:
        bot.send_message(m.chat.id, "🌐 **القائمة الرئيسية - اختر الخدمة:**", reply_markup=kb, parse_mode="Markdown")

@bot.message_handler(commands=['start'])
def start(m):
    send_main_menu(m)

bot.polling(none_stop=True)
