from aiogram.types import CallbackQuery
from aiogram_dialog.api.entities.modes import ShowMode
from aiogram_dialog.widgets.kbd import ManagedRadio
from aiogram_dialog import DialogManager
from my_fast_api import r


async def get_user_count():
    users_started_bot_allready = await r.scard("users")  # Считаю юзеров
    return users_started_bot_allready


async def radio_spam_button_clicked(callback: CallbackQuery,
                                    radio: ManagedRadio,
                                    dialog_manager: DialogManager, *args, **kwargs):
    temp_dict = {'1': 'Nun ja', '2': 'Sehr gut !'}
    user_id = str(callback.from_user.id)
    await callback.message.answer(f"{temp_dict[callback.data[-1]]}")

    key_profile = f"user:{user_id}:profile"
    choice = callback.data[-1]
    if choice == '2':
        await r.hset(key_profile, mapping={
            "spam_opt_in": "2",
        })

    dialog_manager.show_mode = ShowMode.SEND
    await dialog_manager.next()

async def get_total_months_count() -> int:
    """
    Возвращает общее количество месяцев
    во всех user:{user_id}:months
    """
    total = 0

    user_ids = await r.smembers("users")

    for user_id in user_ids:
        key = f"user:{user_id}:months"
        count = await r.scard(key)
        total += count

        # если ключа нет или тип другой — просто пропускаем
    return total






