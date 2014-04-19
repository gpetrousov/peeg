# a script to test PyEEG on real EEG data
# just define the data folders
# original script 
# for paper PyEEG:A Open Source Python Module for EEG/MEG Feature Extraction
# 2010/10/18  Xin Lin

# Graphical environment and improvements by Petrousov Giannis 
# student University of Western Macedonia ICTE

import sys,string
from pyeeg import *
from pylab import *
from numpy import *

from Tkinter import *

""" This is a script for testing PyEEG on data sets signals.
	
	Here list the feature abbreviations 
	
	'spect'  ======> spectral entropy
	'bp'      ======> bin_power
	'hurst'  ======> hurst
	'dfa'     ======> dfa
	'hjorth' ======> hjorth
	'pfd'     ======> pfd
	'apen'   ======> ap_en
	'hfd'     ======> hfd
	'fi'        ======> fisher_information
	'svd'     ======> svd_entropy
	
"""

### GE functions ###

def shutdown():  #destroy when exit pressed
        main_win.destroy()
	signal_win.destroy()

def shutdown_signal():
	signal_win.destroy()

def plus_func():
	SIG_PATHS.append(Entry(signal_win))
	SIG_PATHS[-1].pack()

def minus_func():
	SIG_PATHS[-1].pack_forget()
	del SIG_PATHS[-1]

####### ends #########


#### definition of feature plot function ###########
def feature_plot(IDX):

	AXIS = array([[-0.5,4.5,0.12,0.31],
						[-0.5,4.5,0.32,0.98],
						[-0.5,4.5,0.02,0.12],
						[-0.5,4.5,0.11,0.25],
						[-0.5,4.5,0, 1],
						[-0.5,4.5,0.52,0.69],
						[-0.5,4.5,0.574,0.609],
						[-0.5,4.5,0, 1],
						[-0.5,4.5,0.67,0.82],
						[-0.5,4.5,1.92,2.26]])

	N = 5
	NAME_MAP = {'1':'AP', '2':'DFA', '3':'FI', '4':'HFD', '5':'Hjorth', '6':'HURST', '7':'PFD', '8':'PSI', '9':'SPECT', '10':'SVD'}
	for i in xrange(1, len(IDX)):
		if IDX[i] == 1:
			NAME = NAME_MAP[str(i)]  #onoma synartisis
			f1=open('Z.'+NAME+'.A.txt','r')
			#f1=open('Z/'+NAME+'.A.txt','r')
			A=[]
			for line in f1.readlines():
				A.append(map(double, line.split()))

			
			f2=open('O.'+NAME+'.B.txt','r')
			#f2=open('O/'+NAME+'.B.txt','r')
			B=[]
			for line in f2.readlines():
				B.append(map(double, line.split()))

			f3=open('N.'+NAME+'.C.txt','r')
			#f3=open('N/'+NAME+'.C.txt','r')
			C=[]
			for line in f3.readlines():
				C.append(map(double, line.split()))

			f4=open('F.'+NAME+'.D.txt','r')
			#f4=open('F/'+NAME+'.D.txt','r')
			D=[]
			for line in f4.readlines():
				D.append(map(double, line.split()))

			f5=open('S.'+NAME+'.E.txt','r')
			#f5=open('S/'+NAME+'.E.txt','r')
			E=[]
			for line in f5.readlines():
				E.append(map(double, line.split()))


			A = array(A)
			B = array(B)
			C = array(C)
			D = array(D)
			E = array(E)
			
			x = range(0,len(A))
			if NAME == 'Hjorth':
				Mobmean = [mean(A[:,0]),mean(B[:,0]),mean(C[:,0]),mean(D[:,0]),mean(E[:,0])]
				Mobstd = [var(A[:,0]),var(B[:,0]),var(C[:,0]),var(D[:,0]),var(E[:,0])]
				maxcom=max(max(A[:,1]),max(B[:,1]),max(C[:,1]),max(D[:,1]),max(E[:,1]))
				mincom=min(min(A[:,1]),min(B[:,1]),min(C[:,1]),min(D[:,1]),min(E[:,1]))
				A[:,1]=(A[:,1]-mincom)/(maxcom-mincom)
				B[:,1]=(B[:,1]-mincom)/(maxcom-mincom)
				C[:,1]=(C[:,1]-mincom)/(maxcom-mincom)
				D[:,1]=(D[:,1]-mincom)/(maxcom-mincom)
				E[:,1]=(E[:,1]-mincom)/(maxcom-mincom)
				Commean = [mean(A[:,1]),mean(B[:,1]),mean(C[:,1]),mean(D[:,1]),mean(E[:,1])]
				Comstd = [var(A[:,1]),var(B[:,1]),var(C[:,1]),var(D[:,1]),var(E[:,1])]
		
				figure(i, figsize=(12,6))
				subplot(121)
				ind = arange(N)  # the x locations for the groups
				width = 0.5       # the width of the bars
				p2 = errorbar(ind, Mobmean, Mobstd,marker='s',linestyle='-',linewidth=0.5,markersize=0.1)
				axis([-0.5,4.5,0.0025,0.0060])
				xticks(ind, ('A', 'B', 'C', 'D', 'E'),size=20 )
				title('(a) Hjorth Mobility',size=20)
				subplot(122)
				p2 = errorbar(ind, Commean, Comstd,marker='s',linestyle='-',linewidth=0.5,markersize=0.1)
				xticks(ind, ('A', 'B', 'C', 'D', 'E'),size=20)
				xlim(-width,len(ind))
				title('(b) Hjorth Complexity',size=20)
				savefig('Hjorth.png')
					
			elif NAME == 'PSI':			### bin power case
		
				MA = mean(A, 0)
				MB = mean(B, 0)
				MC = mean(C, 0)
				MD = mean(D, 0)
				ME = mean(E, 0)
		
				figure(i, figsize=(30,6))
				subplot(151)
				plot(MA, 'b')
				#import code;code.interact(local=locals())
				axis([-1,43,0,350000])
				grid(True)
				title('A', size=20)

				subplot(152)
				plot(MB, 'c')
				axis([-1,43,0,500000])
				grid(True)
				title('B', size=20)

				subplot(153)
				plot(MC, 'm')
				axis([-1,43,0,600000])
				grid(True)
				title('C', size=20)

				subplot(154)
				plot(MD, 'r')
				axis([-1,43,0,750000])
				grid(True)
				title('D', size=20)

				subplot(155)
				plot(ME, 'y')
				axis([-1,43,0,2500000])
				grid(True)
				title('E', size=20)
				savefig('PSI.png')
	
			else:				## other cases
	
				Mean = [mean(A),mean(B),mean(C),mean(D),mean(E)]
				Std = [var(A),var(B),var(C),var(D),var(E)]

				figure(i, figsize=(5,5))
				ind = arange(N)  # the x locations for the groups
				width = 0.5       # the width of the bars		
				p2 = errorbar(ind, Mean, Std,marker='s',linestyle='-',linewidth=0.5,markersize=2)
				axis(AXIS[i-1][:])
				xticks(ind, ('A', 'B', 'C', 'D', 'E'),size=20)
				title(NAME,size=20)
				savefig(NAME + '.png')
	show()
	
####### Begin the main part #####################
####### Define the parameters ##############
### Note if you change these default parameter values, you may need to adjust the axis interval when plotting

FEA_IDX = {'spect':0, 'bp':0, 'hurst':0, 'dfa':0, 'hjorth':0, 'pfd':0, 'apen':0, 'hfd':0, 'fi':0, 'svd':0}

SIG_PATHS=[]

def play(spect_var, bp_var, hurst_var, dfa_var, hjorth_var, pfd_var, apen_var, hfd_var, fi_var, svd_va):	

        DIM = 10
        TAU = 4
        Kmax = 5
        Fs = 173
        Band = [2*i+1 for i in xrange(0, 43)]		## 0.5~85 Hz
        SET_MAP = {'A':'Z', 'B':'O', 'C':'N', 'D':'F','E':'S'}   #de3ia einai o fakelos, aristera einai to string gia to teliko onoma
        FEA_MAP = {'apen':'1', 'dfa':'2', 'fi':'3', 'hfd':'4', 'hjorth':'5', 'hurst':'6', 'pfd':'7', 'bp':'8', 'spect':'9', 'svd':'10'}
        ALL = 0
        FLAG = zeros(11)

        if (spect_var.get() == 1):
                FEA_IDX['spect']=1 	
		FLAG[9]=1
		
        if (bp_var.get()==1):
		FEA_IDX['bp']=1
		FLAG[8]=1
		
	if (hurst_var.get()==1):
		FEA_IDX['hurst']=1
		FLAG[6]=1
		
	if (dfa_var.get()==1):
		FEA_IDX['dfa']=1
		FLAG[2]=1
		
	if (hjorth_var.get()==1):
		FEA_IDX['hjorth']=1
		FLAG[5]=1
		
	if (pfd_var.get()==1):
		FEA_IDX['pfd']=1
		FLAG[7]=1
		
	if (apen_var.get()==1):
	        FEA_IDX['apen']=1
	        FLAG[1]=1
	        
	if (hfd_var.get()==1):
		FEA_IDX['hfd']=1
		FLAG[4]=1
		
	if (fi_var.get()==1):
		FEA_IDX['fi']=1
		FLAG[3]=1
		
	if (svd_var.get()==1):
		FEA_IDX['svd']=1	
		FLAG[10]=1
		
        ##### Feature Extraction part ################
        
        for i in range(0,len(SIG_PATHS)):     #loop gia ta paths twn simatwn
		
                SET_NAME=SIG_PATHS[i].get()		# mporeis na valeis to apolyto path H to sxetiko
                
                print 'Begin with %c' % SET_NAME[-1]  #kratame to teleytaio gramma toy path 
		
                for j in xrange(1, 101):
                        print 'Begin the %dth SEGMENT of SET %d' % (j,i+1)

                        if (j == 100):   #otan ftasei stin teleytaia grammi 8a pei pou apo8ikeyse to apotelesma
                            print '<--RESULT SAVED IN "%s" ' % RESULT_DIR
			#ka8orizoume to onoma toy txt
                        if j < 10:		#mexri 009.txt
                                FILE_NAME = '00' + str(j)   #leei pio *.txt 8a anoi3ei
                        elif j < 100:		#apo 010.txt ews 099.txt
                                FILE_NAME = '0' + str(j)
                        else:
                                FILE_NAME = str(j)	#100.txt
                                
                        #ka8orizei onoma path + txt
                        FILE_NAME = SET_NAME + '/' + SET_NAME[-1] + FILE_NAME + '.txt' + '.cut.txt'

                        FILE_DIR = FILE_NAME
                        
                        fid = open(FILE_DIR, 'r')     #anoigei to *.txt, reading
                        
                        print FILE_DIR
                        
                        tmp = fid.readlines()    #epistrefei oles tis grammes tou arxeioy sto tmp
                        
                        DATA = [float(k) for k in tmp]   #DATA=stoixeio (data loop)
                        
                ####### Methods ######## stelnei to ka8e stoixeio (grammi) sti synartisi
                	
                        if (FEA_IDX['spect']):      #an FEA_IDX=1 
                                print 'spectral entropy...\n',
                                RESULT_DIR = SET_NAME[-1] + '.SPECT' + '.txt'  #apo8ikeyetai sto path toy programmatos
                                fod = open(RESULT_DIR, 'a')
                                result = spectral_entropy(DATA, Band, Fs)  #periexei to apotelesma
                                fod.write('%f\n' % float(result)) #grafei to apotelesma sto arxeio
                        
                        if (FEA_IDX['bp']):
                                print 'PSI ...\n',
                                RESULT_DIR = SET_NAME[-1] + '.PSI' + '.txt'
                                fod = open(RESULT_DIR, 'a')
                                result = bin_power(DATA, Band, Fs)
                                for k in result[0]:
                                        fod.write('%f\t' % float(k))
                                fod.write('\n')
                                RESULT_DIR = SET_NAME[-1] + '.RIR' + '.txt'
                                fod = open(RESULT_DIR, 'a')
                                for k in result[1]:
                                        fod.write('%f\t' % float(k))
                                fod.write('\n')	
                
                        if (FEA_IDX['hurst']):
                                print 'Hurst Exponent...\n',
                                RESULT_DIR = SET_NAME[-1] + '.HURST' + '.txt'
                                fod = open(RESULT_DIR, 'a')
                                result = hurst(DATA)
                                if not isnan(result):
                                        fod.write('%f\n' % float(result))
                                print '<--result line saved in "%s" ' % RESULT_DIR
                        
                        if (FEA_IDX['dfa']):
                                print 'DFA...\n',
                                RESULT_DIR = SET_NAME[-1] + '.DFA' + '.txt'
                                fod = open(RESULT_DIR, 'a')
                                #import code;code.interact(local=locals())
                                result = dfa(DATA)
                                fod.write('%f\n' % float(result))
                        
                        if (FEA_IDX['hjorth']):
                                print 'Hjorth...\n',
                                RESULT_DIR = SET_NAME[-1] + '.Hjorth' + '.txt'
                                fod = open(RESULT_DIR, 'a')
                                result = hjorth(DATA)
                                fod.write('%f\t%f\n' % (float(result[0]),float(result[1])))

                        if (FEA_IDX['pfd']):
                                print 'PFD...\n',
                                RESULT_DIR = SET_NAME[-1] + '.PFD' + '.txt'
                                fod = open(RESULT_DIR, 'a')
                                result = pfd(DATA)
                                fod.write('%f\n' % float(result))
                        
                        if (FEA_IDX['apen']):
                                print 'approximate entropy...\n',
                                R = std(DATA) * 0.3
                                RESULT_DIR = SET_NAME[-1] + '.AP' + '.txt'
                                fod = open(RESULT_DIR, 'a')
                                result = ap_entropy(DATA, DIM, R)
                                fod.write('%f\n' % float(result))
                        
                        if (FEA_IDX['hfd']):
                                print 'HFD...\n',
                                RESULT_DIR = SET_NAME[-1] + '.HFD' + '.txt'
                                fod = open(RESULT_DIR, 'a')
                                result = hfd(DATA, Kmax)
                                fod.write('%f\n' % float(result))
                        
                        if (FEA_IDX['fi']):
                                print 'fisher information...\n',
                                M = embed_seq(DATA, TAU, DIM)
                                W = svd(M, compute_uv=0)
                                W /= sum(W)	
                                RESULT_DIR = SET_NAME[-1] + '.FI' + '.txt'	
                                fod = open(RESULT_DIR, 'a')		
                                result = fisher_info(DATA, TAU, DIM, W)
                                fod.write('%f\n' % float(result))
                        
                        if (FEA_IDX['svd']):
                                print 'SVD entropy...\n'
                                M = embed_seq(DATA, TAU, DIM)
                                W = svd(M, compute_uv=0)
                                W /= sum(W)                                
                                RESULT_DIR = SET_NAME[-1] + '.SVD' + '.txt'
                                fod = open(RESULT_DIR, 'a')
                                result = svd_entropy(DATA, TAU, DIM, W)
                                fod.write('%f\n' % float(result))
	
        ###### Plot part #######
        #feature_plot(FLAG)

if __name__=="__main__":

#main window is fixed first
	main_win=Tk()           #main windows shows all functions
	main_win.title("pyeeg")  #main window title
	main_win.geometry("300x650+300+300")
	main_win.protocol('WM_DELETE_WINDOW', shutdown)
	
	message=Label(main_win, text="Choose functions to execute", height=3)
	message.pack()
	
	#signal path window is fixed second
	
	signal_win=Tk()
	signal_win.title("signals")
	signal_win.geometry("300x500+300+300")
	signal_win.protocol("WM_DELETE_WINDOW", shutdown_signal)
	
	message_signal=Label(signal_win, text="choose signal paths", height=3)
	message_signal.pack()
	
	plus_button_var=IntVar()
	plus_button=Button(signal_win, text="add signal", height=1, width=5, command=plus_func)
	plus_button.pack(anchor=N)

	minus_button_var=IntVar()
	minus_button=Button(signal_win, text="remove signal", height=1, width=8, command=minus_func)
	minus_button.pack(anchor=N)
	
	#paths for signals
	SIG_PATHS.append(Entry(signal_win))
	SIG_PATHS[0].pack()
	############## ends ###############
		
	spect_var = IntVar()  #default value 0
	spect_button = Checkbutton(main_win, text="Spectral entropy", variable=spect_var, height=2)
	spect_button.pack()
	
	bp_var=IntVar()
	bp_button = Checkbutton(main_win, text="binary power", variable=bp_var, height=2, onvalue=1, offvalue=0)
	bp_button.pack()
	
	hurst_var=IntVar()
	hurst_button=Checkbutton(main_win, text="hurst", variable=hurst_var, height=2, onvalue=1, offvalue=0)
	hurst_button.pack()
	
	dfa_var=IntVar()
	dfa_button=Checkbutton(main_win, text="dfa", variable=dfa_var, height=2, onvalue=1, offvalue=0)
	dfa_button.pack()
	
	hjorth_var=IntVar()
	hjorth_button=Checkbutton(main_win, text="hjorth", variable=hjorth_var, height=2, onvalue=1, offvalue=0)
	hjorth_button.pack()
	
	pfd_var=IntVar()
	pfd_button=Checkbutton(main_win, text="pfd", variable=pfd_var, height=2, onvalue=1, offvalue=0)
	pfd_button.pack()
	
	apen_var=IntVar()
	apen_button=Checkbutton(main_win, text="ap en", variable=apen_var, height=2, onvalue=1, offvalue=0)
	apen_button.pack()
	
	hfd_var=IntVar()
	hfd_button=Checkbutton(main_win, text="hfd", variable=hfd_var, height=2, onvalue=1, offvalue=0)
	hfd_button.pack()
	
	fi_var=IntVar()
	fi_button=Checkbutton(main_win, text="fisher information", variable=fi_var, height=2, onvalue=1, offvalue=0)
	fi_button.pack()
	
	svd_var=IntVar()
	svd_button=Checkbutton(main_win, text="svd entropy", variable=svd_var, height=2, onvalue=1, offvalue=0)
	svd_button.pack()

	play_var=IntVar()
	play_button=Button(main_win, text="Play", height=2, width=10, command=lambda: play(spect_var, bp_var, hurst_var, dfa_var, hjorth_var, pfd_var, apen_var, hfd_var, fi_var, svd_var))
	play_button.pack()
	
	exit_var=IntVar()
	exit_button=Button(main_win, text="Exit", height=2, width=10, command=shutdown)
	exit_button.pack()
	
	main_win.mainloop()
	
		
		
