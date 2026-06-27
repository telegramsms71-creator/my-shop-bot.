import telebot

TOKEN = '8851361153:AAH5CsfaUnYlGxByN7YUKSOByNuomynKWlc'
bot = telebot.TeleBot(TOKEN)
SUPPORT_USER = "@Sultan_Support27"
ADMIN_ID = 8767607098 

# --- حفظ المستخدمين للإشعارات ---
def save_user(user_id):
    users = get_users()
    if str(user_id) not in users:
        with open("users.txt", "a") as f:
            f.write(str(user_id) + "\n")

def get_users():
    try:
        with open("users.txt", "r") as f:
            return set(line.strip() for line in f)
    except: return set()

# --- القوائم ---
def main_menu():
    markup = telebot.types.InlineKeyboardMarkup(row_width=1)
    markup.add(
        telebot.types.InlineKeyboardButton("♡ شراء أرقام وهمية ♡", callback_data="numbers_type"),
        telebot.types.InlineKeyboardButton("♡ خدمات الرشق والمتابعين ♡", callback_data="rashq_menu"),
        telebot.types.InlineKeyboardButton("♡ اشحن حسابك (طرق الدفع) ♡", callback_data="charge"),
        telebot.types.InlineKeyboardButton("♡ الدعم الفني ♡", callback_data="support")
    )
    return markup

def select_number_type():
    markup = telebot.types.InlineKeyboardMarkup(row_width=1)
    markup.add(
        telebot.types.InlineKeyboardButton("📱 تليجرام", callback_data="numbers_telegram"),
        telebot.types.InlineKeyboardButton("💬 واتساب", callback_data="numbers_whatsapp"),
        telebot.types.InlineKeyboardButton("✖️ رجوع", callback_data="main_menu")
    )
    return markup

def telegram_numbers_menu():
    markup = telebot.types.InlineKeyboardMarkup(row_width=2)
    countries = [
        ("Uzbekistan | 33.1 P", "tg_uzb"), ("Bangladesh | 15.6 P", "tg_ban"),
        ("Saudi Arabia | 56.5 P", "tg_sau"), ("Italy | 47.5 P", "tg_ita"),
        ("Mexico | 28.6 P", "tg_mex"), ("Kazakhstan | 42.9 P", "tg_kaz"),
        ("Yemen | 26.0 P", "tg_yem"), ("Latvia | 66.3 P", "tg_lat"),
        ("Portugal | 85.1 P", "tg_por"), ("Kyrgyzstan | 56.5 P", "tg_kyr"),
        ("Tajikistan | 33.1 P", "tg_taj"), ("United States | 16.9 P", "tg_usa"),
        ("Egypt | 21.4 P", "tg_egy"), ("Iraq | 85.1 P", "tg_irq"),
        ("Turkey | 47.5 P", "tg_tur"), ("Venezuela | 47.5 P", "tg_ven"),
        ("Colombia | 15.6 P", "tg_col"), ("Zimbabwe | 16.9 P", "tg_zim")
    ]
    for name, cb in countries: markup.add(telebot.types.InlineKeyboardButton(name, callback_data=f"buy_{cb}"))
    markup.add(telebot.types.InlineKeyboardButton("✖️ رجوع", callback_data="numbers_type"))
    return markup

def whatsapp_numbers_menu():
    markup = telebot.types.InlineKeyboardMarkup(row_width=2)
    countries = [
        ("فيتنام | 13.0 P", "wa_v"), ("الفلبين | 13.0 P", "wa_ph"),
        ("تايلاند | 13.0 P", "wa_t"), ("إندونيسيا | 13.0 P", "wa_in"),
        ("مصر | 13.0 P", "wa_e"), ("كندا | 13.0 P", "wa_ca"),
        ("المغرب | 16.9 P", "wa_ma"), ("جنوب إفريقيا | 16.9 P", "wa_sa"),
        ("ليبيا | 13.0 P", "wa_l"), ("بورتوريكو | 13.0 P", "wa_pr"),
        ("اليمن | 16.9 P", "wa_ye"), ("فرنسا | 13.0 P", "wa_fr"),
        ("الجزائر | 13.0 P", "wa_dz"), ("سوريا | 13.0 P", "wa_sy"),
        ("البرازيل | 10.4 P", "wa_br"), ("أنغولا | 13.0 P", "wa_an"),
        ("أستراليا | 13.0 P", "wa_au"), ("المكسيك | 13.0 P", "wa_mx"),
        ("السعودية | 23.4 P", "wa_sau"), ("اليمن (2) | 16.9 P", "wa_ye2"),
        ("بريطانيا | 13.0 P", "wa_uk"), ("تركيا | 13.0 P", "wa_tr"),
        ("العراق | 13.0 P", "wa_iq"), ("بنغلاديش | 13.0 P", "wa_bd")
    ]
    for name, cb in countries: markup.add(telebot.types.InlineKeyboardButton(name, callback_data=f"buy_{cb}"))
    markup.add(telebot.types.InlineKeyboardButton("✖️ رجوع", callback_data="numbers_type"))
    return markup

def rashq_menu():
    markup = telebot.types.InlineKeyboardMarkup(row_width=1)
    markup.add(
        telebot.types.InlineKeyboardButton("📢 رشق تليجرام", callback_data="contact_tg_rashq"),
        telebot.types.InlineKeyboardButton("📸 رشق إنستجرام", callback_data="contact_insta_rashq"),
        telebot.types.InlineKeyboardButton("🎵 رشق تيك توك", callback_data="contact_tiktok_rashq"),
        telebot.types.InlineKeyboardButton("📺 رشق يوتيوب", callback_data="contact_yt_rashq"),
        telebot.types.InlineKeyboardButton("✖️ رجوع", callback_data="main_menu")
    )
    return markup

def payment_menu():
    markup = telebot.types.InlineKeyboardMarkup(row_width=1)
    payments = [
        ("💎 Cwallet | 61824874", "cwallet"), ("📧 FaucetPay | TelegramSMS", "faucetpay"),
        ("⛓️ Tron (TRC20)", "trc20"), ("🌐 USDT (ERC20)", "erc20"),
        ("🌐 USDT (BEP20)", "bep20"), ("🌐 USDT (Polygon)", "polygon")
    ]
    for name, cb in payments: markup.add(telebot.types.InlineKeyboardButton(name, callback_data=f"contact_{cb}"))
    markup.add(telebot.types.InlineKeyboardButton("✖️ رجوع", callback_data="main_menu"))
    return markup

# --- المعالج ---
@bot.message_handler(commands=['start'])
def start(message):
    save_user(message.chat.id)
    bot.send_message(message.chat.id, "👋 أهلاً بك في بوت السلطان", reply_markup=main_menu())

@bot.message_handler(commands=['notify'])
def notify_users(message):
    if message.from_user.id == ADMIN_ID:
        text = message.text.replace("/notify ", "")
        for user_id in get_users():
            try: bot.send_message(user_id, f"🔔 إشعار من السلطان:\n\n{text}")
            except: pass
        bot.reply_to(message, "تم إرسال الإشعار.")

@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == "main_menu": bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="القائمة الرئيسية:", reply_markup=main_menu())
    elif call.data == "numbers_type": bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="اختر نوع الخدمة:", reply_markup=select_number_type())
    elif call.data == "numbers_telegram": bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="اختر الدولة (تليجرام):", reply_markup=telegram_numbers_menu())
    elif call.data == "numbers_whatsapp": bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="اختر الدولة (واتساب):", reply_markup=whatsapp_numbers_menu())
    elif call.data == "rashq_menu": bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="قسم الرشق:", reply_markup=rashq_menu())
    elif call.data == "charge": bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="طرق الدفع:", reply_markup=payment_menu())
    elif call.data.startswith(("buy_", "contact_")): bot.send_message(call.message.chat.id, f"✅ تواصل مع الدعم لإتمام الطلب:\n{SUPPORT_USER}")

bot.polling(none_stop=True)
