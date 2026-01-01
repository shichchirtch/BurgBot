from aiogram.types import BotCommand


async def set_main_menu(bot):
    main_menu_commands = [
        BotCommand(command='/help',
                   description="manual bot's"),

        BotCommand(command='/about_project',
                   description='Info'),

        BotCommand(command='/hauptfenster',
                   description='zum Hauptfenster'),

        BotCommand(command='/wieviel',
                   description='wie viel Nutzern wurde gestartet')

    ]
    await bot.set_my_commands(main_menu_commands)