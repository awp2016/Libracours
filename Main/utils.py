from datetime import datetime


class FormUtils:
    def __get_birthday_years():
        current_year = datetime.now().year
        maximum_lifespan = 130  # in years
        return tuple(i for i in range(current_year,
                                      current_year - maximum_lifespan,
                                      -1))

    get_birthday_years = staticmethod(__get_birthday_years)
