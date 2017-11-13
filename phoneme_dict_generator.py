import sys
import io
import re

list_word = []
list_phoneme_seq = []

def readTranskrip(infile):
	with open(infile,'r') as myfile:
		word = myfile.read().replace("  "," ")
		
		word = word.replace(".","")
		word = word.replace(",","")
		word = word.replace("?","")
		word = word.replace("!","")
		
		return word

def extractPhonemeSet(raw_transcript):
	list_row = raw_transcript.split('\n')
	list_row = list_row[0:-1]
	for row in list_row:
		word_list_ori = row.split('\t')[1].split(' ')
		word_list_detail = row.split('\t')[2].split(' ')
		
		if len(word_list_ori)!=len(word_list_detail):
			print(word_list_ori)
			print(word_list_detail)
			print("\n"+str(len(word_list_ori))+str(len(word_list_detail)))
		#numidx = len(word_list_ori)-abs(len(word_list_ori)-len(word_list_detail))

		if len(word_list_ori)==len(word_list_detail):
			for i in range(0,len(word_list_ori)):
				same = 0
				if '-' in word_list_ori[i]:
					word_re = word_list_ori[i].lower().split('-')
					if word_re[0]==word_re[1]:
						same = 1

				if same==0:
					if word_list_ori[i] not in list_word:
						list_word.append(word_list_ori[i].lower())
						list_phoneme_seq.append(phonemeSeqGenetor(word_list_detail[i].replace('E','@').lower()))
				else:
					if word_re[0] not in list_word:
						list_word.append(word_re[1])
						list_phoneme_seq.append(phonemeSeqGenetor(word_list_detail[i].split('-')[1].replace('E','@').lower()))	

		

def phonemeSeqGenetor(word):
	phonem_seq = ""
	idx = 0

	while idx < len(word):
		skip = 0
		if (idx+1<len(word)):
			if word[idx:idx+2]=='ai':
				phonem_seq+='ai '
				skip = 1
			elif word[idx:idx+2]=='au':
				phonem_seq+='au '
				skip = 1
			elif word[idx:idx+2]=='kh':
				phonem_seq+='kh '
				skip = 1
			elif word[idx:idx+2]=='ng':
				phonem_seq+='ng '
				skip = 1
			elif word[idx:idx+2]=='ny':
				phonem_seq+='ny '
				skip = 1
			elif word[idx:idx+2]=='oi':
				phonem_seq+='oi '
				skip = 1
			elif word[idx:idx+2]=='sy':
				phonem_seq+='sy '
				skip = 1
			elif word[idx:idx+2]=='dj':
				phonem_seq+='j '
				skip = 1
			if skip==1:
				idx+=2
			
		if skip==0:
			if word[idx]=='a':
				phonem_seq+='a '
			elif word[idx]=='b':
				phonem_seq+='b '
			elif word[idx]=='c':
				phonem_seq+='c '
			elif word[idx]=='d':
				phonem_seq+='d '
			elif word[idx]=='e':
				phonem_seq+='e '
			elif word[idx]=='@':
				phonem_seq+='@ '
			elif word[idx]=='f' or word[idx]=='v':
				phonem_seq+='f '
			elif word[idx]=='g':
				phonem_seq+='g '
			elif word[idx]=='h':
				phonem_seq+='h '
			elif word[idx]=='i':
				phonem_seq+='i '
			elif word[idx]=='j':
				phonem_seq+='j '
			elif word[idx]=='k':
				phonem_seq+='k '
			elif word[idx]=='l':
				phonem_seq+='l '
			elif word[idx]=='m':
				phonem_seq+='m '
			elif word[idx]=='n':
				phonem_seq+='n '
			elif word[idx]=='o':
				phonem_seq+='o '
			elif word[idx]=='p':
				phonem_seq+='p '
			elif word[idx]=='q':
				phonem_seq+='q '
			elif word[idx]=='r':
				phonem_seq+='r '
			elif word[idx]=='s':
				phonem_seq+='s '
			elif word[idx]=='t':
				phonem_seq+='t '
			elif word[idx]=='u':
				phonem_seq+='u '
			elif word[idx]=='w':
				phonem_seq+='w '
			elif word[idx]=='y':
				phonem_seq+='y '
			elif word[idx]=='z':
				phonem_seq+='z '
			elif word[idx]=='x':
				phonem_seq+="k s "
			elif word[idx]=='-' or word[idx]=='\'':
				phonem_seq+=''
			else:
				phonem_seq+="#"
			idx+=1	

	
	phonem_seq+='/'
	phonem_seq='/'+phonem_seq
	return phonem_seq

def savePhonemeSet(outfile):
	outputF = open(outfile,'w')
	for i in range (0,len(list_word)):
		outputF.write(list_word[i]+"\t"+list_phoneme_seq[i]+"\n")
	outputF.close()

transkrip = readTranskrip('F:/Sashi/Kuliah S1/SEM7/NLP/IF4072 Tugas Besar Speech/Dataset/transcript/B-raw.tsv')
extractPhonemeSet(readTranskrip('F:/Sashi/Kuliah S1/SEM7/NLP/IF4072 Tugas Besar Speech/Dataset/transcript/B-raw.tsv'))
extractPhonemeSet(readTranskrip('F:/Sashi/Kuliah S1/SEM7/NLP/IF4072 Tugas Besar Speech/Dataset/transcript/C-raw.tsv'))
extractPhonemeSet(readTranskrip('F:/Sashi/Kuliah S1/SEM7/NLP/IF4072 Tugas Besar Speech/Dataset/transcript/D-raw.tsv'))
extractPhonemeSet(readTranskrip('F:/Sashi/Kuliah S1/SEM7/NLP/IF4072 Tugas Besar Speech/Dataset/transcript/E-raw.tsv'))
extractPhonemeSet(readTranskrip('F:/Sashi/Kuliah S1/SEM7/NLP/IF4072 Tugas Besar Speech/Dataset/transcript/F-raw.tsv'))
extractPhonemeSet(readTranskrip('F:/Sashi/Kuliah S1/SEM7/NLP/IF4072 Tugas Besar Speech/Dataset/transcript/G-raw.tsv'))
extractPhonemeSet(readTranskrip('F:/Sashi/Kuliah S1/SEM7/NLP/IF4072 Tugas Besar Speech/Dataset/transcript/H-raw.tsv'))
extractPhonemeSet(readTranskrip('F:/Sashi/Kuliah S1/SEM7/NLP/IF4072 Tugas Besar Speech/Dataset/transcript/I-raw.tsv'))
extractPhonemeSet(readTranskrip('F:/Sashi/Kuliah S1/SEM7/NLP/IF4072 Tugas Besar Speech/Dataset/transcript/J-raw.tsv'))

savePhonemeSet('oout.txt')