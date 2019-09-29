import yaml


class I18n:
    def __init__(self, file_name: str):
        with open(f"app/locales/{file_name}.yaml", 'r') as file_stream:
            self.locale_file = yaml.safe_load(file_stream)

    def set_locale(self, locale: str):
        self.locale = locale

    def t(self, word: str):
        '''transrateメソッド'''
        return self.locale_file[self.locale][word]
