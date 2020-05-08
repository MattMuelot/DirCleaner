import os
import time


class FileOrganizer:
	def __init__(self):
		self.fix_dir = 'C:\\Users\\chine\\Downloads\\'
		self.homeless_files = []
		self.directories = ['TEXT', 'EXCEL', 'IMAGES', 'INSTALLERS', 'PDF', 'ZIP']
		self.files_to_ignore = ['desktop.ini']
		self.text_types = ['.doc', '.docx', '.odt', '.rtf', '.txt']
		self.excel_types = ['.csv', '.mhtml', '.ods', '.xls', '.xlsb', '.xlsm', '.xlsx', '.xml', '.xlt', '.xps']
		self.img_types = ['.jpg', '.png', '.gif', '.jpeg']

	def check_directory(self):
		self.homeless_files = []
		os.chdir(self.fix_dir)
		files_in_directory = os.listdir(self.fix_dir)
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

	def move_files(self):
		while len(self.homeless_files) > 0:
			for f in self.homeless_files:
				for t in self.text_types:
					if t in f.lower():
						os.replace(f, 'TEXT\\' + f)
						self.homeless_files.remove(f)
						break
					else:
						pass
				for e in self.excel_types:
					if e in f.lower():
						os.replace(f, 'EXCEL\\' + f)
						self.homeless_files.remove(f)
						break
					else:
						pass
				for i in self.img_types:
					if i in f.lower():
						os.replace(f, 'IMAGES\\' + f)
						self.homeless_files.remove(f)
						break
					else:
						pass
				if '.pdf' in f.lower()

	def app_mainloop(self):
		try:
			self.check_directory()
			self.move_files()
		except:
			print('Error')
			time.sleep(5)

fl = FileOrganizer()
fl.app_mainloop()
