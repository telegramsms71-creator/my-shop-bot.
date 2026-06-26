import telebot
from telebot import types

BOT_TOKEN = "8851361153:AAHEmdqQqfNn9kDt2xHNinQneGa1MBI-9xU"
bot = telebot.TeleBot(BOT_TOKEN)
SUPPORT = "@elegramSMS_Support23" # تم التحديث إلى 23

def main_menu(m, edit=False):
    kb = types.InlineKeyboardMarkup(row_width=2)
    kb.add(
        types.InlineKeyboardButton("📱 WhatsApp", callback_data="cat_wa"),
        types.InlineKeyboardButton("✈️ Telegram", callback_data="cat_tg"),
        types.InlineKeyboardButton("🔵 Facebook", callback_data="cat_fb"),
        types.InlineKeyboardButton("📸 Instagram", callback_data="cat_ig"),
        types.InlineKeyboardButton("🎵 TikTok", callback_data="cat_tt"),
        types.InlineKeyboardButton("⭐️ متجر النجوم", callback_data="stars"),
        types.InlineKeyboardButton("💳 طرق الدفع", callback_data="pay")
    )
    text = f"🌐 〈 𝐒𝐄𝐑𝐕𝐈𝐂𝐄 𝐌𝐄𝐍𝐔 〉\n\nChoose your service below 💎\n\n💬 Support: {SUPPORT}"
    if edit: bot.edit_message_text(text, m.chat.id, m.message_id, reply_markup=kb, parse_mode="Markdown")
    else: bot.send_message(m.chat.id, text, reply_markup=kb, parse_mode="Markdown")

@bot.callback_query_handler(func=lambda c: True)
def cb(c):
    cid, mid = c.message.chat.id, c.message.message_id
    back_btn = types.InlineKeyboardMarkup().add(types.InlineKeyboardButton("🔙 BACK", callback_data="back"))
    
    if c.data == "back": main_menu(c.message, edit=True)
    
    elif c.data == "pay":
        text = (
            "💳 **طرق الدفع المتاحة:**\n\n"
            "🔹 **Polygon (USDT):**\n`0xA7fE0a5Ae6Adcd5b47df238F836449b4d0866155`\n\n"
            "🔹 **BEP20 (USDT):**\n`0xA7fE0a5Ae6Adcd5b47df238F836449b4d0866155`\n\n"
            "🔹 **ERC20 (USDT):**\n`0x8D7dDE7719e9d6D3e5175CE170Fae00372715493`\n\n"
            "🔹 **TRC20 (USDT):**\n`TRHUB8kuMpdCoDzST6c4AJ4cJdk6Ttoz97`\n\n"
            f"⚠️ أرسل الإيصال للدعم بعد التحويل: {SUPPORT}"
        )
        bot.edit_message_text(text, cid, mid, reply_markup=back_btn, parse_mode="Markdown")

    elif c.data == "cat_wa":
        text = ("📱 **WhatsApp Pricing:**\n"
                "• France: $0.50 (50ن) | • Gabon: $0.25 (25ن)\n"
                "• Germany: $0.20 (20ن) | • Ghana: $0.15 (15ن)\n"
                "• Madagascar: $0.30 (30ن) | • Nigeria: $0.20 (20ن)\n"
                "• Sudan: $0.15 (15ن) | • Ukraine: $0.40 (40ن)\n"
                "• Venezuela: $0.25 (25ن)\n\n" + f"💬 Support: {SUPPORT}")
        bot.edit_message_text(text, cid, mid, reply_markup=back_btn)

    elif c.data == "cat_tg":
        text = ("✈️ **Telegram Pricing:**\n"
                "• Egypt: $0.50 (50ن) | • India: $0.30 (30ن)\n"
                "• Mixed: $0.28 (28ن) | • Syria: $1.10 (110ن)\n"
                "• USA: $0.25 (20ن)\n\n" + f"💬 Support: {SUPPORT}")
        bot.edit_message_text(text, cid, mid, reply_markup=back_btn)

    elif c.data == "cat_fb":
        text = ("🔵 **Facebook Pricing:**\n"
                "• Germany: $0.20 (20ن) | • Ghana: $0.25 (25ن)\n"
                "• Jordan: $0.30 (30ن) | • Madagascar: $0.20 (20ن)\n"
                "• Sudan: $0.20 (20ن)\n\n" + f"💬 Support: {SUPPORT}")
        bot.edit_message_text(text, cid, mid, reply_markup=back_btn)

    elif c.data == "cat_ig":
        text = ("📸 **Instagram Pricing:**\n"
                "• Ghana: $0.25 (25ن) | • Jordan: $0.30 (30ن)\n\n" + f"💬 Support: {SUPPORT}")
        bot.edit_message_text(text, cid, mid, reply_markup=back_btn)

    elif c.data == "cat_tt":
        text = ("🎵 **TikTok Pricing:**\n"
                "• Norway: $0.30 (0.3ن)\n\n" + f"💬 Support: {SUPPORT}")
        bot.edit_message_text(text, cid, mid, reply_markup=back_btn)

    elif c.data == "stars":
        text = ("⭐️ **متجر النجوم والهدايا:**\n\n"
                "• النجمة الواحدة = 0.015$\n"
                "🎁 **الهدايا:**\n"
                "• دب: $0.2 | • وردة: $0.29 | • كيكة: $0.55 | • خاتم: $1.1\n\n" + f"💬 Support: {SUPPORT}")
        bot.edit_message_text(text, cid, mid, reply_markup=back_btn)

@bot.message_handler(commands=['start'])
def start(m):
    main_menu(m)

bot.polling(none_stop=True)
