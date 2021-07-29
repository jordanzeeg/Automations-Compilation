#pip install pygsheets
import gspread
import send_email
import datetime
import time #put this in the main program at the end

start_time = time.time() #put this in the main program at the end
gc = gspread.service_account(filename= 'credentials.json')
today = datetime.datetime.today().strftime('%m/%d/%y')
#currently using the test sheet. change key to key for real sheet later
sh = gc.open_by_key('1T9JQBnk9cwEHLYqIezYYDs2XxsGpbSkVNEhDQwULEK0')
resultSh = gc.open_by_key('1jxCVoFxCWtabFVgputblzAdn_h4vM-ZL7jt1_akFlOc')
worksheet = sh.worksheet("Sheet2") #new data

resultWkSht = resultSh.worksheet("Software Tasks")

res = worksheet.get_all_values()
row1 = worksheet.row_values(1)
#remove first row
i = 0
#loop through each row (not the first) and write them to the other spreadsheet
#need to add fields to them (dates, finished?, owner, ...)

emailSubj = today + " EOD Tasks"
emailMsg = """Hello \n\n This is the list of tasks that Jordan completed on """ + today + """. \n\n"""
emailMsg2 = ""
             

print(today)
for row in res:
    if(i!=0):
         print(row)
         for opt in row:
             print(opt)
         #create list in order(based on social marketing thing)   
         resultRow = ["Quick Updates",row[0],"Email",today,today, today, today, "high", "Jordan",row[3],row[1]]
         resultWkSht.append_row(resultRow)
         emailMsg2 = emailMsg2 + "On this day I worked to " + row[0] + ". \nThis involved: \n   " + row[1] + ". This is important because " + row[2] + ". \n\n"
         
    i = i + 1     
emailMsg2 = emailMsg2 + "\n Thanks, \n Jordan Ziegler"
emailMsg = emailMsg + emailMsg2
send_email.send_email(emailSubj, emailMsg)


"""submit list order
0 - project name
1 - task name
2 - assigned by
3 - date assigned
4 - due date
5 - date started
6 - completed date
7 - priority
8 - owner
9 - status
10 - notes
11+ nothing else matters


 """


print("--- %s seconds ---" % (time.time() - start_time)) #put this in the main program at the end
#get data
#get data for today
#rearrange data
#display data
#update second sheet with new data in new format (STAR?)
# situation task action result
# what did i do, who benefits by me doing it?



#call send_email




#res = worksheet.get_all_records() <- dict
#dict has the key being the first row. 

#res = worksheet.get_all_values() <- lists
# each row is a list

#res = worksheet.col_values(1)
#gives you a list of values in the first column

#res = worksheet.get('A2:C3')
#gets the data as a 2d array

#worksheet.insert_row(data,3)
#inserts in the place specified

#worksheet.append_row(data)
#adds to the end

#sheets.getDaily


#sheets.upsertDaily



#sheets.getALLRecords
#sheets.updateRecord
#sheets.appendRecord
#sheets.deleteRecord

def getDataToWrite():
    print("stuff goes here")

def writeData(param):
    print("stuff goes here to upload to the sheet")
