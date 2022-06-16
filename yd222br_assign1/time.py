Sec1=int(input(" Give a number of seconds: "))
Hours=Sec1//3600
Mins=Sec1//60-Hours*60
Sec2=Sec1-Hours*3600-Mins*60
print("This corresponds to:"+ str(Hours)+" hours," +str(Mins)+" minutes and " +str(Sec2)+" seconds.")
print(f"This corresponds to: {Hours} hours, {Mins} minutes and {Sec2} seconds.")
