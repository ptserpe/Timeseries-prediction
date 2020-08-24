import pandas as pd
import numpy as np
import datetime
#* --- paperTitle
#@ --- Authors
#t ---- Year
#c  --- publication venue
#index 00---- index id of this paper
#% ---- the id of references of this paper (there are multiple lines, with each indicating a reference)
#! --- Abstract

#Each paper is associated with abstract, authors, year, venue, and title.
#df = pd.DataFrame(columns=[ 'paperTitle', 'authors','year','publication venue',  'id','references' , 'abstract'])
temp_dict = {}
temp_list = []
df = pd.DataFrame()

with open("outputacm.txt", encoding="utf-8", buffering=374784) as fp:
    line = fp.readline()
    #print("Line {}: {}".format(cnt, line.strip()))
    cnt = 0
    while line:
        ref = []
        if line[0] == '#':
            
            line = line.rstrip()
            if line[1] == '*':
                if 'paperTitle' not in temp_dict:
                    temp_dict['paperTitle'] = line[2:]
                #df.loc[cnt,'paperTitle'] = line[2:]
            
            elif line[1] == '@':
                if 'authors' not in temp_dict:
                    temp_dict['authors'] = line[2:]
                #df.loc[cnt,'authors'] = line[2:]
                
            elif line[1] == 't':
                if 'year' not in temp_dict:
                    temp_dict['year'] = line[2:]
                #df.loc[cnt,'year'] = line[2:]
                

            elif line[1] == 'c':
                if 'publication venue' not in temp_dict:
                    temp_dict['publication venue'] = line[2:]
                #df.loc[cnt,'publication venue'] = line[2:]
               
            elif line[1] == 'i':
                if 'id' not in temp_dict:
                    temp_dict['id'] = line[6:]
                #df.loc[cnt,'id'] = line[6:]
               
            elif line[1] == '!':
                if 'abstract' not in temp_dict:
                    temp_dict['abstract'] = line[2:]
                #df.loc[cnt,'abstract'] = line[2:]
                    
            elif line[1] == '%':
                ref.append(line[2:])
                
                line = fp.readline()

                while line[0] == '#' and line[1] == '%':
                    
                    line = line.rstrip()
                    ref.append(line[2:])
                       
                    line = fp.readline()
                if 'references' not in temp_dict:
                    temp_dict['references'] = ref
                
                #df.loc[cnt,'references'] = ref
                
                continue

               
            line = fp.readline()
               
        else:
            if 'references' not in temp_dict:
                temp_dict['references'] = ref
            temp_list.append(temp_dict)
            cnt += 1 

            line = fp.readline()
            temp_dict = {}

df = df.append(temp_list, ignore_index=True)

#for i in range(len(df)):
 #   print(df.iloc[i]["paperTitle"])
#df.head(100)

# #drop the columns that are not needed for the neural nets
df_small = df.drop(['paperTitle', 'authors', 'publication venue', 'abstract'], axis=1)

# #drop rows with nan values
#df_small = df_small.dropna() 
df_small = df_small[df.year != '-1']
# #sort by ascending order of pablication year 
#df_small = df_small.sort_values(by=['year'])
#df_small = df_small.reindex(df['references'].str.len().sort_values(ascending=True).index)
# #lists of unique ids and years (all)
years = []
ids = []
years = df_small.year.unique()
years = years.tolist()
ids = df_small.id.unique()
ids = ids.tolist()
ids.pop(0)
years.pop(0)

# #We have a dataset with the year of publication , the id of paper and
# # references  of papers that are being used for each paper(with id)
df_small = df_small.drop(df_small.index[len(df_small)-1])
df_small = df_small.drop(df_small.index[0])
# #Dataframe to X Y arrays
matrx = np.asarray(df_small)

# #create array id x year

y = len(years)
x = len(ids)
buckets = [[0 for col in range(y)] for row in range(x)]

# # its a matrix with rows (different ids) and columns (years)
# # each pos is increasing by one everytime a paper is used as a reference in 
# #another paper of each year 
# #
# #this array will be used as the training set of our neural net
# # its a matrix with rows (different ids) and columns (years)
# # each pos is increasing by one everytime a paper is used as a reference in 
# #another paper of each year 
# #
# #this array will be used as the training set of our neural net


######################################################################
m = len(matrx)
#for i in range(m):
#    if matrx[i][1]:
#        print(matrx[i])
#        break
#begin = i
#print(begin)




#nn = nn.drop(nn.columns[1], axis=1)
#nn = nn.fillna(0)

#nn_matrx = np.asarray(nn)

t_list = []
# try ascending by list len
print('BEGIN')

for i in range(m):
    t_list = matrx[i][1]
    t_year = matrx[i][2]
    #print(t_list)
    #print(t_year)
    if t_list:
    
        for temp in t_list:
            y = years.index(t_year)
            x = ids.index(temp)
            buckets[x][y] += 1
            
#l = len(buckets)
#for z in range(0,l):
#    if all(item == 0 for item in buckets[z]):
#        np.delete(buckets,z, axis = 0)
#        #np.delete(ids, z, axis = 0)
#        ids.pop(z)
#        
nn = pd.DataFrame()

nn = nn.append(buckets, ignore_index = True)


nn.columns = years
nn['ids'] = ids

print(datetime.datetime.now())

export_csv = nn.to_csv (r'C:\Users\Sevi\Documents\CE418_Project(Neurofuzzy)\export_dataframe.csv', index = None, header=True)














#friaxnw lista temp megetoyw isi me years
################################################################33
###################################################################
#temp_list= [0] * y
#print('BEGIN')  
#m = len(matrx)
#for i in range(m-1):
#    temp_id = matrx[i][0] #string
#    temp_year =  matrx[i][2] #string
#    temp = i
#    for j in range(temp, m-1):
#           
#        if temp_id in matrx[j][1]:
#            k = np.where(years == matrx[j][2])
#            #buckets[x[0][0]][y[0][0]] += 1
#            print(k[0][0])
#            temp_list[k[0][0]] += 1
#    
#    z = np.where(ids == temp_id)
#    buckets[z[0][0]] = temp_list
#    #print(buckets[z[0][0]])
#    temp_list = [0]* y
    
   #else 
                #   append 0 
          #else
              #append 0
              
              #sorted by year apo to mikrotero sto megalytero kai !!!!na psaxnei apo ton eayto soy katw!
              ####################################
#print('BEGIN')
#temp_dict = {}
#for i in years:
#    if i not in temp_dict:
#        temp_dict[i] = 0        
#        
#temp_list = []
#
#nn = pd.DataFrame() 
#flag = 0
#m = len(matrx)
#for i in range(m-1):
#    temp_id = matrx[i][0] #string
#    #temp_year =  matrx[i][2] #string
#    temp = i
#    for j in range(temp, m-1):
#           
#        if temp_id in matrx[j][1]:
#            flag = 1
#            temp_dict[matrx[j][2]] += 1
#    
#    temp_list.append(temp_dict)
#    if flag:
#        for i in years:
#            temp_dict[i] = 0
#        flag = 0
#nn = nn.append(temp_list, ignore_index=True)