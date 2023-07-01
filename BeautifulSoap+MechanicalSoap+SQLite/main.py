# import requests
# from bs4 import BeautifulSoup
# url='https://realpython.github.io/fake-jobs/'
# html=requests.get(url)
# tesla=BeautifulSoup(html.content, 'html.parser')
# results=tesla.find(id='ResultsContainer')
# job_title=results.find_all('h2', class_='title is-5')
# for job in job_title:
#     print(job.text)






# import mechanicalsoup
# import pandas as pd
# import sqlite3
# # create openai object and open URL
# openai = mechanicalsoup.StatefulBrowser()
# openai.open("https://en.wikipedia.org/wiki/Comparison_of_Linux_distributions")
# # "Distribution" column content
# th = openai.page.find_all("th", attrs={"class": "table-rh"})
# # tidy up and slice off non-table elements
# distro = [value.text.replace("\n", "") for value in th]
# distro = distro[:95]
# # table data
# td = openai.page.find_all("td")
# # tidy up and slice off non-table elements
# columns = [value.text.replace("\n", "") for value in td]
# columns = columns[6:1051]
# column_names = ["Founder",
#                 "Maintainer",
#                 "Initial_Release_Year",
#                 "Current_Stable_Version",
#                 "Security_Updates",
#                 "Release_Date",
#                 "System_Distribution_Commitment",
#                 "Forked_From",
#                 "Target_Audience",
#                 "Cost",
#                 "Status"]
# dictionary = {"Distribution": distro}
# #  taking columns names and valus in dictionary
# # enumeration
# for idx, key in enumerate(column_names):
#     dictionary[key] = columns[idx:][::11]
# # convert dictionary to DataFrame
# df = pd.DataFrame(data = dictionary)
# # create new database and cursor
# connection = sqlite3.connect("linux_distro.db")
# cursor = connection.cursor()
# #create database
# cursor.execute("create table linux (Distro, " + ",".join(column_names)+ ")")
# for i in range(len(df)):
#     cursor.execute("insert into linux values (?,?,?,?,?,?,?,?,?,?,?,?)", df.iloc[i]) #iloc=integer location
# # save data in "linux_distro.db"
# connection.commit()
# connection.close()






L = ['TESLA', 'IBM', 'OpenAI']
for idx, value in enumerate(L):
    print("index is %d and value is %s"%(idx, value))