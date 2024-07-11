from aiogram import Router, types, F
from aiogram.filters.command import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from less3.keybords.prof_keyboards import make_row_keybord


router = Router()

available_jobs = [
    "Программист",
    "Дизайнер",
    "Маркетолог",
    "Руководитель",

]

available_grades = ['Junior', 'Middle', 'Senior']


class ChoiceProfile(StatesGroup):
    job = State()
    grade = State()


@router.message(Command("prof"))
async def command_prof(message: types.Message, state: FSMContext):
        await message.answer(
            text = "Выбери профессию",
            reply_markup = make_row_keybord(available_jobs))
        await state.set_state(ChoiceProfile.job)


@router.message(ChoiceProfile.job, F.text.in_(available_jobs))
async def prof_choisen(message: types.Message, state: FSMContext):
    await state.update_data(profession=message.text)
    await message.answer(
        text="Выберите уровень",
        reply_markup=make_row_keybord(available_grades))
    await state.set_state(ChoiceProfile.grade)



@router.message(ChoiceProfile.job)
async def prof_choisen_corr(message: types.Message):
    await message.answer(
        text="Выбери профессию",
        reply_markup=make_row_keybord(available_jobs))


@router.message(ChoiceProfile.grade, F.text.in_(available_grades))
async def grade_choisen(message: types.Message, state: FSMContext):
    user_data = await state.get_data()
    await message.answer(f"Ваша профессия: {user_data['profession']}\n"
                        f'Ваш уровень: {message.text}',
                        reply_markup=types.ReplyKeyboardRemove())
    await state.clear()


@router.message(ChoiceProfile.grade)
async def grade_choisen_corr(message: types.Message):
    await message.answer(
        text="Выберите уровень",
        reply_markup=make_row_keybord(available_grades))



    

