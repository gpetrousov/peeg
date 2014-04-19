# Compiled by Petrousov Giannis 2012
# student University of Western Macedonia ICTE

win_size=3
win_cover=2

buf_counter=0

origin_file = 'results.txt'
dest_file = 'windowed.txt'

sig_paths=['Z','O','F','S'] #signal paths

for i in range(0,len(sig_paths)):
	SET_NAME = sig_paths[i]
	for j in xrange(1, 101):
			
        	print 'Begin the %dth SEGMENT of SET %d' % (j,i+1)
		#ka8orizoume to onoma toy txt
                if j < 10:		#mexri 009.txt
                	FILE_NAME = '00' + str(j)   #leei pio *.txt 8a anoi3ei
                elif j < 100:		#apo 010.txt ews 099.txt
                        FILE_NAME = '0' + str(j)
                else:
                        FILE_NAME = str(j)	#100.txt
                        
		origin_file = SET_NAME + '/' + SET_NAME + FILE_NAME + '.txt'
		dest_file = SET_NAME + '/' + SET_NAME + FILE_NAME + '.txt' + '.cut.txt'
		
		origin = open(origin_file, 'r')
		dest = open(dest_file, 'a')
		
		buf = origin.readlines()
		buf_counter = 0		
		
		for first in range(win_size): #grafei ta prwta sto window
		    print buf_counter
		    dest.write( '%f\n' % float( buf[ buf_counter ] ) )
		    buf_counter+=1	#deixnei to epomeno pou den exei graftei    

		#print "first ", buf_counter
		#print buf_counter

		while ( buf_counter < len(buf)):

		    tmp_counter = win_cover

		#print tmp_counter
		#print range(win_size-win_cover+1)

		    for second in range(win_size-win_cover+1): #grapse ta covered
			dest.write( '%f\n' % float(buf[ buf_counter-tmp_counter ] ) )
		#    print buf[ tmp_counter ]
			tmp_counter-=1

		    for third in range( win_size-win_cover): #grapse ta ypoloipa sto win-cover
			dest.write('%f\n' % float( buf[ buf_counter ] ))
			buf_counter+=1 #deixnei to epomeno pou den exei graftei
		print 'done with %s" ' % dest_file
print 'done all'
