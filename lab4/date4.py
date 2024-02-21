from datetime import datetime

def difference_in_seconds(date1, date2):
    # Преобразование строк в объекты datetime
    dt1 = datetime.strptime(date1, '%Y-%m-%d %H:%M:%S')
    dt2 = datetime.strptime(date2, '%Y-%m-%d %H:%M:%S')

    # Расчет разницы в секундах
    diff_seconds = abs((dt2 - dt1).total_seconds())
    
    return diff_seconds

# Пример использования
date1 = '2024-01-01 12:00:20'
date2 = '2024-01-01 12:00:00'
difference = difference_in_seconds(date1, date2)
print("Разница в секундах между датами:", difference)
