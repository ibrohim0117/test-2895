from aiogram.fsm.state import State, StatesGroup


class AddFilm(StatesGroup):
    name = State()
    year = State()
    janr = State()
    language = State()
    sifati = State()
    about = State()
    kino_code = State()
    kino_file_id = State()


class SearchFilm(StatesGroup):
    code = State()