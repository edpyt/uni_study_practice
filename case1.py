from datetime import date

WEEK_DAYS = {
    0: "Понедельник",
    1: "Вторник",
    2: "Среда",
    3: "Четверг",
    4: "Пятница",
    5: "Суббота",
    6: "Воскресенье",
}
DIGITAL_DIGITS = {
    "0": (" *** ", "*   *", "*   *", "*   *", " *** "),
    "1": ("  *  ", " **  ", "  *  ", "  *  ", "*****"),
    "2": (" *** ", "*   *", "   * ", "  *  ", "*****"),
    "3": (" *** ", "*   *", "  ** ", "*   *", " *** "),
    "4": ("   * ", "  ** ", " * * ", "*****", "   * "),
    "5": ("*****", "*    ", "**** ", "    *", "**** "),
    "6": (" *** ", "*    ", "**** ", "*   *", " *** "),
    "7": ("*****", "   * ", "  *  ", " *   ", "*    "),
    "8": (" *** ", "*   *", " *** ", "*   *", " *** "),
    "9": (" *** ", "*   *", " ****", "    *", " *** "),
    " ": ("     ", "     ", "     ", "     ", "     "),
}


def which_weekday(birthday: date) -> str:
    return WEEK_DAYS[birthday.weekday()]


def is_leap_year(birthday: date) -> bool:
    return birthday.year % 4 == 0 and (
        birthday.year % 100 != 0 or birthday.year % 400 == 0
    )


def retrieve_ages_from_birthday(birthday: date) -> int:
    today = date.today()
    return today.replace(year=today.year - birthday.year).year


def _print_birthdate(birthday: date) -> None:
    date_str = f"{birthday.day:02d} {birthday.month:02d} {birthday.year}"

    for row in range(5):
        line = ""
        for ch in date_str:
            line += DIGITAL_DIGITS[ch][row] + "  "
        print(line)


def main():
    print("Введите День рождения")
    birthday = date(
        *[
            int(i)
            for i in (
                input("Число: "),
                input("Месяц: "),
                input("Год: "),
            )
        ][::-1]
    )
    print("-" * 20)
    print("День недели:", which_weekday(birthday))
    print("Год високосный:", is_leap_year(birthday))
    print("Пользователю в этом году:", retrieve_ages_from_birthday(birthday))
    print("-" * 20)
    _print_birthdate(birthday)


if __name__ == "__main__":
    main()
