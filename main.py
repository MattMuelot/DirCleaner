import os
from DirectoryDecorators import Decorators
import platform


class FileOrganizer:
    def __init__(self, working_dir):
        self.working_dir = working_dir
        self.homeless_files = []
        self.directories = ['TEXT', 'EXCEL', 'IMAGES', 'INSTALLERS', 'PDF', 'ZIP', 'UNKNOWN']
        self.files_to_ignore = ['desktop.ini']
        self.text_types = ['.doc', '.docx', '.odt', '.rtf', '.txt']
        self.excel_types = ['.csv', '.mhtml', '.ods', '.xls', '.xlsb', '.xlsm', '.xlsx', '.xml', '.xlt', '.xps']
        self.img_types = ['.jpg', '.png', '.gif', '.jpeg']
        self.num_moved = 0
        self.sys_type = platform.system()

    def check_directory(self):
        self.homeless_files = []
        os.chdir(self.working_dir)
        files_in_directory = os.listdir(self.working_dir)
        for d in self.directories:
            if d not in files_in_directory:
                os.mkdir(d)
        for f in files_in_directory:
            if f in self.directories:
                pass
            else:
                if f not in self.files_to_ignore:
                    self.homeless_files.append(f)
                else:
                    pass

    def move_files_win(self):
        while len(self.homeless_files) > 0:
            for f in self.homeless_files:
                for t in self.text_types:
                    if t in f.lower():
                        os.replace(f, 'TEXT\\' + f)
                        self.homeless_files.remove(f)
                        self.num_moved += 1
                        break
                    else:
                        pass
                for e in self.excel_types:
                    if e in f.lower():
                        os.replace(f, 'EXCEL\\' + f)
                        self.homeless_files.remove(f)
                        self.num_moved += 1
                        break
                    else:
                        pass
                for i in self.img_types:
                    if i in f.lower():
                        os.replace(f, 'IMAGES\\' + f)
                        self.homeless_files.remove(f)
                        self.num_moved += 1
                        break
                    else:
                        pass
                if '.pdf' in f.lower():
                    os.replace(f, 'PDF\\' + f)
                    self.homeless_files.remove(f)
                    self.num_moved += 1
            for f in self.homeless_files:
                os.replace(f, 'UNKNOWN\\' + f)
                self.homeless_files.remove(f)
                self.num_moved += 1

    def move_files_lin(self):
        # TODO: Add Linux functionality, working with file names with/without extensions.
        pass

    @Decorators.completion_decorator
    def app_mainloop(self):
        try:
            if self.sys_type == 'Windows':
                self.check_directory()
                self.move_files_win()
                return self.num_moved
            elif self.sys_type == 'Linux':
                self.check_directory()
                # self.move_files_lin()
                return self.num_moved
        except:
            return False


fl = FileOrganizer(input('Path: '))
fl.app_mainloop()
