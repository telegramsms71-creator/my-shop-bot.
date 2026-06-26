import telebot
import time

# التوكن الخاص بك
BOT_TOKEN = "8851361153:AAE_adap5TIOw1mmG8RHZWsn1Bk80SyVx8c"
bot = telebot.TeleBot(BOT_TOKEN)

# هذا الجزء يضمن استمرار عمل البوت حتى لو حدث خطأ بسيط في الاتصال
def run_bot():
    print("جاري تشغيل البوت...")
    while True:
        try:
            bot.polling(none_stop=True, interval=0, timeout=20)
        except Exception as e:
            print(f"حدث خطأ: {e}")
            time.sleep(5)  # ينتظر 5 ثواني ثم يعيد المحاولة

if __name__ == "__main__":
    run_bot()
