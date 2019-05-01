
# coding: utf-8

# In[26]:


df = pd.read_excel('Faculty.xlsx', sheetname='Sheet1')  
for index, row in df.iterrows():
    email = row['Email ID']  
    
    if (email.find('@')==-1):
        email = email +  '@pilani.bits-pilani.ac.in'
        print(email)
        df.at[index, 'Email ID'] = email

print(df['Email ID'])
df = df.set_index('Faculty ID')
df.to_excel( 'Faculty.xlsx')

