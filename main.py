import telebot
from telebot import types

BOT_TOKEN = "8851361153:AAHEmdqQqfNn9kDt2xHNinQneGa1MBI-9xU"
bot = telebot.TeleBot(BOT_TOKEN)
SUPPORT = "@elegramSMS_Support20"
CHANNELS = ["@freemoney20262", "@sms202622", "@sms20262"]

def check_sub(uid):
    for ch in CHANNELS:
        try:
            if bot.get_chat_member(ch, uid).status in ['left', 'kicked']: return False
        except: return False
    return True

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
    text = "🌐 〈 𝐒𝐄𝐑𝐕𝐈𝐂𝐄 𝐌𝐄𝐍𝐔 〉\n\nChoose your service below 💎"
    if edit: bot.edit_message_text(text, m.chat.id, m.message_id, reply_markup=kb, parse_mode="Markdown")
    else: bot.send_message(m.chat.id, text, reply_markup=kb, parse_mode="Markdown")

@bot.callback_query_handler(func=lambda c: True)
def cb(c):
    cid, mid = c.message.chat.id, c.message.message_id
    back_btn = types.InlineKeyboardMarkup().add(types.InlineKeyboardButton("🔙 BACK", callback_data="back"))
    
    if c.data == "back": main_menu(c.message, edit=True)
    elif c.data == "check":
        if check_sub(cid): main_menu(c.message)
        else: bot.answer_callback_query(c.id, "❌ Join channels first!", show_alert=True)
    
    elif c.data == "cat_wa":
        text = ("📱 **WhatsApp Pricing:**\n• Nigeria: 20ن ($0.30)\n• Sudan: 15ن ($0.22)\n"
                "• Venezuela: 25ن ($0.37)\n• Germany: 20ن ($0.30)")
        bot.edit_message_text(text, cid, mid, reply_markup=back_btn)
        
    elif c.data == "cat_tg":
        text = ("✈️ **Telegram Pricing:**\n• USA: 20ن ($0.30)\n• Egypt: 50ن ($0.75)\n"
                "• Syria: 110ن ($1.65)")
        bot.edit_message_text(text, cid, mid, reply_markup=back_btn)
        
    elif c.data == "cat_fb":
        text = ("🔵 **Facebook Pricing:**\n• Germany: 20ن ($0.30)\n• Jordan: 30ن ($0.45)")
        bot.edit_message_text(text, cid, mid, reply_markup=back_btn)
        
    elif c.data == "cat_ig":
        text = ("📸 **Instagram Pricing:**\n• Ghana: 25ن ($0.37)\n• Jordan: 30ن ($0.45)")
        bot.edit_message_text(text, cid, mid, reply_markup=back_btn)
        
    elif c.data == "cat_tt":
        text = "🎵 **TikTok Pricing:**\n• Norway: 0.3ن ($0.0045)"
        bot.edit_message_text(text, cid, mid, reply_markup=back_btn)

    elif c.data == "stars":
        text = ("⭐️ **متجر النجوم والهدايا:**\n\n"
                "• النجمة الواحدة = 0.015$\n\n"
                "🎁 **أسعار الهدايا:**\n"
                "• دب: 0.2$ | • وردة: 0.29$\n"
                "• كيكة: 0.55$ | • خاتم: 1.1$")
        bot.edit_message_text(text, cid, mid, reply_markup=back_btn, parse_mode="Markdown")

    elif c.data == "pay":
        text = ("💳 **Payment Methods (USDT):**\n\n"
                "• Polygon: `0xA7fE0a5Ae6Adcd5b47df238F836449b4d0866155`\n"
                "• BEP20: `0xA7fE0a5Ae6Adcd5b47df238F836449b4d0866155`\n"
                "• ERC20: `0x8D7dDE7719e9d6D3e5175CE170Fae00372715493`\n"
                "• TRC20: `TRHUB8kuMpdCoDzST6c4AJ4cJdk6Ttoz97`")
        bot.edit_message_text(text, cid, mid, reply_markup=back_btn, parse_mode="Markdown")

@bot.message_handler(commands=['start'])
def start(m):
    main_menu(m)

bot.polling(none_stop=True)
