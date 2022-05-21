#!/usr/bin/env python
# coding: utf-8

# In[3]:


Manufacturer_dummies={
    "BMW": [1,0,0,0,0,0,0],
    "CHEVROLET":[0,1,0,0,0,0,0],
    "FORD":[0,0,1,0,0,0,0],
    "HYUNDAI":[0,0,0,1,0,0,0],
    "MERCEDES-BENZ":[0,0,0,0,1,0,0],
    "Other":[0,0,0,0,0,1,0],
    "TOYOTA":[0,0,0,0,0,0,1]
}



predict_dummis={0:'the price predict is: from 0:to 200',
1:'the price predict is: from 200:to 400',
2:'the price predict is: from 400:to 600',
3:'the price predict is: from 600:to 800',
4:'the price predict is: from 800:to 1000',
5:'the price predict is: from 1000:to 1200',
6:'the price predict is: from 1200:to 1400',
7:'the price predict is: from 1400:to 1600',
8:'the price predict is: from 1600:to 1800',
9:'the price predict is: from 1800:to 2000',
10:'the price predict is: from 2000:to 2200',
11:'the price predict is: from 2200:to 2400',
12:'the price predict is: from 2400:to 2600',
13:'the price predict is: from 2600:to 2800',
14:'the price predict is: from 2800:to 3000',
15:'the price predict is: from 3000:to 3200',
16:'the price predict is: from 3200:to 3400',
17:'the price predict is: from 3400:to 3600',
18:'the price predict is: from 3600:to 3800',
19:'the price predict is: from 3800:to 4000',
20:'the price predict is: from 4000:to 4200',
21:'the price predict is: from 4200:to 4400',
22:'the price predict is: from 4400:to 4600',
23:'the price predict is: from 4600:to 4800',
24:'the price predict is: from 4800:to 5000',
25:'the price predict is: from 5000:to 5200',
26:'the price predict is: from 5200:to 5400',
27:'the price predict is: from 5400:to 5600',
28:'the price predict is: from 5600:to 5800',
29:'the price predict is: from 5800:to 6000',
30:'the price predict is: from 6000:to 6200',
31:'the price predict is: from 6200:to 6400',
32:'the price predict is: from 6400:to 6600',
33:'the price predict is: from 6600:to 6800',
34:'the price predict is: from 6800:to 7000',
35:'the price predict is: from 7000:to 7200',
36:'the price predict is: from 7200:to 7400',
37:'the price predict is: from 7400:to 7600',
38:'the price predict is: from 7600:to 7800',
39:'the price predict is: from 7800:to 8000',
40:'the price predict is: from 8000:to 8200',
41:'the price predict is: from 8200:to 8400',
42:'the price predict is: from 8400:to 8600',
43:'the price predict is: from 8600:to 8800',
44:'the price predict is: from 8800:to 9000',
45:'the price predict is: from 9000:to 9200',
46:'the price predict is: from 9200:to 9400',
47:'the price predict is: from 9400:to 9600',
48:'the price predict is: from 9600:to 9800',
49:'the price predict is: from 9800:to 10000',
50:'the price predict is: from 10000:to 10200',
51:'the price predict is: from 10200:to 10400',
52:'the price predict is: from 10400:to 10600',
53:'the price predict is: from 10600:to 10800',
54:'the price predict is: from 10800:to 11000',
55:'the price predict is: from 11000:to 11200',
56:'the price predict is: from 11200:to 11400',
57:'the price predict is: from 11400:to 11600',
58:'the price predict is: from 11600:to 11800',
59:'the price predict is: from 11800:to 12000',
60:'the price predict is: from 12000:to 12200',
61:'the price predict is: from 12200:to 12400',
62:'the price predict is: from 12400:to 12600',
63:'the price predict is: from 12600:to 12800',
64:'the price predict is: from 12800:to 13000',
65:'the price predict is: from 13000:to 13200',
66:'the price predict is: from 13200:to 13400',
67:'the price predict is: from 13400:to 13600',
68:'the price predict is: from 13600:to 13800',
69:'the price predict is: from 13800:to 14000',
70:'the price predict is: from 14000:to 14200',
71:'the price predict is: from 14200:to 14400',
72:'the price predict is: from 14400:to 14600',
73:'the price predict is: from 14600:to 14800',
74:'the price predict is: from 14800:to 15000',
75:'the price predict is: from 15000:to 15200',
76:'the price predict is: from 15200:to 15400',
77:'the price predict is: from 15400:to 15600',
78:'the price predict is: from 15600:to 15800',
79:'the price predict is: from 15800:to 16000',
80:'the price predict is: from 16000:to 16200',
81:'the price predict is: from 16200:to 16400',
82:'the price predict is: from 16400:to 16600',
83:'the price predict is: from 16600:to 16800',
84:'the price predict is: from 16800:to 17000',
85:'the price predict is: from 17000:to 17200',
86:'the price predict is: from 17200:to 17400',
87:'the price predict is: from 17400:to 17600',
88:'the price predict is: from 17600:to 17800',
89:'the price predict is: from 17800:to 18000',
90:'the price predict is: from 18000:to 18200',
91:'the price predict is: from 18200:to 18400',
92:'the price predict is: from 18400:to 18600',
93:'the price predict is: from 18600:to 18800',
94:'the price predict is: from 18800:to 19000',
95:'the price predict is: from 19000:to 19200',
96:'the price predict is: from 19200:to 19400',
97:'the price predict is: from 19400:to 19600',
98:'the price predict is: from 19600:to 19800',
99:'the price predict is: from 19800:to 20000',
100:'the price predict is: from 20000:to 20200',
101:'the price predict is: from 20200:to 20400',
102:'the price predict is: from 20400:to 20600',
103:'the price predict is: from 20600:to 20800',
104:'the price predict is: from 20800:to 21000',
105:'the price predict is: from 21000:to 21200',
106:'the price predict is: from 21200:to 21400',
107:'the price predict is: from 21400:to 21600',
108:'the price predict is: from 21600:to 21800',
109:'the price predict is: from 21800:to 22000',
110:'the price predict is: from 22000:to 22200',
111:'the price predict is: from 22200:to 22400',
112:'the price predict is: from 22400:to 22600',
113:'the price predict is: from 22600:to 22800',
114:'the price predict is: from 22800:to 23000',
115:'the price predict is: from 23000:to 23200',
116:'the price predict is: from 23200:to 23400',
117:'the price predict is: from 23400:to 23600',
118:'the price predict is: from 23600:to 23800',
119:'the price predict is: from 23800:to 24000',
120:'the price predict is: from 24000:to 24200',
121:'the price predict is: from 24200:to 24400',
122:'the price predict is: from 24400:to 24600',
123:'the price predict is: from 24600:to 24800',
124:'the price predict is: from 24800:to 25000',
125:'the price predict is: from 25000:to 25200',
126:'the price predict is: from 25200:to 25400',
127:'the price predict is: from 25400:to 25600',
128:'the price predict is: from 25600:to 25800',
129:'the price predict is: from 25800:to 26000',
130:'the price predict is: from 26000:to 26200',
131:'the price predict is: from 26200:to 26400',
132:'the price predict is: from 26400:to 26600',
133:'the price predict is: from 26600:to 26800',
134:'the price predict is: from 26800:to 27000',
135:'the price predict is: from 27000:to 27200',
136:'the price predict is: from 27200:to 27400',
137:'the price predict is: from 27400:to 27600',
138:'the price predict is: from 27600:to 27800',
139:'the price predict is: from 27800:to 28000',
140:'the price predict is: from 28000:to 28200',
141:'the price predict is: from 28200:to 28400',
142:'the price predict is: from 28400:to 28600',
143:'the price predict is: from 28600:to 28800',
144:'the price predict is: from 28800:to 29000',
145:'the price predict is: from 29000:to 29200',
146:'the price predict is: from 29200:to 29400',
147:'the price predict is: from 29400:to 29600',
148:'the price predict is: from 29600:to 29800',
149:'the price predict is: from 29800:to 30000',
150:'the price predict is: from 30000:to 30200',
151:'the price predict is: from 30200:to 30400',
152:'the price predict is: from 30400:to 30600',
153:'the price predict is: from 30600:to 30800',
154:'the price predict is: from 30800:to 31000',
155:'the price predict is: from 31000:to 31200',
156:'the price predict is: from 31200:to 31400',
157:'the price predict is: from 31400:to 31600',
158:'the price predict is: from 31600:to 31800',
159:'the price predict is: from 31800:to 32000',
160:'the price predict is: from 32000:to 32200',
161:'the price predict is: from 32200:to 32400',
162:'the price predict is: from 32400:to 32600',
163:'the price predict is: from 32600:to 32800',
164:'the price predict is: from 32800:to 33000',
165:'the price predict is: from 33000:to 33200',
166:'the price predict is: from 33200:to 33400',
167:'the price predict is: from 33400:to 33600',
168:'the price predict is: from 33600:to 33800',
169:'the price predict is: from 33800:to 34000',
170:'the price predict is: from 34000:to 34200',
171:'the price predict is: from 34200:to 34400',
172:'the price predict is: from 34400:to 34600',
173:'the price predict is: from 34600:to 34800',
174:'the price predict is: from 34800:to 35000',
175:'the price predict is: from 35000:to 35200',
176:'the price predict is: from 35200:to 35400',
177:'the price predict is: from 35400:to 35600',
178:'the price predict is: from 35600:to 35800',
179:'the price predict is: from 35800:to 36000',
180:'the price predict is: from 36000:to 36200',
181:'the price predict is: from 36200:to 36400',
182:'the price predict is: from 36400:to 36600',
183:'the price predict is: from 36600:to 36800',
184:'the price predict is: from 36800:to 37000',
185:'the price predict is: from 37000:to 37200',
186:'the price predict is: from 37200:to 37400',
187:'the price predict is: from 37400:to 37600',
188:'the price predict is: from 37600:to 37800',
189:'the price predict is: from 37800:to 38000',
190:'the price predict is: from 38000:to 38200',
191:'the price predict is: from 38200:to 38400',
192:'the price predict is: from 38400:to 38600',
193:'the price predict is: from 38600:to 38800',
194:'the price predict is: from 38800:to 39000',
195:'the price predict is: from 39000:to 39200',
196:'the price predict is: from 39200:to 39400',
197:'the price predict is: from 39400:to 39600',
198:'the price predict is: from 39600:to 39800',
199:'the price predict is: from 39800:to 40000',
200:'the price predict is: from 40000:to 40200',
201:'the price predict is: from 40200:to 40400',
202:'the price predict is: from 40400:to 40600',
203:'the price predict is: from 40600:to 40800',
204:'the price predict is: from 40800:to 41000',
205:'the price predict is: from 41000:to 41200',
206:'the price predict is: from 41200:to 41400',
207:'the price predict is: from 41400:to 41600',
208:'the price predict is: from 41600:to 41800',
209:'the price predict is: from 41800:to 42000',
210:'the price predict is: from 42000:to 42200',
211:'the price predict is: from 42200:to 42400',
212:'the price predict is: from 42400:to 42600',
213:'the price predict is: from 42600:to 42800',
214:'the price predict is: from 42800:to 43000',
215:'the price predict is: from 43000:to 43200',
216:'the price predict is: from 43200:to 43400',
217:'the price predict is: from 43400:to 43600',
218:'the price predict is: from 43600:to 43800',
219:'the price predict is: from 43800:to 44000',
220:'the price predict is: from 44000:to 44200',
221:'the price predict is: from 44200:to 44400',
222:'the price predict is: from 44400:to 44600',
223:'the price predict is: from 44600:to 44800',
224:'the price predict is: from 44800:to 45000',
225:'the price predict is: from 45000:to 45200',
226:'the price predict is: from 45200:to 45400',
227:'the price predict is: from 45400:to 45600',
228:'the price predict is: from 45600:to 45800',
229:'the price predict is: from 45800:to 46000',
230:'the price predict is: from 46000:to 46200',
231:'the price predict is: from 46200:to 46400',
232:'the price predict is: from 46400:to 46600',
233:'the price predict is: from 46600:to 46800',
234:'the price predict is: from 46800:to 47000',
235:'the price predict is: from 47000:to 47200',
236:'the price predict is: from 47200:to 47400',
237:'the price predict is: from 47400:to 47600',
238:'the price predict is: from 47600:to 47800',
239:'the price predict is: from 47800:to 48000',
240:'the price predict is: from 48000:to 48200'}


# In[5]:


Leatherinterior_dummise={
    "Yes":[1],
    "No":[0]
}


# In[6]:


Category_dummise={
    "Coupe":[1,0,0,0,0,0,0],
    "Hatchback":[0,1,0,0,0,0,0],
    "Jeep":[0,0,1,0,0,0,0],
    "Minivan":[0,0,0,1,0,0,0],
    "Other":[0,0,0,0,1,0,0],
    "Sedan":[0,0,0,0,0,1,0],
    "Universal":[0,0,0,0,0,0,1]
}


# In[7]:


Fueltype_dummies={
    "Diesel":[1,0,0,0,0,0],
    "Hybrid":[0,1,0,0,0,0],
    "Hydrogen":[0,0,1,0,0,0],
    "LPG":[0,0,0,1,0,0],
    "Petrol":[0,0,0,0,1,0],
    "Plug-in Hybrid":[0,0,0,0,0,1],
    "CNG":[0,0,0,0,0,0]
}


# In[8]:


Gearboxtype_dummies={
    "Automatic":[1,0,0],
    "Other":[0,1,0],
    "Tiptronic":[0,0,1]
}


# In[10]:


Drivewheels_dummies={
    "Front":[1,0],
    "Rear":[0,1],
    "4x4":[0,0]
}


# In[11]:


Wheel_dummies={
    "Right-hand drive":[1],
    "Left wheel":[0]
}


# In[ ]:




