def calc():
	import csv
	import time
	fail,fail1,fail2,fail3,fail4,fail5,fail6,fail7,fail8,fail9,fail10,fail11,fail12,fail13,fail14,fail15,fail16,fail17,fail18,fail19,fail20,fail21,fail22,fail23,fail24,fail25,fail26,fail27,fail28,fail29,fail30,fail31,fail32,fail33,fail34,fail35,fail36,fail37=0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0
	count,count1,count2,count3,count4,count5,count6,count7,count8,count9,count10,count11,count12,count13,count14,count15,count16,count17,count18,count19,count20,count21,count22,count23,count24,count25,count26,count27,count28,count29,count30,count31,count31,count32,count33,count34,count35,count36,count37=0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0
	at,at1,at2,at3,at4,at5,at6,at7,at8,at9,at10,at11,at12,at13,at14,at15,at16,at17,at18,at19,at20,at21,at22,at23,at24,at25,at26,at27,at28,at29,at30,at31,at32,at33,at34,at35,at36,at37=0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0
	inel=0
	print('''
	 'CE302' : 'DESIGN OF HYDRAULIC STRUCTURES'
	 'CE304' : 'DESIGN OF CONCRETE STRUCTURES II'
	 'CE306' : 'COMPUTER PROGRAMMING AND COMPUTATIONAL TECHNIQUES'
	 'CE308' :'TRANSPORTATION ENGINEERING I'
	 'HS300' :'PRINCIPLES OF MANAGEMENT'
	 'CE374' :'AIR QUALITY MANAGEMEN'
	 'CE332' :'TRANSPORTATION ENGINEERING LAB'
	 'CE334' :'COMPUTER AIDED CIVIL ENGINEERING LAB'
	 'CE352' :'COMPREHENSIVE EXAM'
	 'CE362' :'GROUND IMPROVEMENT TECHNIQUES'
	 'CE366' :'TRAFFIC ENGINEERING AND MANAGEMENT'
	 'CS302' :'DESIGN AND ANALYSIS OF ALGORITHMS'
	 'CS304' :'COMPILER DESIGN'
	 'CS306' :'COMPUTER NETWORKSCS308 SOFTWARE ENGINEERING AND PROJECTMANAGEMENT'
	 'HS300' :'PRINCIPLES OF MANAGEMENT'
	 'CS368' :'WEB TECHNOLOGIES'
	 'CS332' :'MICROPROCESSOR LAB'
	 'CS334' :'NETWORK PROGRAMMING LAB'
	 'CS352' :'COMPREHENSIVE EXAM'
	 'EC302' :'DIGITAL COMMUNICATION'
	 'EC304' :'VLSI'
	 'EC306' :'ANTENNA & WAVE PROPAGATION'
	 'EC308' :'EMBEDDED SYSTEMS'
	 'EC312' :'OBJECT ORIENTED PROGRAMMING'
	 'EC366' :'REAL TIME OPERATING SYSTEMS'
	 'EC332' :'COMMUNICATION ENGG LAB (ANALOG & DIGITAL)'
	 'EC334' :'MICROCONTROLLER LAB'
	 'EC352' :'COMPREHENSIVE EXAM'
	 'EC370' :'DIGITAL IMAGE PROCESSING'
	 'EE302' :'ELECTROMAGNETICS'
	 'EE304' :'ADVANCED CONTROL THEORY'
	 'EE306' :'POWER SYSTEM ANALYSIS'
	 'EE308' :'ELECTRIC DRIVES'
	 'HS300' :'PRINCIPLES OF MANAGEMENT'
	 'EE372' :'BIOMEDICAL INSTRUMENTATION'
	 'EE332' :'SYSTEMS AND CONTROL LAB'
	 'EE334' :'POWER ELECTRONICS & DRIVES LAB'
	 'EE352' :'COMPREHENSIVE EXAM'
	 'EE368' :'SOFT COMPUTING' 
	''')
	file = open ('pec.csv')
	file_read = csv.reader(file)
	file_data = list(file_read)
	listToStr = ' '.join([str(elem) for elem in file_data])
	new_stra = listToStr.replace(","," ")
	new_strb = new_stra.replace("n"," ")
	new_strc = new_strb.replace("'"," ")
	new_strd = new_strc.replace("["," ")
	new_stre = new_strd.replace("]"," ")
	b=[]
	b=new_stre.split(" ")
	for j in range(0,len(b)):
		if ('CE302(F)' == b[j]):
			fail = fail+1
		if ('CE304(F)' == b[j]):
			fail1 = fail1+1
		if ('CE306(F)' == b[j]):
			fail2 = fail2+1
		if ('CE308(F)' == b[j]):
			fail3 = fail3+1
		if ('HS300(F)' == b[j]):
			fail4 = fail4+1
		if ('CE374(F)' == b[j]):
			fail5 = fail5+1
		if ('CE332(F)' == b[j]):
			fail6 = fail6+1
		if ('CE334(F)' == b[j]):
			fail7 = fail7+1
		if ('CE352(F)' == b[j]):
			fail8 = fail8+1
		if ('CE362(F)' == b[j]):
			fail9 = fail9+1
		if ('CE366(F)' == b[j]):
			fail10 = fail10+1
		if ('CS302(F)' == b[j]):
			fail11 = fail11+1
		if ('CS304(F)' == b[j]):
			fail12 = fail12+1
		if ('CS306(F)' == b[j]):
			fail13 = fail13+1
		if ('CS368(F)' == b[j]):
			fail14 = fail14+1
		if ('CS332(F)' == b[j]):
			fail15 = fail15+1
		if ('CS334(F)' == b[j]):
			fail16 = fail16+1
		if ('CS352(F)' == b[j]):
			fail17 = fail17+1
		if ('EC302(F)' == b[j]):
			fail18 = fail18+1
		if ('EC304(F)' == b[j]):
			fail19 = fail19+1
		if ('EC306(F)' == b[j]):
			fail20 = fail20+1
		if ('EC308(F)' == b[j]):
			fail21 = fail21+1
		if ('EC312(F)' == b[j]):
			fail22 = fail22+1
		if ('EC366(F)' == b[j]):
			fai23 = fail23+1
		if ('EC332(F)' == b[j]):
			fail24 = fail24+1
		if ('EC334(F)' == b[j]):
			fail25 = fail25+1
		if ('EC352(F)' == b[j]):
			fail26 = fail26+1
		if ('EC370(F)' == b[j]):
			fail27 = fail27+1
		if ('EE302(F)' == b[j]):
			fail28 = fail28+1
		if ('EE304(F)' == b[j]):
			fail29 = fail29+1
		if ('EE306(F)' == b[j]):
			fail30 = fail30+1
		if ('EE308(F)' == b[j]):
			fail31 = fail31+1
		if ('EE372(F)' == b[j]):
			fail32 = fail32+1
		if ('EE332(F)' == b[j]):
			fail33 = fail33+1
		if ('EE334(F)' == b[j]):
			fail34 = fail34+1
		if ('EE352(F)' == b[j]):
			fail35 = fail35+1
		if ('EE368(F)' == b[j]):
			fail36 = fail36+1

		if ('CE302(Absent)' == b[j] or 'CE302(FE)' == b[j]) or 'CE302(I)' == b[j]:
			at = at + 1
		if ('CE304(Absent)' == b[j] or 'CE304(FE)' == b[j]) or 'CE304(I)' == b[j]:
			at1 = at1 + 1
		if ('CE306(Absent)' == b[j] or 'CE306(FE)' == b[j]) or 'CE306(I)' == b[j]:
			at2 = at2 + 1
		if ('CE308(Absent)' == b[j] or 'CE308(FE)' == b[j]) or 'CE308(I)' == b[j]:
			at3 = at3 + 1
		if ('HS300(Absent)' == b[j] or 'HS300(FE)' == b[j]) or 'HS300(I)' == b[j]:
			at4 = at4 + 1
		if ('CE374(Absent)' == b[j] or 'CE374(FE)' == b[j]) or 'CE374(I)' == b[j]:
			at5 = at5 + 1
		if ('CE332(Absent)' == b[j] or 'CE332(FE)' == b[j]) or 'CE332(I)' == b[j]:
			at6 = at6 + 1
		if ('CE334(Absent)' == b[j] or 'CE334(FE)' == b[j]) or 'CE334(I)' == b[j]:
			at7 = at7 + 1
		if ('CE352(Absent)' == b[j] or 'CE352(FE)' == b[j]) or 'CE352(I)' == b[j]:
			at8 = at8 + 1
		if ('CE362(Absent)' == b[j] or 'CE362(FE)' == b[j]) or 'CE362(I)' == b[j]:
			at9 = at9 + 1
		if ('CE366(Absent)' == b[j] or 'CE366(FE)' == b[j]) or 'CE366(I)' == b[j]:
			at10 = at10 + 1
		if ('CS302(Absent)' == b[j] or 'CS302(FE)' == b[j]) or 'CS302(I)' == b[j]:
			at11 = at11 + 1
		if ('CS304(Absent)' == b[j] or 'CS304(FE)' == b[j]) or 'CS304(I)' == b[j]:
			at12 = at12 + 1
		if ('CS306(Absent)' == b[j] or 'CS306(FE)' == b[j]) or 'CS306(I)' == b[j]:
			at13 = at13 + 1
		if ('CS368(Absent)' == b[j] or 'CS368(FE)' == b[j]) or 'CS368(I)' == b[j]:
			at14 = at14 + 1
		if ('CS332(Absent)' == b[j] or 'CS332(FE)' == b[j]) or 'CS332(I)' == b[j]:
			at15 = at15 + 1
		if ('CS334(Absent)' == b[j] or 'CS334(FE)' == b[j]) or 'CS334(I)' == b[j]:
			at16 = at16 + 1
		if ('CS352(Absent)' == b[j] or 'CS352(FE)' == b[j]) or 'CS352(I)' == b[j]:
			at17 = at17 + 1
		if ('EC302(Absent)' == b[j] or 'EC302(FE)' == b[j]) or 'EC302(I)' == b[j]:
			at18 = at18 + 1
		if ('EC304(Absent)' == b[j] or 'EC304(FE)' == b[j]) or 'EC304(I)' == b[j]:
			at19 = at19+ 1
		if ('EC306(Absent)' == b[j] or 'EC306(FE)' == b[j]) or 'EC306(I)' == b[j]:
			at20 = at20 + 1
		if ('EC308(Absent)' == b[j] or 'EC308(FE)' == b[j]) or 'EC308(I)' == b[j]:
			at21 = at21 + 1
		if ('EC312(Absent)' == b[j] or 'EC312(FE)' == b[j]) or 'EC312(I)' == b[j]:
			at22 = at22 + 1
		if ('EC366(Absent)' == b[j] or 'EC366(FE)' == b[j]) or 'EC366(I)' == b[j]:
			at23 = at23 + 1
		if ('EC332(Absent)' == b[j] or 'EC332(FE)' == b[j]) or 'EC332(I)' == b[j]:
			at24 = at24 + 1
		if ('EC334(Absent)' == b[j] or 'EC334(FE)' == b[j]) or 'EC334(I)' == b[j]:
			at25 = at25 + 1
		if ('EC352(Absent)' == b[j] or 'EC352(FE)' == b[j]) or 'EC352(I)' == b[j]:
			at26 = at26 + 1
		if ('EC370(Absent)' == b[j] or 'EC370(FE)' == b[j]) or 'EC370(I)' == b[j]:
			at27 = at27 + 1
		if ('EE302(Absent)' == b[j] or 'EE302(FE)' == b[j]) or 'EE302(I)' == b[j]:
			at28 = at28 + 1
		if ('EE304(Absent)' == b[j] or 'EE304(FE)' == b[j]) or 'EE304(I)' == b[j]:
			at29 = at29 + 1
		if ('EE306(Absent)' == b[j] or 'EE306(FE)' == b[j]) or 'EE306(I)' == b[j]:
			at30 = at30 + 1
		if ('EE308(Absent)' == b[j] or 'EE308(FE)' == b[j]) or 'EE308(I)' == b[j]:
			at31 = at31 + 1
		if ('EE372(Absent)' == b[j] or 'EE372(FE)' == b[j]) or 'EE372(I)' == b[j]:
			at32 = at32 + 1
		if ('EE332(Absent)' == b[j] or 'EE332(FE)' == b[j]) or 'EE332(I)' == b[j]:
			at33 = at33 + 1
		if ('EE334(Absent)' == b[j] or 'EE334(FE)' == b[j]) or 'EE334(I)' == b[j]:
			at34 = at34 + 1
		if ('EE352(Absent)' == b[j] or 'EE352(FE)' == b[j]) or 'EE352(I)' == b[j]:
			at35 = at35 + 1
		if ('EE368(Absent)' == b[j] or 'EE368(FE)' == b[j]) or 'EE368(I)' == b[j]:
			at36 = at36 + 1
		





	new_str = listToStr.replace("(A)"," ")
	new_str1 = new_str.replace("(A+)"," ")
	new_str2 = new_str1.replace("(B)"," ")
	new_str3 = new_str2.replace("(B+)"," ")
	new_str4 = new_str3.replace("(C)"," ")
	new_str5 = new_str4.replace("(P)"," ")
	new_str6 = new_str5.replace("(F)"," ")
	new_str7 = new_str6.replace("(Absent)"," ")
	new_str8 = new_str7.replace("(O)"," ")
	new_str9 = new_str8.replace("(FE)"," ")
	new_str10 = new_str9.replace("(I)"," ")
	final_str = new_str10.replace("n"," ")
	a=[]
	a=final_str.split(" ")
	for i in range(0,len(a)):
		if('CE302'==a[i]):
			count=count+1
		if('CE304'==a[i]):
			count1=count1+1
		if('CE306'==a[i]):
			count2=count2+1
		if('CE308'==a[i]):
			count3=count3+1
		if('HS300'==a[i]):
			count4=count4+1
		if('CE374'==a[i]):
			count5=count5+1
		if('CE332'==a[i]):
			count6=count6+1
		if('CE334'==a[i]):
			count7=count7+1
		if('CE352'==a[i]):
			count8=count8+1
		if('CE362'==a[i]):
			count9=count9+1
		if('CE366'==a[i]):
			count10=count10+1
		if('CS302'==a[i]):
			count11=count11+1
		if('CS304'==a[i]):
			count12=count12+1
		if('CS306'==a[i]):
			count13=count13+1
		if('CS368'==a[i]):
			count14=count14+1
		if('CS332'==a[i]):
			count15=count15+1
		if('CS334'==a[i]):
			count16=count16+1
		if('CS352'==a[i]):
			count17=count17+1
		if('EC302'==a[i]):
			count18=count18+1
		if('EC304'==a[i]):
			count19=count19+1
		if('EC306'==a[i]):
			count20=count20+1
		if('EC308'==a[i]):
			count21=count21+1
		if('EC312'==a[i]):
			count22=count22+1
		if('EC366'==a[i]):
			count23=count23+1
		if('EC332'==a[i]):
			count24=count24+1
		if('EC334'==a[i]):
			count25=count25+1
		if('EC352'==a[i]):
			count26=count26+1
		if('EC370'==a[i]):
			count27=count27+1
		if('EE302'==a[i]):
			count28=count28+1
		if('EE304'==a[i]):
			count29=count29+1
		if('EE306'==a[i]):
			count30=count30+1
		if('EE308'==a[i]):
			count31=count31+1
		if('EE372'==a[i]):
			count32=count32+1
		if('EE332'==a[i]):
			count33=count33+1
		if('EE334'==a[i]):
			count34=count34+1
		if('EE352'==a[i]):
			count35=count35+1
		if('EE368'==a[i]):
			count36=count36+1

	CE302 = count - 1
	CE304 = count1 - 1
	CE306 = count2 - 1
	CE308 = count3 - 1
	HS300 = count4 - 1
	CE374 = count5 - 1
	CE332 = count6 - 1
	CE334 = count7 - 1
	CE352 = count8 - 1
	CE362 = count9 - 1
	CE366 = count10 - 1
	CS302 = count11 - 1
	CS304 = count12 - 1
	CS306 = count13 - 1
	CS368 = count14 - 1
	CS332 = count15 - 1
	CS334 = count16 - 1
	CS352 = count17 - 1
	EC302 = count18 - 1
	EC304 = count19 - 1
	EC306 = count20 - 1
	EC308 = count21 - 1
	EC312 = count22 - 1
	EC366 = count23 - 1
	EC332 = count24 - 1
	EC334 = count25 - 1
	EC352 = count26 - 1
	EC370 = count27 - 1
	EE302 = count28 - 1
	EE304 = count29 - 1
	EE306 = count30 - 1
	EE308 = count31 - 1
	EE372 = count32 - 1
	EE332 = count33 - 1
	EE334 = count34 - 1
	EE352 = count35 - 1
	EE368 = count36 - 1


	check = True
	while check :

		inp = input('\n\n\tEnter the subject (eg. EE368, CS352, CE362 ..\n\n\t')

		user_inp = inp.upper()

		if user_inp == 'CE302' :
			print('\n\tAnalysis of DESIGN OF HYDRAULIC STRUCTURES ')
			print(f'\n\tNumber of students who passed = {count-(fail+at)}')
			print(f'\n\tNumber of students who failed = {fail}')
			print(f'\n\tNumber of students who couldnt attend = {at}')
			print(f'\n\tPass percentage = {((count-(fail+at))/count) * 100 }')
		if user_inp == 'CE304' :
			print('\n\tAnalysis of DESIGN OF CONCRETE STRUCTURES II ')
			print(f'\n\tNumber of students who passed = {count1-(fail1+at1)}')
			print(f'\n\tNumber of students who failed = {fail1}')
			print(f'\n\tNumber of students who couldnt attend = {at1}')
			print(f'\n\tPass percentage = {((count1-(fail1+at1))/count1) * 100 }')
		if user_inp == 'CE306' :
			print('\n\tAnalysis of COMPUTER PROGRAMMING AND COMPUTATIONAL TECHNIQUES ')
			print(f'\n\tNumber of students who passed = {count2-(fail2+at2)}')
			print(f'\n\tNumber of students who failed = {fail2}')
			print(f'\n\tNumber of students who couldnt attend = {at2}')
			print(f'\n\tPass percentage = {((count2-(fail2+at2))/count2) * 100 }')
		if user_inp == 'CE308' :
			print('\n\tAnalysis of TRANSPORTATION ENGINEERING I ')
			print(f'\n\tNumber of students who passed = {count3-(fail3+at3)}')
			print(f'\n\tNumber of students who failed = {fail3}')
			print(f'\n\tNumber of students who couldnt attend = {at3}')
			print(f'\n\tPass percentage = {((count3-(fail3+at3))/count3) * 100 }')
		if user_inp == 'HS300' :
			print('\n\tAnalysis of PRINCIPLES OF MANAGEMENT ')
			print(f'\n\tNumber of students who passed = {count4-(fail4+at4)}')
			print(f'\n\tNumber of students who failed = {fail4}')
			print(f'\n\tNumber of students who couldnt attend = {at4}')
			print(f'\n\tPass percentage = {((count4-(fail4+at4))/count4) * 100 }')
		if user_inp == 'CE374' :
			print('\n\tAnalysis of AIR QUALITY MANAGEMENT ')
			print(f'\n\tNumber of students who passed = {count5-(fail5+at5)}')
			print(f'\n\tNumber of students who failed = {fail5}')
			print(f'\n\tNumber of students who couldnt attend = {at5}')
			print(f'\n\tPass percentage = {((count5-(fail5+at5))/count5) * 100 }')
		if user_inp == 'CE332' :
			print('\n\tAnalysis of TRANSPORTATION ENGINEERING LAB ')
			print(f'\n\tNumber of students who passed = {count6-(fail6+at6)}')
			print(f'\n\tNumber of students who failed = {fail6}')
			print(f'\n\tNumber of students who couldnt attend = {at6}')
			print(f'\n\tPass percentage = {((count6-(fail6+at6))/count6) * 100 }')
		if user_inp == 'CE334' :
			print('\n\tAnalysis of COMPUTER AIDED CIVIL ENGINEERING LAB ')
			print(f'\n\tNumber of students who passed = {count7-(fail7+at7)}')
			print(f'\n\tNumber of students who failed = {fail7}')
			print(f'\n\tNumber of students who couldnt attend = {at7}')
			print(f'\n\tPass percentage = {((count7-(fail7+at7))/count7) * 100 }')
		if user_inp == 'CE352'  :
			print('\n\tAnalysis of COMPREHENSIVE EXAM ')
			print(f'\n\tNumber of students who passed = {count8-(fail8+at8)}')
			print(f'\n\tNumber of students who failed = {fail8}')
			print(f'\n\tNumber of students who couldnt attend = {at8}')
			print(f'\n\tPass percentage = {((count8-(fail8+at8))/count8) * 100 }')
		if user_inp == 'CE362'  :
			print('\n\tAnalysis of GROUND IMPROVEMENT TECHNIQUES ')
			print(f'\n\tNumber of students who passed = {count9-(fail9+at9)}')
			print(f'\n\tNumber of students who failed = {fail9}')
			print(f'\n\tNumber of students who couldnt attend = {at9}')
			print(f'\n\tPass percentage = {((count9-(fail9+at9))/count9) * 100 }')
		if user_inp == 'CE366'  :
			print('\n\tAnalysis of TRAFFIC ENGINEERING AND MANAGEMENT ')
			print(f'\n\tNumber of students who passed = {count10-(fail10+at10)}')
			print(f'\n\tNumber of students who failed = {fail10}')
			print(f'\n\tNumber of students who couldnt attend = {at10}')
			print(f'\n\tPass percentage = {((count10-(fail10+at10))/count10) * 100 }')
		if user_inp == 'CS302' :
			print('\n\tAnalysis of DESIGN AND ANALYSIS OF ALGORITHMS ')
			print(f'\n\tNumber of students who passed = {count11-(fail11+at11)}')
			print(f'\n\tNumber of students who failed = {fail11}')
			print(f'\n\tNumber of students who couldnt attend = {at11}')
			print(f'\n\tPass percentage = {((count11-(fail11+at11))/count11) * 100 }')
		if user_inp == 'CS304' :
			print('\n\tAnalysis of COMPILER DESIGN ')
			print(f'\n\tNumber of students who passed = {count12-(fail12+at12)}')
			print(f'\n\tNumber of students who failed = {fail12}')
			print(f'\n\tNumber of students who couldnt attend = {at12}')
			print(f'\n\tPass percentage = {((count12-(fail12+at12))/count12) * 100 }')
		if user_inp == 'CS306'  :
			print('\n\tAnalysis of COMPUTER NETWORKSCS308 SOFTWARE ENGINEERING AND PROJECTMANAGEMENT ')
			print(f'\n\tNumber of students who passed = {count13-(fail13+at13)}')
			print(f'\n\tNumber of students who failed = {fail13}')
			print(f'\n\tNumber of students who couldnt attend = {at13}')
			print(f'\n\tPass percentage = {((count13-(fail13+at13))/count13) * 100 }')
		if user_inp == 'CS368'  :
			print('\n\tAnalysis of WEB TECHNOLOGIES  ')
			print(f'\n\tNumber of students who passed = {count14-(fail14+at14)}')
			print(f'\n\tNumber of students who failed = {fail14}')
			print(f'\n\tNumber of students who couldnt attend = {at14}')
			print(f'\n\tPass percentage = {((count14-(fail14+at14))/count14) * 100 }')
		if user_inp == 'CS332' :
			print('\n\tAnalysis of MICROPROCESSOR LAB ')
			print(f'\n\tNumber of students who passed = {count15-(fail15+at15)}')
			print(f'\n\tNumber of students who failed = {fail15}')
			print(f'\n\tNumber of students who couldnt attend = {at15}')
			print(f'\n\tPass percentage = {((count15-(fail15+at15))/count15) * 100 }')
		if user_inp == 'CS334'  :
			print('\n\tAnalysis of NETWORK PROGRAMMING LAB')
			print(f'\n\tNumber of students who passed = {count16-(fail16+at16)}')
			print(f'\n\tNumber of students who failed = {fail16}')
			print(f'\n\tNumber of students who couldnt attend = {at16}')
			print(f'\n\tPass percentage = {((count16-(fail16+at16))/count16) * 100 }')
		if user_inp == 'CS352'  :
			print('\n\tAnalysis of COMPREHENSIVE EXAM ')
			print(f'\n\tNumber of students who passed = {count17-(fail17+at17)}')
			print(f'\n\tNumber of students who failed = {fail17}')
			print(f'\n\tNumber of students who couldnt attend = {at17}')
			print(f'\n\tPass percentage = {((count17-(fail17+at17))/count17) * 100 }')
		if user_inp == 'EC302' :
			print('\n\tAnalysis of DIGITAL COMMUNICATION ')
			print(f'\n\tNumber of students who passed = {count18-(fail18+at18)}')
			print(f'\n\tNumber of students who failed = {fail18}')
			print(f'\n\tNumber of students who couldnt attend = {at18}')
			print(f'\n\tPass percentage = {((count18-(fail18+at18))/count18) * 100 }')
		if user_inp == 'EC304' :
			print('\n\tAnalysis of VLSI ')
			print(f'\n\tNumber of students who passed = {count19-(fail19+at19)}')
			print(f'\n\tNumber of students who failed = {fail19}')
			print(f'\n\tNumber of students who couldnt attend = {at19}')
			print(f'\n\tPass percentage = {((count19-(fail19+at19))/count19) * 100 }')
		if user_inp == 'EC306'  :
			print('\n\tAnalysis of ANTENNA & WAVE PROPAGATIONS ')
			print(f'\n\tNumber of students who passed = {count20-(fail20+at20)}')
			print(f'\n\tNumber of students who failed = {fail20}')
			print(f'\n\tNumber of students who couldnt attend = {at20}')
			print(f'\n\tPass percentage = {((count20-(fail20+at20))/count20) * 100 }')
		if user_inp == 'EC308' :
			print('\n\tAnalysis of EMBEDDED SYSTEMS ')
			print(f'\n\tNumber of students who passed = {count21-(fail21+at21)}')
			print(f'\n\tNumber of students who failed = {fail21}')
			print(f'\n\tNumber of students who couldnt attend = {at21}')
			print(f'\n\tPass percentage = {((count21-(fail21+at21))/count21) * 100 }')
		if user_inp == 'EC312' :
			print('\n\tAnalysis of OBJECT ORIENTED PROGRAMMING')
			print(f'\n\tNumber of students who passed = {count22-(fail22+at22)}')
			print(f'\n\tNumber of students who failed = {fail22}')
			print(f'\n\tNumber of students who couldnt attend = {at22}')
			print(f'\n\tPass percentage = {((count22-(fail22+at22))/count22) * 100 }')
		if user_inp == 'EC366' :
			print('\n\tAnalysis of REAL TIME OPERATING SYSTEMS')
			print(f'\n\tNumber of students who passed = {count23-(fail23+at23)}')
			print(f'\n\tNumber of students who failed = {fail23}')
			print(f'\n\tNumber of students who couldnt attend = {at23}')
			print(f'\n\tPass percentage = {((count23-(fail23+at23))/count23) * 100 }')
		if user_inp == 'EC332' :
			print('\n\tAnalysis of COMMUNICATION ENGG LAB (ANALOG & DIGITAL) ')
			print(f'\n\tNumber of students who passed = {count24-(fail24+at24)}')
			print(f'\n\tNumber of students who failed = {fail24}')
			print(f'\n\tNumber of students who couldnt attend = {at24}')
			print(f'\n\tPass percentage = {((count24-(fail24+at24))/count24) * 100 }')
		if user_inp == 'EC334' :
			print('\n\tAnalysis of MICROCONTROLLER LAB ')
			print(f'\n\tNumber of students who passed = {count25-(fail25+at25)}')
			print(f'\n\tNumber of students who failed = {fail25}')
			print(f'\n\tNumber of students who couldnt attend = {at25}')
			print(f'\n\tPass percentage = {((count25-(fail25+at25))/count25) * 100 }')
		if user_inp == 'EC352' :
			print('\n\tAnalysis of COMPREHENSIVE EXAM ')
			print(f'\n\tNumber of students who passed = {count26-(fail26+at26)}')
			print(f'\n\tNumber of students who failed = {fail26}')
			print(f'\n\tNumber of students who couldnt attend = {at26}')
			print(f'\n\tPass percentage = {((count26-(fail26+at26))/count26) * 100 }')
		if user_inp == 'EC370' :
			print('\n\tAnalysis of DIGITAL IMAGE PROCESSING ')
			print(f'\n\tNumber of students who passed = {count27-(fail27+at27)}')
			print(f'\n\tNumber of students who failed = {fail27}')
			print(f'\n\tNumber of students who couldnt attend = {at27}')
			print(f'\n\tPass percentage = {((count27-(fail27+at27))/count27) * 100 }')
		if user_inp == 'EE302':
			print('\n\tAnalysis of ELECTROMAGNETICS ')
			print(f'\n\tNumber of students who passed = {count28-(fail28+at28)}')
			print(f'\n\tNumber of students who failed = {fail28}')
			print(f'\n\tNumber of students who couldnt attend = {at28}')
			print(f'\n\tPass percentage = {((count28-(fail28+at28))/count28) * 100 }')
		if user_inp == 'EE304'  :
			print('\n\tAnalysis of ADVANCED CONTROL THEORY ')
			print(f'\n\tNumber of students who passed = {count29-(fail29+at29)}')
			print(f'\n\tNumber of students who failed = {fail29}')
			print(f'\n\tNumber of students who couldnt attend = {at29}')
			print(f'\n\tPass percentage = {((count29-(fail29+at29))/count29) * 100 }')
		if user_inp == 'EE306' :
			print('\n\tAnalysis of POWER SYSTEM ANALYSIS ')
			print(f'\n\tNumber of students who passed = {count30-(fail30+at30)}')
			print(f'\n\tNumber of students who failed = {fail30}')
			print(f'\n\tNumber of students who couldnt attend = {at30}')
			print(f'\n\tPass percentage = {((count30-(fail30+at30))/count30) * 100 }')
		if user_inp == 'EE308' :
			print('\n\tAnalysis of ELECTRIC DRIVES ')
			print(f'\n\tNumber of students who passed = {count31-(fail31+at31)}')
			print(f'\n\tNumber of students who failed = {fail31}')
			print(f'\n\tNumber of students who couldnt attend = {at31}')
			print(f'\n\tPass percentage = {((count31-(fail31+at31))/count31) * 100 }')
		if user_inp == 'EE372' :
			print('\n\tAnalysis of BIOMEDICAL INSTRUMENTATION  ')
			print(f'\n\tNumber of students who passed = {count32-(fail32+at32)}')
			print(f'\n\tNumber of students who failed = {fail32}')
			print(f'\n\tNumber of students who couldnt attend = {at32}')
			print(f'\n\tPass percentage = {((count32-(fail32+at32))/count32) * 100 }')
		if user_inp == 'EE332'  :
			print('\n\tAnalysis of SYSTEMS AND CONTROL LAB ')
			print(f'\n\tNumber of students who passed = {count33-(fail33+at33)}')
			print(f'\n\tNumber of students who failed = {fail33}')
			print(f'\n\tNumber of students who couldnt attend = {at33}')
			print(f'\n\tPass percentage = {((count33-(fail33+at33))/count33) * 100 }')
		if user_inp == 'EE334' :
			print('\n\tAnalysis of POWER ELECTRONICS & DRIVES ')
			print(f'\n\tNumber of students who passed = {count34-(fail34+at34)}')
			print(f'\n\tNumber of students who failed = {fail34}')
			print(f'\n\tNumber of students who couldnt attend = {at34}')
			print(f'\n\tPass percentage = {((count34-(fail34+at34))/count34) * 100 }')
		if user_inp == 'EE352' :
			print('\n\tAnalysis of COMPREHENSIVE EXAM ')
			print(f'\n\tNumber of students who passed = {count35-(fail35+at35)}')
			print(f'\n\tNumber of students who failed = {fail35}')
			print(f'\n\tNumber of students who couldnt attend = {at35}')
			print(f'\n\tPass percentage = {((count35-(fail35+at35))/count35) * 100 }')
		if user_inp == 'EE368' :
			print('\n\tAnalysis of SOFT COMPUTING ')
			print(f'\n\tNumber of students who passed = {count36-(fail36+at36)}')
			print(f'\n\tNumber of students who failed = {fail36}')
			print(f'\n\tNumber of students who couldnt attend = {at36}')
			print(f'\n\tPass percentage = {((count36-(fail35+at36))/count36) * 100 }')


		again = input('\n\n\n\tWant to check again (y/n)? : ')
		
		if again == 'y' :
			check = True
		else :
			check = False
