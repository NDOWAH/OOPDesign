import abc
from datetime import datetime


class WriteFile(object):
    """An abstract class for the LogFile and DelimFile
    classes"""
    __metaclass__ = abc.ABCMeta

    def __init__(self, file_name):
        self.file_name = file_name

    @abc.abstractmethod
    def write(self):
        return

    def write_line(self, text):
        file = open(self.file_name, 'a')
        file.write(text + '\n')
        file.close()


class DelimFile(WriteFile):
    """creates a csv file and file it with content"""
    def __init__(self, file_name, delim):
        super(DelimFile, self).__init__(file_name)
        self.delim = delim

    def write(self, text):
        line = self.delim.join(text)
        return self.write_line(line)


class LogFile(WriteFile):
    """creates a text file and file it with content"""
    def write(self, text):
        date_time = datetime.now()
        date_time_str = date_time.strftime('%Y-%m-%d %H:%M')
        self.write_line(f'{date_time_str} {text}')


csv_obj = DelimFile('csvfile', ',')
txt_obj = LogFile('txtfile')
csv_obj.write(['Jane', 'Paul', 'Peter', 'Stephanie', 'Mildred'])
txt_obj.write('This log message is correct')








