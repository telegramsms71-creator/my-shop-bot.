Import telebot
from telebot import types

# التوكن المحدث
BOT_TOKEN = "8851361153:AAHfG-uIBWfHfuYD79iVK6oKRWbg-20ytH4"
bot = telebot.TeleBot(BOT_TOKEN)

# تم تحديث اليوزر هنا
SUPPORT = "@elegramSMS_Support27" 
CHANNELS = ["@freemoney20262", "@sms202622", "@sms20262"]

# دالة التحقق من الاشتراك
def check_sub(uid):
    for ch in CHANNELS:
        try:
            status = bot.get_chat_member(ch, uid).status
            if status in ['left', 'kicked']: return False
        except: return False
    return True

# القائمة الرئيسية
def main_menu(m, edit=False):
    kb = types.InlineKeyboardMarkup(row_width=2)
    kb.add(
        types.InlineKeyboardButton("📱 WhatsApp", callback_data="cat_wa"),
        types.InlineKeyboardButton("✈️ Telegram", callback_data="cat_tg"),
        types.InlineKeyboardButton("🔵 Facebook", callback_data="cat_fb"),
        types.InlineKeyboardButton("📸 Instagram", callback_data="cat_ig"),
        types.InlineKeyboardButton("🎵 TikTok", callback_data="cat_tt"),
        types.InlineKeyboardButton("🔍 Google", callback_data="cat_goog"),
        types.InlineKeyboardButton("⭐️ متجر النجوم", callback_data="stars"),
        types.InlineKeyboardButton("💳 طرق الدفع", callback_data="pay"),
        types.InlineKeyboardButton("📞 الدعم الفني", url=f"https://t.me/{SUPPORT[1:]}")
    )
    text = "🌐 〈 𝐒𝐄𝐑𝐕𝐈𝐂𝐄 𝐌𝐄𝐍𝐔 〉\n\nChoose your service below 💎"
    if edit: bot.edit_message_text(text, m.chat.id, m.message_id, reply_markup=kb, parse_mode="Markdown")
    else: bot.send_message(m.chat.id, text, reply_markup=kb, parse_mode="Markdown")

@bot.message_handler(commands=['start'])
def start(m):
    if not check_sub(m.chat.id):
        kb = types.InlineKeyboardMarkup()
        for ch in CHANNELS: kb.add(types.InlineKeyboardButton(f"JOIN {ch}", url=f"https://t.me/{ch[1:]}"))
        kb.add(types.InlineKeyboardButton("✅ تحقق من الاشتراك", callback_data="check"))
        bot.send_message(m.chat.id, "⚠️ **يجب الاشتراك في القنوات أولاً لتشغيل البوت:**", reply_markup=kb, parse_mode="Markdown")
    else: main_menu(m)

@bot.callback_query_handler(func=lambda c: True)
def cb(c):
    cid, mid = c.message.chat.id, c.message.message_id
    back_kb = types.InlineKeyboardMarkup()
    back_kb.add(types.InlineKeyboardButton("🔙 BACK", callback_data="back"))
    back_kb.add(types.InlineKeyboardButton("📞 تواصل مع الدعم", url=f"https://t.me/{SUPPORT[1:]}"))
    
    if c.data == "back": main_menu(c.message, edit=True)
    elif c.data == "check":
        if check_sub(cid): main_menu(c.message)
        else: bot.answer_callback_query(c.id, "❌ لم تشترك بعد في القنوات!", show_alert=True)
    
    # --- الخدمات ---
    elif c.data == "cat_wa":
        bot.edit_message_text("📱 **WhatsApp Services:**\n\n• France: $0.50 (50ن)\n\n• Gabon: $0.25 (25ن)\n\n• Germany: $0.20 (20ن)\n\n• Ghana: $0.15 (15ن)\n\n• Madagascar: $0.30 (30ن)\n\n• Nigeria: $0.20 (20ن)\n\n• Sudan: $0.15 (15ن)\n\n• Ukraine: $0.40 (40ن)\n\n• Venezuela: $0.25 (25ن)", cid, mid, reply_markup=back_kb)
    elif c.data == "cat_tg":
        bot.edit_message_text("✈️ **Telegram Services:**\n\n• USA: $0.25 (20ن)\n\n• Egypt: $0.50 (50ن)\n\n• Syria: $1.10 (110ن)\n\n• India: $0.30 (30ن)\n\n• Mixed: $0.28 (28ن)", cid, mid, reply_markup=back_kb)
    elif c.data == "cat_fb":
        bot.edit_message_text("🔵 **Facebook Services:**\n\n• Germany: $0.20 (20ن)\n\n• Madagascar: $0.20 (20ن)\n\n• Sudan: $0.20 (20ن)\n\n• Jordan: $0.30 (30ن)\n\n• Ghana: $0.25 (25ن)", cid, mid, reply_markup=back_kb)
    elif c.data == "cat_ig":
        bot.edit_message_text("📸 **Instagram Services:**\n\n• Ghana: $0.25 (25ن)\n\n• Jordan: $0.30 (30ن)", cid, mid, reply_markup=back_kb)
    elif c.data == "cat_tt":
        bot.edit_message_text("🎵 **TikTok Services:**\n\n• Norway: $0.30 (0.3ن)", cid, mid, reply_markup=back_kb)
    elif c.data == "cat_goog":
        bot.edit_message_text("🔍 **Google Services:**\n\n• Venezuela: $0.20 (20ن)", cid, mid, reply_markup=back_kb)
    
    # --- الدفع والنجوم ---
    elif c.data == "pay":
        bot.edit_message_text("💳 **طرق الدفع (USDT):**\n\n🔹 **Polygon:**\n`0xA7fE0a5Ae6Adcd5b47df238F836449b4d0866155`\n\n🔹 **BEP20:**\n`0xA7fE0a5Ae6Adcd5b47df238F836449b4d0866155`\n\n🔹 **ERC20:**\n`0x8D7dDE7719e9d6D3e5175CE170Fae00372715493`\n\n🔹 **TRC20:**\n`TRHUB8kuMpdCoDzST6c4AJ4cJdk6Ttoz97`", cid, mid, reply_markup=back_kb, parse_mode="Markdown")
    elif c.data == "stars":
        bot.edit_message_text("⭐️ **متجر النجوم:**\n\n• النجمة الواحدة = 0.015$\n\n🎁 **الهدايا:**\n\n• دب: $0.2\n\n• وردة: $0.29\n\n• كيكة: $0.55\n\n• خاتم: $1.1", cid, mid, reply_markup=back_kb)

bot.polling(none_stop=True)
