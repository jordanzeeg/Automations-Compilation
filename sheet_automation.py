#pip install pygsheets
import gspread
import send_email
import time #put this in the main program at the end

start_time = time.time() #put this in the main program at the end
gc = gspread.service_account(filename= 'credentials.json')

#currently using the test sheet. change key to key for real sheet later
sh = gc.open_by_key('1T9JQBnk9cwEHLYqIezYYDs2XxsGpbSkVNEhDQwULEK0')
resultSh = gc.open_by_key('1SLwsiYP1ng_I90lUBW61FhtoqTy4314Bn5IUC3DZlP0')
worksheet = sh.worksheet("datasheet")

res = worksheet.get_all_values()
row1 = worksheet.row_values(1)
#remove first row
i = 0
#loop through each row (not the first) and write them to the other spreadsheet
#need to add fields to them (dates, finished?, owner, ...)
for row in res:
    if(i!=0):
         print(row)
         for opt in row:
             print(opt)
         #create list in order(based on social marketing thing)    
    i = i + 1     
    

    
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
