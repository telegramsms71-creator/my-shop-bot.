import telebot
from telebot import types

BOT_TOKEN = "8851361153:AAHEmdqQqfNn9kDt2xHNinQneGa1MBI-9xU"
bot = telebot.TeleBot(BOT_TOKEN)
SUPPORT = "@elegramSMS_Support20"
CHANNELS = ["@freemoney20262", "@sms202622", "@sms20262"]

# ... [دوال الاشتراك والـ start كما هي] ...

@bot.callback_query_handler(func=lambda c: True)
def cb(c):
    cid, mid = c.message.chat.id, c.message.message_id
    back_kb = types.InlineKeyboardMarkup()
    back_kb.add(types.InlineKeyboardButton("🔙 BACK", callback_data="back"))
    back_kb.add(types.InlineKeyboardButton("📞 تواصل مع الدعم", url=f"https://t.me/{SUPPORT[1:]}"))
    
    if c.data == "back": main_menu(c.message, edit=True)
    
    # --- قسم الأرقام (كل دولة في سطر مستقل) ---
    elif c.data == "cat_wa":
        text = ("📱 **WhatsApp Services:**\n\n"
                "• France: $0.50 (50ن)\n\n"
                "• Gabon: $0.25 (25ن)\n\n"
                "• Germany: $0.20 (20ن)\n\n"
                "• Ghana: $0.15 (15ن)\n\n"
                "• Madagascar: $0.30 (30ن)\n\n"
                "• Nigeria: $0.20 (20ن)\n\n"
                "• Sudan: $0.15 (15ن)\n\n"
                "• Ukraine: $0.40 (40ن)\n\n"
                "• Venezuela: $0.25 (25ن)")
        bot.edit_message_text(text, cid, mid, reply_markup=back_kb)

    elif c.data == "cat_tg":
        text = ("✈️ **Telegram Services:**\n\n"
                "• USA: $0.25 (20ن)\n\n"
                "• Egypt: $0.50 (50ن)\n\n"
                "• Syria: $1.10 (110ن)\n\n"
                "• India: $0.30 (30ن)\n\n"
                "• Mixed: $0.28 (28ن)")
        bot.edit_message_text(text, cid, mid, reply_markup=back_kb)

    elif c.data == "cat_fb":
        text = ("🔵 **Facebook Services:**\n\n"
                "• Germany: $0.20 (20ن)\n\n"
                "• Madagascar: $0.20 (20ن)\n\n"
                "• Sudan: $0.20 (20ن)\n\n"
                "• Jordan: $0.30 (30ن)\n\n"
                "• Ghana: $0.25 (25ن)")
        bot.edit_message_text(text, cid, mid, reply_markup=back_kb)

    elif c.data == "cat_ig":
        text = ("📸 **Instagram Services:**\n\n"
                "• Ghana: $0.25 (25ن)\n\n"
                "• Jordan: $0.30 (30ن)")
        bot.edit_message_text(text, cid, mid, reply_markup=back_kb)

    elif c.data == "cat_tt":
        text = ("🎵 **TikTok Services:**\n\n"
                "• Norway: $0.30 (0.3ن)")
        bot.edit_message_text(text, cid, mid, reply_markup=back_kb)

    elif c.data == "cat_goog":
        text = ("🔍 **Google Services:**\n\n"
                "• Venezuela: $0.20 (20ن)")
        bot.edit_message_text(text, cid, mid, reply_markup=back_kb)
    
    # --- قسم الدفع (متباعد) ---
    elif c.data == "pay":
        text = ("💳 **طرق الدفع (USDT):**\n\n"
                "🔹 **Polygon:**\n`0xA7fE0a5Ae6Adcd5b47df238F836449b4d0866155`\n\n"
                "🔹 **BEP20:**\n`0xA7fE0a5Ae6Adcd5b47df238F836449b4d0866155`\n\n"
                "🔹 **ERC20:**\n`0x8D7dDE7719e9d6D3e5175CE170Fae00372715493`\n\n"
                "🔹 **TRC20:**\n`TRHUB8kuMpdCoDzST6c4AJ4cJdk6Ttoz97`")
        bot.edit_message_text(text, cid, mid, reply_markup=back_kb, parse_mode="Markdown")

    elif c.data == "stars":
        text = ("⭐️ **متجر النجوم:**\n\n"
                "• النجمة الواحدة = 0.015$\n\n"
                "🎁 **الهدايا:**\n\n"
                "• دب: $0.2\n\n"
                "• وردة: $0.29\n\n"
                "• كيكة: $0.55\n\n"
                "• خاتم: $1.1")
        bot.edit_message_text(text, cid, mid, reply_markup=back_kb)

bot.polling(none_stop=True)
