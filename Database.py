from openpyxl import Workbook, load_workbook
from collections import defaultdict


def fix_date(date: str) -> str:
    """
    changes (or not) and returns a date string to a string in format DD/MM
    :param date: a date string containing day and month
    :return: date represented in DD/MM format
    """

    lst = date.split("/")  # a list with two items DD, MM
    lst = [("0" + i if len(i) == 1 else i) for i in lst]  # adds "0" to day or month if needed
    return "/".join(lst)


def load_database_dict():
    """
    Reads xlsx file and loads python dict
    :return: dict in format {date string : [teacher names]}
    """

    dates_names_dict = defaultdict(lambda: [])
    wb = load_workbook('Teachers-Bday.xlsx')
    ws = wb.active

    for row in range(2, ws.max_row):
        date = fix_date(ws["B" + str(row)].value)
        name = ws["A" + str(row)].value

        dates_names_dict[date].append(name)
    return dates_names_dict
