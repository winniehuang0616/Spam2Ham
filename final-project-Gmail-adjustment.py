#!/usr/bin/env python
# coding: utf-8

# In[4]:


spam_texts = []
for i in range(2551,3051):
    r = open(r'.\output_final\output\output%d.txt'%i, encoding="utf-8")
    str = r.read()
    spam_texts.append(str)
    r.close()
len(spam_texts)


# In[5]:


spam_terms = []
for n in range(len(spam_texts)):
    spam_terms1 = spam_texts[n].split()
    spam_terms.extend(spam_terms1)
#     for a in spam_terms1:
#         spam_terms.append(a)
len(spam_terms)


# In[6]:


import collections
c1 = collections.Counter(spam_terms)
spam_comm = c1.most_common()
for i in spam_comm:
    print(i)


# In[7]:


spam = set()
for i in spam_comm: spam.add(i[0])
len(spam), spam


# In[8]:


ham_texts = []
for i in range(0,2551):
    r = open(r'.\output_final\output\output%d.txt'%i, encoding="utf-8")
    str = r.read()
    ham_texts.append(str)
    r.close()
len(ham_texts)


# In[9]:


ham_terms=[]
for n in range(len(ham_texts)):
    ham_terms1 = ham_texts[n].split()
    ham_terms.extend(ham_terms1)
#     for a in ham_terms1:
#         ham_terms.append(a)
len(ham_terms)


# In[10]:


c1 = collections.Counter(ham_terms)
ham_comm = c1.most_common()
for i in ham_comm:
    print(i)


# In[11]:


ham = set()
for i in ham_comm: ham.add(i[0])
len(ham), ham


# In[12]:


len(ham - spam)


# In[13]:


intersact = list(ham - spam)
intersact


# In[14]:


hw_dict = {}
for hw in ham_comm:
    include = False
    for sw in spam_comm:
        if hw[0] == sw[0]:
            include = True
            break
    if not include:
        hw_dict[hw[0]] = hw[1]
        
hw_dict


# In[15]:


lower_sw_dict = {}
for sw in spam_comm:
    include = False
    for hw in ham_comm:
        if sw[0].lower() == hw[0].lower():
            include = True
            break
    if not include:
        try:
            lower_sw_dict[sw[0].lower()] += sw[1]
        except:
            lower_sw_dict[sw[0].lower()] = sw[1]
        
lower_sw_dict


# In[33]:


append_dict = []
threshold = 150
for key, val in hw_dict.items():
    if val >= threshold:
        append_dict.append(key)
append_dict, len(append_dict)
print(len(append_dict),append_dict)


# In[34]:


#new = 'I wrote an unseen Message----- for you, You said that the Hat looks -----Original == '


# In[46]:


new = 'I wrote an unseen message for you, you said that the hat looks original == '


# In[17]:


word = '''['wrote:', 'URL:', 'XML', 'ALB>', '[1]', '<RPM-List@freshrpms.net>', 'RPM-List', 'http://lists.freshrpms.net/mailman/listinfo/rpm-list', 'Matthias', '0.99;', 'Bush', 'Hat', 'said.', 'Groups', '[2]', 'rpm', 'Perl', 'unseen', 'DataPower', '0.000', 'install']'''


# In[ ]:


word = ['wrote:']


# In[4]:


word = '''['wrote:', 'URL:', 'XML', 'ALB>', '[1]', '<RPM-List@freshrpms.net>', 'RPM-List', 'http://lists.freshrpms.net/mailman/listinfo/rpm-list', 'Matthias', '0.99;', 'Bush', 'Hat', 'said.', 'Groups', '[2]', 'rpm', 'Perl', 'unseen', 'DataPower', '0.000', 'install', 'exmh', 'packages', '{', 'Java', '0.01', 'msgs', 'kernel', '[Spambayes]', '@@', 'log', 'that.', 'wrote', 'Sent:', '}', 'OSDN', 'phone?', 'lists/l-k', 'Saou', 'https://www.inphonic.com/r.asp?r=sourceforge1&refcode1=vs3390', 'Wed,', 'Message-----', 'writes:', 'heaven.', '-----Original', '==', 'looks', 'by:ThinkGeek', 'http://thinkgeek.com/sf', 'SA', '-------', 'systems', 'Exmh-users', 'Exmh-users@redhat.com', 'https://listman.redhat.com/mailman/listinfo/exmh-users']'''


# In[5]:


word = word.split(',')
for i in range(len(word)):
    word[i] = word[i].strip()
    word[i] = word[i][1:-1]

word[0] = word[0][1:]
word[-1] = word[-1][:-1]

word


# In[44]:


text = []
for i in range(0,3051):
    doc = open(r'.\output_final\output\output%d.txt'%i, encoding="utf-8")
    data = doc.read()
    text.append(data)
    doc.close()
len(text)


# In[45]:


new = ''
for news in word:
    new += news + ' '
print(new)


# In[ ]:


for a in range(len(text)):
    if 2951 < a < 3051: 
        token = text[a].split()
        for i in range(len(del_dict)):    
            for n in range(len(token)):
                if token[n] == del_dict[i]:
                    token[n] = ''
                    c.append(del_dict[i])
        text[a] = ' '.join(token)
print(c)


# In[47]:


c = []
for a in range(len(text)):
    if a%2 == 0 and 2550<a<3051: 
        text[a] += new

print(text[3000])


# In[49]:


# 重新跑模型
label = []
for num in range(0,3051):
    if num <= 2551:
        label.append(0)
    else:
        label.append(1)
        
from sklearn.feature_extraction.text import CountVectorizer
TF_vectorizer = CountVectorizer(stop_words = 'english')
TF_vectors = TF_vectorizer.fit_transform(text)
TF_list0 = TF_vectors.toarray().tolist()

TF_list=[]
for a in range(0,3051):
    TF_list.append(TF_list0[a])
len(TF_list)

x_test = []
x_train = []
y_test = []
y_train = []
    
for a in range(0,3051):
    if a%2 == 0:
        x_test.append(TF_list[a])
        y_test.append(label[a])
    else:
        x_train.append(TF_list[a])
        y_train.append(label[a])


# In[25]:


len(y_test)


# In[26]:


len(y_train)


# In[50]:


from sklearn. naive_bayes import MultinomialNB
model = MultinomialNB(alpha=1.0,fit_prior=True, class_prior=None)
model.fit(x_train,y_train)

predicted_results = []
expected_results = []
expected_results.extend(y_test)
predicted_results.extend(model.predict(x_test))

from sklearn import metrics
print(metrics.classification_report(expected_results, predicted_results))


# In[ ]:




