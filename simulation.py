import random

def generateTBA(rda):
	if rda == 0:
		return 4
	
	elif rda >= 1 and rda <= 25:
	    return 1
	
	elif rda >= 26 and rda <= 65:
		return 2

	elif rda >= 66 and rda <= 85:
		return 3

	else:
		return 4

def ward_1_service_time(rds):
	if rds == 0:
		return 6
	
	elif rds >= 1 and rds <= 20:
	    return 4
	
	elif rds >= 21 and rds <= 45:
		return 5

	elif rds >= 46 and rds <= 75:
		return 3

	else:
		return 6

def ward_2_service_time(rds):
	if rds == 0:
		return 5
	
	elif rds >= 1 and rds <= 30:
	    return 7
	
	elif rds >= 31 and rds <= 58:
		return 6

	elif rds >= 59 and rds <= 83:
		return 8

	else:
		return 5

def ward_3_service_time(rds):
	if rds == 0:
		return 9
	
	elif rds >= 1 and rds <= 35:
	    return 7
	
	elif rds >= 36 and rds <= 60:
		return 10

	elif rds >= 61 and rds <= 80:
		return 8

	else:
		return 9


cta = 0
rds = round(random.uniform(0,100))

ward_1_tsb = 0
ward_1_st = ward_1_service_time(rds)
ward_1_tse = ward_1_tsb + ward_1_st
ward_1_tst = ward_1_st



ward_2_tse = -1
ward_3_tse = -1

ward_2_tst = 0
ward_3_tst = 0

total_time_queue = 0

for i in range(2,101):
	rda = round(random.uniform(0,100))
	cta = cta + generateTBA(rda)
	rds = round(random.uniform(0,100))

	if cta >= ward_1_tse:
		ward_1_tsb = cta
		ward_1_st = ward_1_service_time(rds)
		ward_1_tse = ward_1_tsb + ward_1_st
		ward_1_tst = ward_1_tst + ward_1_st

	else:
		if cta >= ward_2_tse or ward_2_tse == -1:
			ward_2_tsb = cta
			ward_2_st = ward_2_service_time(rds)
			ward_2_tse = ward_2_tsb + ward_2_st
			ward_2_tst = ward_2_tst + ward_2_st
		else:
			if cta >= ward_3_tse or ward_3_tse == -1:
				ward_3_tsb = cta
				ward_3_st = ward_3_service_time(rds)
				ward_3_tse = ward_3_tsb + ward_3_st
				ward_3_tst = ward_3_tst + ward_3_st

			else:
			    w = min(ward_1_tse,ward_2_tse,ward_3_tse)
                
			    if w == ward_1_tse:
			    	total_time_queue = total_time_queue + ward_1_tse - cta 
			    	ward_1_tsb = ward_1_tse
			    	ward_1_st = ward_1_service_time(rds)
			    	ward_1_tse = ward_1_tsb + ward_1_st
			    	ward_1_tst = ward_1_tst + ward_1_st

			    elif w == ward_2_tse:
			    	total_time_queue = total_time_queue + ward_2_tse - cta
			    	ward_2_tsb = ward_2_tse
			    	ward_2_st = ward_2_service_time(rds)
			    	ward_2_tse = ward_2_tsb + ward_2_st
			    	ward_2_tst = ward_2_tst + ward_2_st

			    else:
			    	total_time_queue = total_time_queue + ward_3_tse - cta
			    	ward_3_tsb = ward_3_tse
			    	ward_3_st = ward_3_service_time(rds)
			    	ward_3_tse = ward_3_tsb + ward_3_st
			    	ward_3_tst = ward_3_tst + ward_3_st


total_time_system = ward_1_tst + ward_2_tst + ward_3_tst + total_time_queue

avg_time_system = total_time_system / 100

avg_delay = total_time_queue / 100

print("Total time in queue: " + str(total_time_queue))
print("Average delay: " + str(avg_delay))
print("Total time in system: " + str(total_time_system))
print("Average time in system: " + str(avg_time_system))


