import matplotlib.pyplot as plt 
import numpy as np

def agregate(file, year, UR_US_total,UR_CA_total,UR_SanMateo_total,UR_SantaClara_total, UR_Alameda_total,UR_Yuba_total):
    # Opens file
    labor = open(file, "r")
    data = labor.readlines() 
    lines = len(data)

    UR_CA_list = []
    UR_US_list = []

    # Employment Rate
    for i in range(6, lines-3):
        try:
            UR_US_list.append(float(data[i].split()[-1]))
            # California FINS state code
            if data[i].split()[1] == '06':
                UR_CA_list.append(float(data[i].split()[-1]))
            # San Mateo LAUS code
            if data[i].split()[0] == 'CN0608100000000':
                UR_SanMateo = float(data[i].split()[-1])
            # Santa Clara LAUS code
            elif data[i].split()[0] == 'CN0608500000000':
                UR_SantaClara = float(data[i].split()[-1])
            # Alameda LAUS code
            elif data[i].split()[0] == 'CN0600100000000':
                UR_Alameda = float(data[i].split()[-1])
            # Yuba LAUS code
            elif data[i].split()[0] == 'CN0611500000000': 
                UR_Yuba = float(data[i].split()[-1])
        except ValueError:
            pass
            
    # Calculates average UR for US and California
    UR_US = sum(UR_US_list)
    average_US = UR_US / len(UR_US_list)
    UR_CA = sum(UR_CA_list)
    average_CA = UR_CA / len(UR_CA_list)

    x = [average_US, average_CA, UR_SanMateo, UR_SantaClara, UR_Alameda, UR_Yuba]
    
    UR_US_total.append(x[0])
    UR_CA_total.append(x[1])
    UR_SanMateo_total.append(x[2])
    UR_SantaClara_total.append(x[3])
    UR_Alameda_total.append(x[4])
    UR_Yuba_total.append(x[5])
    
    labor.close()

UR_US_total = []
UR_CA_total = []
UR_SanMateo_total = []
UR_SantaClara_total = []
UR_Alameda_total = []
UR_Yuba_total = []
years = []

#remember to increase range to 23
for i in range(23):
    
    if i < 10:
        years.append(int(f'200{i}'))
        file = f"200{i}Labor.txt"
        year = int(f'200{i}')
    else:
        years.append(int(f'20{i}'))
        file = f"20{i}Labor.txt"
        year = int(f'20{i}')
    agregate(file, year, UR_US_total,UR_CA_total,UR_SanMateo_total,UR_SantaClara_total, UR_Alameda_total, UR_Yuba_total)

# initializing the data 
x = years
a = UR_US_total
b = UR_CA_total
c = UR_SanMateo_total
d = UR_SantaClara_total
e = UR_Alameda_total
f = UR_Yuba_total

y1 = np.array(a)
y2 = np.array(b)
y3 = np.array(c)
y4 = np.array(d)
y5 = np.array(e)
y6 = np.array(f)

plt.plot(x, y1, x, y2, x, y3, x, y4, x, y5, x, y6)

font = {'family':'serif','color':'darkred','size':15}

plt.xlabel("Year", fontdict = font)
plt.ylabel("Unemployment Rate", fontdict = font)

plt.legend(["United States", "California", "San Mateo", "Santa Barbara", "Alameda", "Yuba"], loc="upper right")

plt.show()

