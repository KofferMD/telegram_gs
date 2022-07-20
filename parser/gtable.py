from datetime import date
from googleapiclient.discovery import build
from google.oauth2 import service_account

arr = list[list[str]]()

def update_table_data():
    SERVICE_ACCOUNT_FILE = 'key.json'
    SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

    creds = None
    creds = service_account.Credentials.from_service_account_file(
            SERVICE_ACCOUNT_FILE, scopes=SCOPES)

    # The ID spreadsheet.
    SAMPLE_SPREADSHEET_ID = '1HMlFxH5lG1HNpFJ_F-GrWgMBnd_5qI3Y9TlThi_iAek'

    service = build('sheets', 'v4', credentials=creds)

    # Call the Sheets API
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                    range="shedule!A2:M6").execute()
    # тут надо очистить arr и заполнить заново с таблицы
    data = result['values']
    return data
'''
result is JSON
{
    'range': 'shedule!A2:M6',
    'majorDimension': 'ROWS',
    'values': [
        ['Дата', '2022-07-14', '2022-07-15', '2022-07-16', '2022-07-17', '2022-07-18', '2022-07-19', '2022-07-20', '2022-07-21', '2022-07-22', '2022-07-23', '2022-07-24', '2022-07-25'],
        ['Винокуров', 'День', 'Ночь', 'Отсыпной', 'Выходной', 'День', 'Ночь', 'День', 'Ночь', 'Отсыпной', 'Выходной', 'День', 'Ночь'],
        ['Егоренчев ', 'Ночь', 'Отсыпной', 'Выходной', 'День', 'Ночь', 'Отсыпной', 'Ночь', 'Отсыпной', 'Выходной', 'День', 'Ночь', 'Отсыпной'],
        ['Бережной', 'Отсыпоной', 'Выходной', 'День', 'Ночь', 'Отсыпоной', 'Выходной', 'Отсыпоной', 'Выходной', 'День', 'Ночь', 'Отсыпоной', 'Выходной'],
        ['Подугин', 'Выходной', 'День', 'Ночь', 'Отсыпной', 'Выходной', 'День', 'Выходной', 'День', 'Ночь', 'Отсыпной', 'Выходной', 'День']
    ]
}
'''

class Staff:
    name = str()
    id = int()

    def __init__(self, name: str, id: int):
        self.name = name
        self.id = id

    def print(self):
        print(f'id: {self.id}, name: {self.name}')

class Parser:
    cols = list[Staff]()
    members = list[str]()

    def __init__(self) -> None:
        pass

    def parse(self, data: list[list[str]]):
        for i in range(len(data)):
            self.cols.append(Staff(data[i][0],
                                   int(i)))
            data[i].pop(0)
            self.members.append(data[i])

    def print(self):
        for i in range(len(self.cols)):
            self.cols[i].print()
            print(self.members[i])

def find_working_staff():
    # тут обновление данных таблицы
    arr = update_table_data()
    p = Parser()
    p.parse(arr)
    # поиск
    cur_date = date.today().strftime('%Y-%m-%d')
    date_index = -1
    for i in range(len(p.members[0])):
        c = p.members[0][i]
        if c == cur_date:
            date_index = i
            break
    if date_index == -1:
        print('Ошибка. Такой даты нет в таблице')
        return
    # TO-DO: исправить наложение прошлых ответов бота
    working = ''

    for i in range(1, len(p.members)):
        if p.members[i][date_index] == 'День':  # День / Ночь
            if working != '':
                working += '; '
            working += f'{p.cols[i].name} - День'
        elif p.members[i][date_index] == 'Ночь':
            if working != '':
                working += '; '
            working += f'{p.cols[i].name} - Ночь'
    print(working)
    return working

