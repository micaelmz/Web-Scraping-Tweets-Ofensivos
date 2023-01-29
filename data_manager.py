import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas
from random import choice, randint
import smtplib
import datetime as dt


class DataManager(object):
    """
    Essa classe é responsável por lidar com o gerenciamento de dados, como o envio de emails e o upload de arquivos para o google sheets.
    """

    def __init__(self):
        super().__init__()
        self.swear_list = pandas.read_csv('datasets/swear_list-PT-BR.csv', index_col=False)  # lista de palavras ofensivas
        self.swear_list_category = self.swear_list.columns.tolist()  # categorias das palavras ofensivas
        self.my_email = ""  # email do remetente
        self.my_password = ""  # senha do email do remetente

    def authenticate_google_sheet(self):
        """
        Essa função é responsável por autenticar o google sheets.
        """
        scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets',
                 "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]
        credentials = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
        client = gspread.authorize(credentials)
        return client

    def upload_to_google_sheet(self, tweets, csv_type=False):
        """
        Essa função é responsável por fazer o upload do arquivo csv para o google sheets.
        """
        sheet_name = "Rovena-Results"
        client = self.authenticate_google_sheet()

        spreadsheet = client.open(sheet_name)  # o arquivo que será editado no google sheets
        if csv_type:
            client.import_csv(spreadsheet.id, data=tweets)
        else:
            spreadsheet.values_append(sheet_name, {'valueInputOption': 'RAW'}, {'values': tweets})


    def clear_csv(self):
        """
        Essa função é responsável por limpar o arquivo csv.
        """
        df = pandas.DataFrame(columns=['Category', 'Text', 'Datetime', 'Tweet_Id',  'Username', 'Url', 'Word'])
        self.upload_to_google_sheet(tweets=df, csv_type=True)


    def pick_a_term(self):
        """
        Essa função é responsável por escolher um termo aleatório para o scraping.
        """
        random_category_id = randint(0, len(self.swear_list_category) - 1)
        swear_list = [word for word in self.swear_list[self.swear_list_category[random_category_id]] if
                      pandas.notnull(word)]
        swear_chosen = choice(swear_list)
        category_chosen = self.swear_list_category[random_category_id]
        return {"word": swear_chosen,
                "category": category_chosen}

    def send_email(self, info):
        pass
