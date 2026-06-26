hereimport requests
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command
import asyncio

# مفاتيح العمل (تذكر أن تقوم بتغييرها فوراً بعد النسخ!)
TOKEN = '8851361153:AAHuWsxPX3S6bDt3mixzL5OzvidSqWSShQM'
FIVE_SIM_KEY = 'E00ca14d01544541b1156bf1340f6d49'
SMM_API_KEY = '67ea662a7e0988d93131434df275fcb4'

bot = Bot(token=TOKEN)
dp = Dispatcher()

# دالة لحساب السعر الجديد
def calculate_price(original_price, profit_percentage):
    # نضرب في (1 + النسبة) للحصول على السعر الجديد
    return round(float(original_price) * (1 + (profit_percentage / 100)), 2)

@dp.message(Command("start"))
async def start(message: types.Message):
    await message.answer("مرحباً! اختر الخدمة:\n1. طلب رقم (ربح 20%)\n2. طلب متابعين (ربح 5%)")

# مثال لطلب رقم مع إضافة 20% ربح
@dp.message(F.text == "رقم")
async def get_price_number(message: types.Message):
    # نفترض أن السعر الأصلي من الموقع هو 1 دولار
    original_price = 1.00 
    final_price = calculate_price(original_price, 20)
    await message.answer(f"سعر الرقم هو: {final_price}$ (شامل ربح 20%)")

# مثال لطلب متابعين مع إضافة 5% ربح
@dp.message(F.text == "متابعين")
async def get_price_followers(message: types.Message):
    # نفترض أن السعر الأصلي هو 0.5 دولار
    original_price = 0.50
    final_price = calculate_price(original_price, 5)
    await message.answer(f"سعر 1000 متابع هو: {final_price}$ (شامل ربح 5%)")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
