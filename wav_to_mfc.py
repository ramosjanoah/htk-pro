import os
import sys
import subprocess

def main():
	if len(sys.argv) == 2:
		with open('train.scp', 'w+') as file_train:
			with open('codetr.scp', 'w+') as file_code:
				path = sys.argv[1]
				for folder in os.listdir(path):
					for filename in os.listdir(path+'/'+folder):
						if (filename[-3:].lower() == 'wav'):
							full_path = path+'/'+folder+'/'+filename
							mfc_full_path = full_path[:-3] + 'mfc'
							file_code.write(full_path + ' ' + mfc_full_path + '\n')
							file_train.write(mfc_full_path + '\n')
		subprocess.call(['HCopy', '-C', 'conf-extraction', '-S', 'codetr.scp'])

if __name__ == "__main__":
	main()
