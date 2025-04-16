import logging

class FileManager:
    def __init__(self, filename):
        self.filename = filename

    def __enter__(self):
        try:
            self.file = open(self.filename, 'w')
            logging.info(f'Fayl "{self.filename}" ochildi.')
            return self.file
        except Exception as e:
            logging.error(f'Fayl ochishda xatolik yuz berdi: {str(e)}')
            raise

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type:
            logging.error(f'Xatolik yuz berdi: {str(exc_value)}')
        else:
            logging.info(f'Fayl yopildi.')
        if hasattr(self, 'file'):
            self.file.close()

logging.info('Dastur boshlandi.')

try:
    with FileManager('data.txt') as file:
        logging.info('Faylga yozilmoqda...')
        file.write('Bu test ma\'lumoti')
        logging.info('Faylga muvaffaqiyatli yozildi.')
except Exception as e:
    logging.error(f'Xatolik yuz berdi: {str(e)}')
