while True:

    print("1.Check the Train Schedules.")
    print("2.Buy the ticket.")
    print("3.Print the E-Ticket.")
    print("4.Exit")
    opt=int(input("Choose the option :"))

    if opt==4:
        print("Thank for inquiry.")
        break

    if opt==1:
        print("The Train Schedules are below :")
        print("TRAIN NUMBER	TRAIN NAME	                                TRAIN TYPE	RUN DAYS	        DEPARTURE TIME(HRS)	ARRIVAL TIME(HRS)")
        print("12267	        MUMBAI CENTRAL - AHMEDABAD AC DURONTO EXP	DURONTO	    M,T,W,T,F,S,S	    23:25	            05:55")
        print("12268	        AHMEDABAD - MUMBAI CENT AC DURONTO EXP	    DURONTO	    M,T,W,T,F,S,S	    23:40	            06:00")
        print("22201         	KOLKATA SEALDAH - PURI DURONTO EXPRESS	    DURONTO	    M,W,F	            20:00	            04:00")
        print("22204	        SECUNDERABAD-VISAKHAPATNAM AC DURONTO EXP	DURONTO	    M,W,S	            20:15	            06:35")
        print("22206	        MADURAI-CHENNAI CENTRAL AC DURONTO EXP	    DURONTO	    TUE,THU	            22:40	            07:20")
        print("12426	        JAMMU TAWI-NEW DELHI RAJDHANI EXPRESS	    RAJDHANI	M,T,W,T,F,S,S	    19:40	            05:05")
        print("12430	        NEW DELHI - LUCKNOW AC SF EXPRESS	        RAJDHANI	M,T,F,S	            20:50            	06:40")
        print("12437        	SECUNDERABAD-HAZRAT NIZAMUDDIN EXP	        RAJDHANI	WED	                12:45	            10:25")
        print("12951	        MUMBAI CENTRAL - NEW DELHI EXP          	RAJDHANI	M,T,W,T,F,S,S	    16:35	            08:35")
        print("12953	        MUMBAI CENT HAZRAT NIZAMUDDIN KRANTI EXP	RAJDHANI	M,T,W,T,F,S,S	    17:40	            10:55")
        print()
    elif opt==2:
        print("Enter your detials.")
        name=str(input("Enter your name :"))
        trainno=int(input("Enter the train number :"))
        day=str(input("Enter the day :"))
        seat=int(input("Enter the no of seat you :"))
        print()

    elif opt==3:
        print("Your E ticket is below : ")
        print("NAME                TRAINNO    DAY   SEAT")
        print("{}      {}     {}      {}".format(name, trainno, day, seat))
        print()

    else:
        print("Choose the appropriate option.")