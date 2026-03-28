from datetime import date

def days_until_new_year() -> int:
    """
    Вычисляет количество дней до наступления следующего Нового года.
    
    Returns:
        int: Количество дней до 1 января следующего года
    """
    today = date.today()
    next_new_year = date(today.year + 1, 1, 1)
    days_left = (next_new_year - today).days
    return days_left