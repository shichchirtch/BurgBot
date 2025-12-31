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
    temp_dict = {'1': 'Ну и ладно', '2': 'Очень хорошо'}

    await callback.message.answer(f"{temp_dict[callback.data[-1]]}")
    dialog_manager.show_mode = ShowMode.SEND
    await dialog_manager.next()







