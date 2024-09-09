from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
import asyncio


api = ""
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

kb = ReplyKeyboardMarkup(resize_keyboard=True)
kb.add(KeyboardButton(text="Рассчитать"))
kb.add(KeyboardButton(text="Информация"))


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


@dp.message_handler(commands=['start'])
async def start(message):
    await message.answer("Привет! Я бот помогающий твоему здоровью.", reply_markup=kb)


@dp.message_handler(text="Рассчитать")
async def set_age(message):
    await message.answer("Введите свой возраст:")
    await UserState.age.set()


@dp.message_handler(state=UserState.age)
async def set_growth(message, state):
    await state.update_data(age=message.text)
    await message.answer("Введите свой рост:")
    await UserState.growth.set()


@dp.message_handler(state=UserState.growth)
async def set_weight(message, state):
    await state.update_data(growth=message.text)
    await message.answer("Введите свой вес:")
    await UserState.weight.set()


@dp.message_handler(state=UserState.weight)
async def send_calories(message, state):
    """  Упрощенный вариант формулы Миффлина-Сан Жеора:
    для мужчин: 10 х вес (кг) + 6,25 x рост (см) – 5 х возраст (г) + 5
    для женщин: 10 x вес (кг) + 6,25 x рост (см) – 5 x возраст (г) – 161

    """
    await state.update_data(weight=message.text)
    data = await state.get_data()
    calories_man = 10*int(data["weight"]) + 6.25*int(data["growth"]) - 5*int(data["age"]) + 5
    await message.answer(f"Ваша норма колорий: {calories_man}")
    await state.finish()


@dp.message_handler()
async def all_message(message):
    await message.answer("Нажмите кнопку 'Рассчитать',\nчтобы узнать о норме потребления калорий.")


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
