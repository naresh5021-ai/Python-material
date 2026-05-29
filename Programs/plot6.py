import matplotlib.pyplot as plt
brnames=['CSE','ECE','IT','MECH','EEE','CIVIL']
stdcount=[100,102,55,90,45,50]
colors  = ["gold","green","coral","skyblue",'yellow','pink']

plt.title('Naresh Pie chart')
plt.pie(stdcount,labels=brnames,
        colors = colors,
        autopct='%1.2f%%',
        shadow=False)
plt.axis('equal')

