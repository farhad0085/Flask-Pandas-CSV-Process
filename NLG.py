import pandas as pd

df1 = pd.read_csv('SurveySection-Question-MAItem.csv',encoding='latin-1')
df2 = pd.read_csv('WrittenSummary-Quote.csv',encoding ='latin-1')
res =pd.read_csv('Response.csv',encoding ='latin-1')
res1 = pd.DataFrame({'count' : res.groupby( ['questionid','ResponseValue'] ).size()}).reset_index()
res1['%'] = 100 * res1['count'] / res1.groupby(['questionid'])['count'].transform('sum')
res1['%'] = res1['%']/100
question_ref = []
questionid = []
for i in res.questionid.unique():
    s= res['questionref'][res.questionid ==i].reset_index()
    question_ref.append(s['questionref'][0])
    questionid.append(i)

tables = pd.DataFrame()
tables['questionref'] = question_ref
tables['questionid'] = questionid

result = pd.merge(res1, tables, on='questionid')

df6 = pd.read_csv('SurveySection-Question-MAItem.csv',encoding='latin-1')
df7= pd.read_csv('WrittenSummary-Quote.csv',encoding ='latin-1')
df8 = pd.merge(df6,df7,on='writtensummaryid',how='left')
df8['quotedefinition'][df8.quotetypename == 'Field']= df8['quotedefinition'][df8.quotetypename == 'Field'].fillna('missing')
fields = []

for i in df8['quotedefinition'][df8.quotetypename == 'Field']:
    if '.' in i:
        fields.append(i.split('.',1)[1].lower())
    else:
        fields.append(i.lower())
df8['quotedefinition'][df8.quotetypename == 'Field'] = fields

if 'missing' in df8['quotedefinition'][df8.quotetypename == 'Field'].unique():
    df8['quotetext'][df8['quotedefinition']=='missing'] = 'missing'

    
for i in df8['quotedefinition'][df8.quotetypename == 'Field'].unique():
    if i != 'missing':
        df8['quotetext'][df8['quotedefinition'] == i] = df8[i][df2['quotedefinition'] == i]
df8['order'] = df8['orderinsidesurveysection'] + df8['orderinsidesurvey']

orderinsidesurvey = []
questionid = []
orderinsidesurveysection = []
for i in df8.questionid.unique():
    s= df8['orderinsidesurvey'][df8.questionid ==i].reset_index()
    l =df8['orderinsidesurveysection'][df8.questionid ==i].reset_index()
    questionid.append(i)
    
    orderinsidesurvey.append(s['orderinsidesurvey'][0])
    orderinsidesurveysection.append(l['orderinsidesurveysection'][0])    



tables1 = pd.DataFrame()
tables1['questionid'] = questionid
tables1['orderinsidesurvey'] =orderinsidesurvey
tables1['orderinsidesurveysection'] =orderinsidesurveysection


results1 =pd.merge(result, tables1, on='questionid')


results1['order'] = results1['orderinsidesurvey'] +results1['orderinsidesurveysection']

charttitle = []
questionid = []
for i in df8.questionid.unique():
    s= df8['charttitle'][df8.questionid ==i].reset_index()
    
    questionid.append(i)
    #print(i)
    charttitle.append(s['charttitle'][0])

tables2 = pd.DataFrame()
tables2['questionid'] = questionid
tables2['charttitle'] = charttitle

results2 =pd.merge(results1, tables2, on='questionid')

caldata = results2.copy()






#caldata = pd.read_csv('chartsdata.csv',encoding ='latin-1')


df = pd.merge(df1,df2,on='writtensummaryid',how='left')
df['quotedefinition'][df.quotetypename == 'Field']= df['quotedefinition'][df.quotetypename == 'Field'].fillna('missing')
fields = []

for i in df['quotedefinition'][df.quotetypename == 'Field']:
    if '.' in i:
        fields.append(i.split('.',1)[1].lower())
    else:
        fields.append(i.lower())


df['quotedefinition'][df.quotetypename == 'Field'] = fields
df['quotedefinition'][df.quotetypename == 'Field'].unique()

if 'missing' in df['quotedefinition'][df.quotetypename == 'Field'].unique():
    df['quotetext'][df['quotedefinition']=='missing'] = 'missing'



for i in df['quotedefinition'][df.quotetypename == 'Field'].unique():
    if i != 'missing':
        df['quotetext'][df['quotedefinition'] == i] = df[i][df['quotedefinition'] == i]


df['order'] = df['orderinsidesurveysection'] + df['orderinsidesurvey']


cal1  = df[['questionid','quotetext','quotedefinition']][df.quotetypename == 'Calculation']


def Select_top_category_of_chart(df, qid):
    df1 =  df[df.questionid == qid].sort_values(by ='count',ascending=False).reset_index()
    return df1['responsevalue'][0]


def percentage_value_of_top_category(df, qid):
        df1 =  df[df.questionid == qid].sort_values(by ='count',ascending=False).reset_index()
        if df1['%'][0]*100 > 1:
            v= int(round(df1['%'][0]*100))
        else:
            v =df1['%'][0]*100
        return v


def count_top_category(df, qid):
    df1 =  df[df.questionid == qid].sort_values(by ='count',ascending=False).reset_index()
    return df1['count'][0]



def count_all_categories(df, qid):
    df1 =  df[df.questionid == qid].sort_values(by ='count',ascending=False).reset_index()
    return df1['count'].sum()


def Select_2nd_top_category_of_chart(df, qid):
    df1 =  df[df.questionid == qid].sort_values(by ='count',ascending=False).reset_index()
    return df1['responsevalue'][1]



def percentage_value_of_2nd_top_category(df, qid):
        df1 =  df[df.questionid == qid].sort_values(by ='count',ascending=False).reset_index()
        if df1['%'][1]*100 > 1:
            v= int(round(df1['%'][1]*100))
        else:
            v =df1['%'][1]*100
        return v

def count_2nd_top_category(df, qid):
    df1 =  df[df.questionid == qid].sort_values(by ='count',ascending=False).reset_index()
    return df1['count'][1]



def Select_2nd_bottom_category_of_chart(df, qid):
    df1 =  df[df.questionid == qid].sort_values(by ='count',ascending=True).reset_index()
    return df1['responsevalue'][1]



def percentage_value_of_2nd_bottom_category(df, qid):
        df1 =  df[df.questionid == qid].sort_values(by ='count',ascending=True).reset_index()
        if df1['%'][0]*100 > 1:
            v= int(round(df1['%'][1]*100))
        else:
            v =df1['%'][1]*100
        return v


def count_2nd_bottom_category(df, qid):
    df1 =  df[df.questionid == qid].sort_values(by ='count',ascending=True).reset_index()
    return df1['count'][1]



def Select_bottom_category_of_chart(df, qid):
    df1 =  df[df.questionid == qid].sort_values(by ='count',ascending=True).reset_index()
    return df1['responsevalue'][0]


def percentage_value_of_bottom_category(df, qid):
        df1 =  df[df.questionid == qid].sort_values(by ='count',ascending=True).reset_index()
        if df1['%'][0]*100 > 1:
            v= int(round(df1['%'][0]*100))
        else:
            v =df1['%'][0]*100
        return v

def count_bottom_category(df, qid):
    df1 =  df[df.questionid == qid].sort_values(by ='count',ascending=True).reset_index()
    return df1['count'][0]


def Calculate_weighted_average(df,qid):
    try:
        if '-' not in df[df.questionid ==qid]['responsevalue'].tolist()[0]:
            rate = df[df.questionid ==qid]['responsevalue'].astype(float).tolist()
            amount =df[df.questionid ==qid]['count'].tolist()
            return int(sum(rate[g] * amount[g] / sum(amount) for g in range(len(rate))))
        else:
            return df[df.questionid ==qid]['count'].mean()
    except ValueError as ve:
        return 'missing'


def percentage_value_8_9_10_category(df,qid):
    sum = df[(df.questionid==qid) & (df.responsevalue =='8')]['%'].values[0] +df[(df.questionid==qid) & (df.responsevalue =='9')]['%'].values[0] +df[(df.questionid==qid) & (df.responsevalue =='10')]['%'].values[0]
    return int(sum*100)



def count_value_8_9_10_category(df,qid):
    sum = df[(df.questionid==qid) & (df.responsevalue =='8')]['count'].values[0] +df[(df.questionid==qid) & (df.responsevalue =='9')]['count'].values[0] +df[(df.questionid==qid) & (df.responsevalue =='10')]['count'].values[0]
    return int(sum)

def percentage_value_of_1_2_3_4_category(df,qid):
    try:
        sum = df[(df.questionid==qid) & (df.responsevalue =='1')]['%'].values[0] +df[(df.questionid==qid) & (df.responsevalue =='2')]['%'].values[0] +df[(df.questionid==qid) & (df.responsevalue =='3')]['%'].values[0] +df[(df.questionid==qid) & (df.responsevalue =='4')]['%'].values[0]
        return int(sum*100)
    except IndexError as ie:
        return 'missing'


def count_value_of_1_2_3_4_category(df,qid):
    try:
        sum = df[(df.questionid==qid) & (df.responsevalue =='1')]['count'].values[0] +df[(df.questionid==qid) & (df.responsevalue =='2')]['count'].values[0] +df[(df.questionid==qid) & (df.responsevalue =='3')]['count'].values[0] +df[(df.questionid==qid) & (df.responsevalue =='4')]['count'].values[0]
        return int(sum)
    except IndexError as ie:
        return 'missing'

def percentage_value_of_Somewhat_unlikely_Very_unlikely_categories(df,qid):
    sum = df[(df.questionid==qid) & (df.responsevalue =='Somewhat unlikely')]['%'].values[0]+df[(df.questionid==qid) & (df.responsevalue =='Very unlikely')]['%'].values[0]
    return int(sum*100)


def count_value_of_Somewhat_unlikely_Very_unlikely_categories(df,qid):
    sum = df[(df.questionid==qid) & (df.responsevalue =='Somewhat unlikely')]['count'].values[0]+df[(df.questionid==qid) & (df.responsevalue =='Very unlikely')]['count'].values[0]
    return int(sum)


def percentage_value_of_Somewhat_likely_Very_likely_categories(df,qid):
    sum = df[(df.questionid==qid) & (df.responsevalue =='Somewhat likely')]['%'].values[0]+df[(df.questionid==qid) & (df.responsevalue =='Very likely')]['%'].values[0]
    return int(sum*100)


def count_value_of_Somewhat_likely_Very_likely_categories(df,qid):
    sum = df[(df.questionid==qid) & (df.responsevalue =='Somewhat likely')]['count'].values[0]+df[(df.questionid==qid) & (df.responsevalue =='Very likely')]['count'].values[0]
    return int(sum)


def percentage_value_of_I_dont_know_category(df,qid):
    return int(df[(df.questionid==qid) & (df.responsevalue =="I don't know")]['%'].values[0]*100)


def count_value_of_I_dont_know_category(df,qid):
    return int(df[(df.questionid==qid) & (df.responsevalue =="I don't know")]['count'].values[0])



def count_value_of_No_category(df,qid):
    return int(df[(df.questionid==qid) & (df.responsevalue =="No")]['count'].values[0])


def percentage_value_of_No_category(df,qid):
    return int(df[(df.questionid==qid) & (df.responsevalue =="No")]['%'].values[0]*100)


def percentage_value_of_Yes_category(df,qid):
    return int(df[(df.questionid==qid) & (df.responsevalue =="Yes")]['%'].values[0]*100)

def count_value_of_Yes_category(df,qid):
    return int(df[(df.questionid==qid) & (df.responsevalue =="Yes")]['count'].values[0])


def percentage_value_of_no_input_in_the_process_category(df,qid):
    try:
        return int(df[(df.questionid==qid) & (df.responsevalue =="no input in the process")]['%'].values[0]*100)
    except IndexError as ie:
        return 'missing'


def count_value_of_no_input_in_the_process_category(df,qid):
    try:
        return int(df[(df.questionid==qid) & (df.responsevalue =="no input in the process")]['count'].values[0])
    except IndexError as ie:
        return 'missing'


def percentage_value_of_top_category_no_input(df, qid):
        df1 =  df[df.questionid == qid].sort_values(by ='count',ascending=False).reset_index()
        if df1['%'][1]*100 > 1:
            v= int(round(df1['%'][1]*100))
        else:
            v =df1['%'][1]*100
        return v


def count_top_category_no_input(df, qid):
    df1 =  df[df.questionid == qid].sort_values(by ='count',ascending=False).reset_index()
    return df1['count'][1]


def count_all_categories_no_input(df, qid):
    df1 =  df[(df.questionid == qid) & (df.responsevalue !='no input in process')].sort_values(by ='count',ascending=False).reset_index()
    return df1['count'].sum()


def Select_top_category_no_input(df, qid):
    df1 =  df[(df.questionid == qid) & (df.responsevalue !='no input in process')].sort_values(by ='count',ascending=False).reset_index()
    return df1['responsevalue'][0]


def Select_2nd_top_category_of_chart_no_input(df, qid):
    df1 =  df[(df.questionid == qid) & (df.responsevalue !='no input in process')].sort_values(by ='count',ascending=False).reset_index()
    return df1['responsevalue'][1]


def count_2nd_top_category_no_input(df, qid):
    df1 =  df[(df.questionid == qid) & (df.responsevalue !='no input in process')].sort_values(by ='count',ascending=False).reset_index()
    return df1['count'][1]

def percentage_2nd_top_category_no_input(df, qid):
    df1 =  df[(df.questionid == qid) & (df.responsevalue !='no input in process')].sort_values(by ='count',ascending=False).reset_index()
    return df1['%'][1]


df['newtext'] = df['quotetext']
newtext =[]
for ind in df.index:
        y = df['quotedefinition'][ind]
        i = df['questionid'][ind]
        #Select top category of chart
        if y == 'Select top category of chart':
            print(ind)
            df['newtext'][ind] = Select_top_category_of_chart(caldata, i)
            newtext.append(df['newtext'][ind])
            
        if y =='% value of top category':
            df['newtext'][ind] = percentage_value_of_top_category(caldata, i)
            newtext.append(df['newtext'][ind])
        if y =='count top category':
            df['newtext'][ind] = count_top_category(caldata, i)
            newtext.append(df['newtext'][ind])
        if y =='count all categories':
            df['newtext'][ind] = count_all_categories(caldata, i)
            newtext.append(df['newtext'][ind])
        if y =='Select 2nd top category of chart':
            df['newtext'][ind] = Select_2nd_top_category_of_chart(caldata, i)
            newtext.append(df['newtext'][ind])
        if y =='% value of 2nd top category':
            df['newtext'][ind] = percentage_value_of_2nd_top_category(caldata, i)
            newtext.append(df['newtext'][ind])
        
        if y =='count 2nd top category':
            df['newtext'][ind] = count_2nd_top_category(caldata, i)
            newtext.append(df['newtext'][ind])
            
        if y =='Select 2nd bottom category of chart':
            df['newtext'][ind] = Select_2nd_bottom_category_of_chart(caldata, i)
            newtext.append(df['newtext'][ind])
        
        if y =='% value of 2nd bottom category':
            df['newtext'][ind] = percentage_value_of_2nd_top_category(caldata, i)
            newtext.append(df['newtext'][ind])
        
        if y =='count 2nd bottom category':
            df['newtext'][ind] = count_2nd_bottom_category(caldata, i)
            newtext.append(df['newtext'][ind])
                
        if y =='Select bottom category of chart':
            df['newtext'][ind] = Select_bottom_category_of_chart(caldata, i)
            newtext.append(df['newtext'][ind])
        
        if y =='% value of bottom category':
            df['newtext'][ind] = percentage_value_of_bottom_category(caldata, i)  
            newtext.append(df['newtext'][ind])
        
        if y =='count bottom category':
            df['newtext'][ind] = count_bottom_category(caldata, i)
            newtext.append(df['newtext'][ind])
        
        if y =='Calculate weighted average (if <1, format as %)':
            df['newtext'][ind] = Calculate_weighted_average(caldata, i)
            newtext.append(df['newtext'][ind])
        
                
        if y =='Calculate weighted average':
            df['newtext'][ind] = Calculate_weighted_average(caldata, i)
            newtext.append(df['newtext'][ind])
        if y =='% value of 8+9+10 category':
            df['newtext'][ind] = percentage_value_8_9_10_category(caldata, i)
            newtext.append(df['newtext'][ind])
        
        if y =='count value of 8+9+10 category':
            df['newtext'][ind] = count_value_8_9_10_category(caldata, i)
            newtext.append(df['newtext'][ind])
        
                     
        if y =='% value of 1+2+3+4 category':
            df['newtext'][ind] = percentage_value_of_1_2_3_4_category(caldata, i)
            newtext.append(df['newtext'][ind])
        
                                
        if y =='count value of 1+2+3+4 category':
            df['newtext'][ind] = (count_value_of_1_2_3_4_category(caldata, i))
            newtext.append(df['newtext'][ind])
            
        if y =='% value of "Somewhat unlikely" + "Very unlikely" categories':
            df['newtext'][ind] = (percentage_value_of_Somewhat_unlikely_Very_unlikely_categories(caldata, i))
            newtext.append(df['newtext'][ind])
        
        if y =='count value of "Somewhat unlikely" + "Very unlikely" categories':
            df['newtext'][ind] = (count_value_of_Somewhat_unlikely_Very_unlikely_categories(caldata, i))
            newtext.append(df['newtext'][ind])
        
                
        if y =='% value of "Somewhat likely" + "Very likely" categories':
            df['newtext'][ind] = (percentage_value_of_Somewhat_likely_Very_likely_categories(caldata, i))  
            newtext.append(df['newtext'][ind])
        
        if y =='count value of "Somewhat likely" + "Very likely" categories':
            df['newtext'][ind] = (count_value_of_Somewhat_likely_Very_likely_categories(caldata, i))  
            newtext.append(df['newtext'][ind])
                
        if y =='% value of "I donÂ´t know" category':
            df['newtext'][ind] = (percentage_value_of_I_dont_know_category(caldata, i))
            newtext.append(df['newtext'][ind])
        if y =='count value of "I donÂ´t know" category':
            df['newtext'][ind] = (count_value_of_I_dont_know_category(caldata, i))
            newtext.append(df['newtext'][ind])
            
        if y =='% value of "No" category':
            df['newtext'][ind] = (percentage_value_of_No_category(caldata, i))
            newtext.append(df['newtext'][ind])
        
        if y =='count value of "No" category':
            df['newtext'][ind] = (count_value_of_No_category(caldata, i))
            newtext.append(df['newtext'][ind])
        if y =='% value of "Yes" category':
            df['newtext'][ind] = (percentage_value_of_Yes_category(caldata, i))
            newtext.append(df['newtext'][ind])
        
        if y =='count value of "Yes" category':
            df['newtext'][ind] = (count_value_of_Yes_category(caldata, i))
            newtext.append(df['newtext'][ind])
                
        if y =='% value of "no input in the process" category':
            df['newtext'][ind] = (percentage_value_of_no_input_in_the_process_category(caldata, i))
            
            newtext.append(df['newtext'][ind])
                        
        if y =='count value of "no input in the process" category':
            df['newtext'][ind] = (count_value_of_no_input_in_the_process_category(caldata, i))
            newtext.append(df['newtext'][ind])

            
        if y =='% value of top category (not counting category "no input in the process"':
            df['newtext'][ind] = (percentage_value_of_top_category_no_input(caldata, i))
            newtext.append(df['newtext'][ind])
            
        if y =='count value of top category (not counting category "no input in the process"':
            df['newtext'][ind] = (count_top_category_no_input(caldata, i))
            newtext.append(df['newtext'][ind])
        
        if y =='count all categories (not counting category "no input in the process"':
            df['newtext'][ind] = (count_all_categories_no_input(caldata, i))
            newtext.append(df['newtext'][ind])
            
        if y =='select value of top category (not counting category "no input in the process"':
            df['newtext'][ind] = (Select_top_category_no_input(caldata, i))
            newtext.append(df['newtext'][ind])
          
        if y =='% value of 2nd  top category (not counting category "no input in the process"':
            df['newtext'][ind] = (percentage_2nd_top_category_no_input(caldata, i))
            newtext.append(df['newtext'][ind])
                  
        if y =='count value of 2nd top category (not counting category "no input in the process"':
            df['newtext'][ind] = (count_2nd_top_category_no_input(caldata, i))
            newtext.append(df['newtext'][ind])
        if y =='select value of 2nd top category (not counting category "no input in the process"':
            df['newtext'][ind] = (Select_2nd_top_category_of_chart_no_input(caldata, i))
            newtext.append(df['newtext'][ind])



df['order'] = df['orderinsidesurveysection'] + df['orderinsidesurvey']


final1 = df.copy()
text=[]
chartHeading =[]
MainHeading =[]
QuestionId = []
order =[]
order1 = []
order2 = []
final['quotetext']= df['newtext']
df['quotetext'] = df['newtext']
for i in final1['questionid'].unique():
    print(i)
    final = final1.copy()
    df1 =final[(final['questionid']==i) & (final['quotedefinition'] !='Question.ChartTitle')]
    df1.sort_values(by=['orderinsidewrittensummary'], inplace=True)
    text.append(" ".join(df1.quotetext.astype('str').to_list()))
    
    chartHeading.append(final1['quotetext'][(final1['questionid']==i) &(final1['quotedefinition']=='Question.ChartTitle')].values)
    
    MainHeading.append(final1['surveysectionname'][(final1['questionid']==i)].to_list()[0])
    order.append(final1['orderinsidesurveysection'][(final1['questionid']==i)].to_list()[0])
    order1.append(final1['order'][(final1['questionid']==i)].to_list()[0])
    order2.append(final1['orderinsidesurvey'][(final1['questionid']==i)].to_list()[0])
    QuestionId.append(i)


df4 = pd.DataFrame()
df4['QuestionId'] =QuestionId
df4['text'] =text
#df1['chartHeading'] = chartHeading
df4['MainHeading'] = MainHeading
df4['orderinsidesurveysection'] =order
df4['order'] =order1
df4['orderinsidesurvey'] =order2
df4 = df1.dropna()
df4.to_csv('NLGdata.csv')
results2.to_csv('Chartsdata.csv')









