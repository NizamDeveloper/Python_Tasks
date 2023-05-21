def solve(n):
    if n<4:
        return str(2**(n-1))+'/'+str(2**n)
    # Asuming the calculation day starting from 6th day and taking last 5 days values of missing GC as constant and doing recursion 
    # as per the results of 1-10 days , i have created these constants 
    # calculated results for attending the class as per the rules
    # {1:2,2:4,3:8,4:15,5:29,6:56,7:108,8:208,9:401,10:773}
    # manual results for missing Graduation ceremony 
    #{1:1,2:2,3:4,4:7,:5:14,6:27,7:52,8:100,9:100,10:193}
    
    count_4th_day_before_now  = 1
    count_3rd_day_before_now  = 2
    count_2nd_day_before_now  = 4
    count_1stday_before_now   = 7 
    count_missing_GC = 14
    
    counter1_attndc1 = 0
    counter1_attndc2 = 1
    counter1_attndc3 = 1
    counter1_attndc4 = 2
    
    counter = 2
    valid_attendance_count = 29
    if n==4:
        return str(15)+'/'+str(count_1stday_before_now)
    if n==5:
        return str(count_missing_GC)+'/'+str(valid_attendance_count)
    for i in range(6,n+1):
        count_4th_day_before_now = count_3rd_day_before_now
        count_3rd_day_before_now = count_2nd_day_before_now
        count_2nd_day_before_now = count_1stday_before_now
        count_1stday_before_now = count_missing_GC
        
        count_missing_GC = count_1stday_before_now+count_2nd_day_before_now+count_3rd_day_before_now+count_4th_day_before_now

        
        valid_attendance_count = ( valid_attendance_count- counter)*2 + counter   
        counter = counter1_attndc4+counter1_attndc3+counter1_attndc2+counter1_attndc1
        counter1_attndc1 = counter1_attndc2
        counter1_attndc2 = counter1_attndc3
        counter1_attndc3 = counter1_attndc4
        counter1_attndc4 = counter
        


    return str(count_missing_GC)+'/'+str(valid_attendance_count)


for i in range(1,11):
    #printing the results for each day 
    print("The results for day/s {}:".format(i),solve(i))


