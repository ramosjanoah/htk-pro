import sys
import io
import re
import os
import shutil

list_word = []
list_phoneme_seq = []
mlf_word = ""
#SET INI!!
folder_dataset = "F:/Sashi/Kuliah S1/SEM7/NLP/IF4072 Tugas Besar Speech2/Dataset/" #Tempat nyimpen dataset tubes atau folder set_
folder_transcript = "F:/Sashi/Kuliah S1/SEM7/NLP/IF4072 Tugas Besar Speech2/Dataset/transcript/" #Tempat nyimpen data" transkrip

def readTranskrip(infile):
	print(infile)
	with open(infile,'r') as myfile:
		word = myfile.read()
		word = word.replace(".","")
		word = word.replace(",","")
		word = word.replace("?","")
		word = word.replace("!","")

		while ("  " in word):
			word = word.replace("  "," ")
		
		return word

def readTranskrip_raw(infile):
	with open(infile,'r') as myfile:
		return myfile.read()

def extractPhonemeSet(raw_transcript): 
	while(raw_transcript[-1]=='\n'):
		raw_transcript = raw_transcript[0:-1]
	list_row = raw_transcript.split('\n')
	
	for row in list_row:
		word_list_ori = row.split('\t')[1].split(' ')
		word_list_detail = row.split('\t')[2].split(' ')

		word_list_ori = [x for x in word_list_ori if x]
		word_list_detail = [x for x in word_list_detail if x]

		if len(word_list_ori)==len(word_list_detail):
			for i in range(0,len(word_list_ori)):
				same = 0
				word_re = []
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
						list_word.append(word_re[0])
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
			elif word[idx:idx+2]=='ch':
				phonem_seq+='h '
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
				phonem_seq+='k '
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
				if idx==0:
					phonem_seq+= "s "
				else:
					phonem_seq+="k s "
			elif word[idx]=='-' or word[idx]=='\'':
				phonem_seq+=''
			else:
				phonem_seq+="#"
			idx+=1	

	return phonem_seq[:-1]

def savePhonemeSet(outfile):
	outputF = open(outfile,'w')
	for i in range (0,len(list_word)):
		outputF.write(list_word[i]+"\t"+list_phoneme_seq[i]+"\n")
	outputF.close()

def sortPhonemeDict_file(infile):
	list_dict = readTranskrip(infile).split("\n")
	list_dict = (list(set(list_dict)))
	list_dict.sort()
	
	outputF = open("dict_phoneme",'w')
	outputF_wlist = open("wlist",'w')
	for i in range (1,len(list_dict)):
		outputF.write(list_dict[i]+"\n")
		outputF_wlist.write(list_dict[i].split("\t")[0]+"\n")
	outputF.close()

def listFolder(root_folder,key):
	folder_list = os.listdir(root_folder)
	folder_list = [folder for folder in folder_list if key in folder]
	for i in range (0,len(folder_list)):
		folder_list[i] = root_folder+folder_list[i]+"/"
	return folder_list

def crawlFile(uttr_code,forlder_list):
	find = 0
	idf = 0
	addr = ""
	while find==0 and idf < len(folder_list):
		sub_folder_list = listFolder(folder_list[idf],"")
		idsf = 0
		while find==0 and idsf < len(sub_folder_list):
			filelist = os.listdir(sub_folder_list[idsf])
			filelist = [file for file in filelist if uttr_code in file]
			if len(filelist)>0:
				addr = (sub_folder_list[idsf]+filelist[0])
				find = 1
			idsf+=1
		idf +=1
	return addr

def search_transcript(wav,folder_transcript):

	transcript_code = wav.replace(".wav","")[-4:]
	transcript_list = readTranskrip(folder_transcript+transcript_code[0]+"-raw.tsv").lower().split("\n")
	transcript = [trans for trans in transcript_list if ("_"+transcript_code[1:]) in trans][0]
	if len(transcript)>4:
		return transcript.split("\t")[1]
	else:
		return ""

def generateMLF_word_audio_based(folder_dataset, folder_transcript):
	mlf_word = ""
	folder_list = listFolder(folder_dataset,"set_")
	#root folder leve
	for set_folder in folder_list:
		#in set_ folder
		sub_set_list = os.listdir(set_folder)
		for sub_set in sub_set_list:
			wav_list = os.listdir(set_folder+sub_set)
			wav_list = [wav for wav in wav_list if '.wav' in wav and ' ' not in wav]

			for wav in wav_list:
				print(wav)
				transcript = search_transcript(wav,folder_transcript)
				if len(transcript)>4:
					mlf_word+= "\""+set_folder+"/"+sub_set+"/"+wav+"\"\n"
					words = transcript.split(" ")
					for word in words:
						if '-' not in word:
							mlf_word+=word+"\n"
						else:
							rep_word = word.split("-")
							if rep_word[0]==rep_word[1]:
								mlf_word+=rep_word[0]+"\n"+rep_word[1]+"\n"
							else:
								mlf_word+=word+"\n"
					mlf_word+='.\n'

	return mlf_word

def generateMLF_word(transcript_file,code):
	mlf_word = ""
	transcript_list = readTranskrip(transcript_file).lower().split("\n")
	for transcript in transcript_list:
		if ("\t" in transcript):
			file_path = crawlFile(code+transcript.split("\t")[0][-3:]+".wav", folder_list)
			if file_path!="":
				mlf_word+= "\""+file_path+"\""+"\n"
				words = transcript.split("\t")[1].split(" ")
				for word in words:
					if '-' not in word:
						mlf_word+=word+"\n"
					else:
						rep_word = word.split("-")
						if rep_word[0]==rep_word[1]:
							mlf_word+=rep_word[0]+"\n"+rep_word[1]+"\n"
						else:
							mlf_word+=word+"\n"
				mlf_word+='.\n'
	return mlf_word
	
def saveStr(instr,outfile):
	file = open(outfile,'w')
	file.write(instr)
	file.close()


def combine_transcript(folder_transcript):
	transcript_list = os.listdir(folder_transcript)
	transcript_list = [trans for trans in transcript_list if "-raw.tsv" in trans]
	comb_trans = ""
	for trans in transcript_list:
		comb_trans+=readTranskrip_raw(folder_transcript+trans)
	saveStr(comb_trans,'all_transcript.tsv')

def combine_audio_folder(folder_dataset,folder_target):
	folder_list = listFolder(folder_dataset,"set_")
	#root folder leve
	for set_folder in folder_list:
		#in set_ folder
		sub_set_list = os.listdir(set_folder)
		for sub_set in sub_set_list:
			wav_list = os.listdir(set_folder+sub_set)
			wav_list = [wav for wav in wav_list if '.wav' in wav]

			for wav in wav_list:
				shutil.copy((set_folder+"/"+sub_set+"/"+wav),folder_target)


extractPhonemeSet(readTranskrip(folder_transcript+'A-raw.tsv'))
extractPhonemeSet(readTranskrip(folder_transcript+'B-raw.tsv'))
extractPhonemeSet(readTranskrip(folder_transcript+'C-raw.tsv'))
extractPhonemeSet(readTranskrip(folder_transcript+'D-raw.tsv'))
extractPhonemeSet(readTranskrip(folder_transcript+'E-raw.tsv'))
extractPhonemeSet(readTranskrip(folder_transcript+'F-raw.tsv'))
extractPhonemeSet(readTranskrip(folder_transcript+'G-raw.tsv'))
extractPhonemeSet(readTranskrip(folder_transcript+'H-raw.tsv'))
extractPhonemeSet(readTranskrip(folder_transcript+'I-raw.tsv'))
extractPhonemeSet(readTranskrip(folder_transcript+'J-raw.tsv'))

savePhonemeSet('dict_phoneme')

sortPhonemeDict_file("dict_phoneme")

folder_list = listFolder(folder_dataset,"set_")
mlf_word = generateMLF_word(folder_transcript+"A-raw.tsv",'A')
mlf_word += generateMLF_word(folder_transcript+"B-raw.tsv",'B')
mlf_word += generateMLF_word(folder_transcript+"C-raw.tsv",'C')
mlf_word += generateMLF_word(folder_transcript+"D-raw.tsv",'D')
mlf_word += generateMLF_word(folder_transcript+"E-raw.tsv",'E')
mlf_word += generateMLF_word(folder_transcript+"F-raw.tsv",'F')
mlf_word += generateMLF_word(folder_transcript+"G-raw.tsv",'G')
mlf_word += generateMLF_word(folder_transcript+"H-raw.tsv",'H')
mlf_word += generateMLF_word(folder_transcript+"I-raw.tsv",'I')
mlf_word += generateMLF_word(folder_transcript+"J-raw.tsv",'J')


mlf_word=generateMLF_word_audio_based(folder_dataset, folder_transcript)
#Save words.mlf
while "\n\n" in mlf_word:
	mlf_word = mlf_word.replace("\n\n","\n")
mlf_word="#!MLF!#\n"+mlf_word
saveStr(mlf_word,"words.mlf")

#Generate dictionary "dict"
os.system("HDMan -m -w wlist -n monophones1 -l dlog dict dict_phoneme")
#Generate phones0.mlf
os.system("HLEd -d dict -X wav -i phones0.mlf mkphones0.led words.mlf")
