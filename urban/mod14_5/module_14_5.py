from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import asyncio
import crud_functions as cr_f

api = ""
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Рассчитать"),
            KeyboardButton(text="Регистрация"),
            KeyboardButton(text="Информация")
        ],
        [KeyboardButton(text="Купить")]
    ],
    resize_keyboard=True
)

kbin = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Рассчитать норму калорий", callback_data="calories"),
            InlineKeyboardButton(text="Формулы расчёта", callback_data="formulas")
        ]
    ],
    resize_keyboard=True
)

kbuy = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Product1", callback_data="product_buying"),
            InlineKeyboardButton(text="Product2", callback_data="product_buying"),
            InlineKeyboardButton(text="Product3", callback_data="product_buying"),
            InlineKeyboardButton(text="Product4", callback_data="product_buying")
        ]
    ],
    resize_keyboard=True
)


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


class RegistrationState(StatesGroup):
    username = State()
    email = State()
    age = State()
    balance = State(state="1000")


@dp.message_handler(commands=['start'])
async def start(message):
    await message.answer("Привет! Я бот помогающий твоему здоровью.", reply_markup=kb)


@dp.message_handler(text="Рассчитать")
async def main_menu(message):
    await message.answer("Выберите опцию:", reply_markup=kbin)


@dp.message_handler(text="Купить")
async def get_buying_list(message):
    records = cr_f.get_all_products()
    for rec in records:
        await message.answer(f"Название: {rec[1]} | Описание: {rec[2]} | Цена: {rec[3]}")
        try:
            with open(f"images/{rec[0]}.png", "rb") as img:
                await message.answer_photo(img)

        except FileNotFoundError:
            await message.answer("НЕТ ФОТО")

    await message.answer("Выберите опцию:", reply_markup=kbuy)


@dp.callback_query_handler(text="product_buying")
async def ssend_confirm_message(call):
    await call.message.answer("Вы успешно приобрели продукт!")
    await call.answer()


@dp.callback_query_handler(text="formulas")
async def get_formulas(call):
    await call.message.answer("для мужчин: 10 х вес (кг) + 6,25 x рост (см) – 5 х возраст (г) + 5:\n"
                              "для женщин: 10 x вес (кг) + 6,25 x рост (см) – 5 x возраст (г) – 161")
    await call.answer()

# ------ Начало функций цепочки состояний UserState: ------------
@dp.callback_query_handler(text="calories")
async def set_age(call):
    await call.message.answer("Введите свой возраст:")
    await call.answer()
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

# ------------ Конец функций цепочки состояний для UserState ------------


# ------------ Начало функций цепочки состояний RegistrationState: -------------
@dp.message_handler(text="Регистрация")
async def sing_up(message):
    await message.answer("Введите имя пользователя (только латинский алфавит):")
    await RegistrationState.username.set()


@dp.message_handler(state=RegistrationState.username)
async def set_username(message, state):
    if cr_f.is_included(message.text):
        await message.answer("Пользователь существует, введите другое имя:")
        await RegistrationState.username.set()

    else:
        await state.update_data(username=message.text)
        await message.answer("Введите свой email:")
        await RegistrationState.email.set()


@dp.message_handler(state=RegistrationState.email)
async def set_email(message, state):
    await state.update_data(email=message.text)
    await message.answer("Введите свой возраст:")
    await RegistrationState.age.set()


@dp.message_handler(state=RegistrationState.age)
async def set_age(message, state):
    await state.update_data(age=message.text)
    data = await state.get_data()
    cr_f.add_user(**data)
    await message.answer("Регистрация прошла успешно")
    await state.finish()

# ------------ Конец функций цепочки состояний для RegistrationState ------------


@dp.message_handler()
async def all_message(message):
    await message.answer("Нажмите кнопку 'Рассчитать',\nчтобы узнать о норме потребления калорий.\n"
                         "Либо команду /start для входа в главное меню")


if __name__ == "__main__":
    cr_f.initiate_db()
    executor.start_polling(dp, skip_updates=True)
