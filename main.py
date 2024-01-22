import numpy as np
import math
import copy

plot1_path = '1plot.txt'
plot6_path = '6plot.txt'
plot15_path = '15plot.txt'
plot33_path = '33plot.txt'
plot41_path = '41plot.txt'
plot46_path = '46plot.txt'
plot51_path = '51plot.txt'
plot58_path = '58plot.txt'
plot64_path = '64plot.txt'
plot72_path = '72plot.txt'
plot74_path = '74plot.txt'
plot84_path = '84plot.txt'
plot92_path = '92plot.txt'
xyz_path = 'xyz.txt'

def read_ref(path):
    f=open(path)
    s=[]
    f_line = f.read().split()
    for line in f_line:
        s.append(float(line))
    data = np.array(s)
    data.resize(data.size//2,2)
    return data

def read_xyz(path):
    f=open(path)
    s=[]
    f_line = f.read().split()
    for line in f_line:
        s.append(float(line))
    data = np.array(s)
    data.resize(data.size//4,4)
    return data

def pos_l(x, ref, d, T=6504):
    c = 2.99792458*10**8
    k = 1.380658*10**-23
    h = 6.6260755*10**-34
    t = T
    c1 = 2*(c**2)*h
    nm = 10**-9
    #nm = 1
    result = 0
    for i in range(380, 400):
        i_1 = i+1 
        l_f = c1/((i*nm)**5*(math.exp(h*c/(k*t*i*nm))-1))
        l_f1 = c1/((i_1*nm)**5*(math.exp(h*c/(k*t*i_1*nm))-1))
        #l_f=1
        #l_f1=1
        result_past = x[i-380][d]*ref[0][1]*l_f
        result_next = x[i+1-380][d]*ref[0][1]*l_f1
        result += (result_past+result_next)/2
    for i in range(400,655):
        i_1 = i+1 
        #l_f=1
        #l_f1=1
        l_f = c1/((ref[i-400][0]*nm)**5*(math.exp(h*c/(k*t*ref[i-400][0]*nm))-1))
        l_f1 = c1/((ref[i-399][0]*nm)**5*(math.exp(h*c/(k*t*ref[i-399][0]*nm))-1))
        result_past = x[i-380][d]*ref[i-400][1]*l_f
        result_next = x[i-379][d]*ref[i-399][1]*l_f1
        result += (result_past+result_next)/2
        #print(result_past)
        #print(l_f)
    for i in range(655,780):
        i_1 = i+1 
        #l_f=1
        #l_f1=1
        l_f = c1/((i*nm)**5*(math.exp(h*c/(k*t*i*nm))-1))
        l_f1 = c1/((i_1*nm)**5*(math.exp(h*c/(k*t*i_1*nm))-1))
        result_past = x[i-380][d]*ref[255][1]*l_f
        result_next = x[i+1-380][d]*ref[255][1]*l_f1
        result += (result_past+result_next)/2
        #print(result_past)
        #print(l_f)
    return result

def in_light(i,T=6504):
    c = 2.99792458*10**8
    k = 1.380658*10**-23
    h = 6.6260755*10**-34
    t = T

    c1 = 2*(c**2)*h
    nm = 10**-9
    e = math.exp(h*c/(k*t*i*nm))-1
    #nm = 1
    result = c1/((i*nm)**5)
    result = result/e
    return result

def pos(x, ref, d, T=6504):
    c = 2.99792458*10**8
    k = 1.380658*10**-23
    h = 6.6260755*10**-34
    t = T
    c1 = 2*(c**2)*h
    nm = 10**-9
    #nm = 1
    result = 0
    for i in range(380, 400):
        i_1 = i+1 
        #l_f = c1/((i*nm)**5*(math.exp(h*c/(k*t*i*nm))-1))
        #l_f1 = c1/((i_1*nm)**5*(math.exp(h*c/(k*t*i_1*nm))-1))
        l_f=-0.001*i+1.5
        l_f1=-0.001*(i+1)+1.5
        result_past = x[i-380][d]*ref[0][1]*l_f
        result_next = x[i+1-380][d]*ref[0][1]*l_f1
        result += (result_past+result_next)/2
    for i in range(400,655):
        i_1 = i+1 
        l_f=-0.001*round(ref[i-400][0])+1.5
        l_f1=-0.001*round(ref[i-399][0])+1.5
        #l_f = c1/((ref[i-400][0]*nm)**5*(math.exp(h*c/(k*t*ref[i-400][0]*nm))-1))
        #l_f1 = c1/((ref[i-399][0]*nm)**5*(math.exp(h*c/(k*t*ref[i-399][0]*nm))-1))
        result_past = x[round(ref[i-400][0])-380][d]*ref[i-400][1]*l_f
        result_next = x[round(ref[i-399][0])-380][d]*ref[i-399][1]*l_f1
        result += (result_past+result_next)*(round(ref[i-399][0])-round(ref[i-400][0]))/2
        #print(result_past)
        #print(l_f)
    for i in range(655,780):
        i_1 = i+1 
        l_f=-0.001*i+1.5
        l_f1=-0.001*(i+1)+1.5
        #l_f = c1/((i*nm)**5*(math.exp(h*c/(k*t*i*nm))-1))
        #l_f1 = c1/((i_1*nm)**5*(math.exp(h*c/(k*t*i_1*nm))-1))
        result_past = x[i-380][d]*ref[255][1]*l_f
        result_next = x[i+1-380][d]*ref[255][1]*l_f1
        result += (result_past+result_next)/2
        #print(result_past)
        #print(l_f)
    return result

def pos_i(x, ref, d, T=6504):
    c = 2.99792458*10**8
    k = 1.380658*10**-23
    h = 6.6260755*10**-34
    t = T
    c1 = 2*(c**2)*h
    nm = 10**-9
    #nm = 1
    result = 0
    for i in range(380, 400):
        i_1 = i+1 
        #l_f = c1/((i*nm)**5*(math.exp(h*c/(k*t*i*nm))-1))
        #l_f1 = c1/((i_1*nm)**5*(math.exp(h*c/(k*t*i_1*nm))-1))
        l_f=1
        l_f1=1
        result_past = x[i-380][d]*ref[0][1]*l_f
        result_next = x[i+1-380][d]*ref[0][1]*l_f1
        result += (result_past+result_next)/2
        #print(result_past)
    for i in range(400,655):
        i_1 = i+1 
        l_f=1
        l_f1=1
        #l_f = c1/((ref[i-400][0]*nm)**5*(math.exp(h*c/(k*t*ref[i-400][0]*nm))-1))
        #l_f1 = c1/((ref[i-399][0]*nm)**5*(math.exp(h*c/(k*t*ref[i-399][0]*nm))-1))
        result_past = x[round(ref[i-400][0])-380][d]*ref[i-400][1]*l_f
        result_next = x[round(ref[i-399][0])-380][d]*ref[i-399][1]*l_f1
        result += (result_past+result_next)*(round(ref[i-399][0])-round(ref[i-400][0]))/2
        #print(result_past)
        #print(l_f)
        #print(result_next)
    for i in range(655,780):
        i_1 = i+1 
        l_f=1
        l_f1=1
        #l_f = c1/((i*nm)**5*(math.exp(h*c/(k*t*i*nm))-1))
        #l_f1 = c1/((i_1*nm)**5*(math.exp(h*c/(k*t*i_1*nm))-1))
        result_past = x[i-380][d]*ref[255][1]*l_f
        result_next = x[i+1-380][d]*ref[255][1]*l_f1
        result += (result_past+result_next)/2
        #print(result_past)
        #print(l_f)
        #print(result_next)
    return result

def xyz_c(x,y,z):
    a=x+y+z
    return [x/a,y/a,z/a]

def rgb_to_rgbs(rgb_result):
    p = copy.deepcopy(rgb_result)
    for i in p:
        for j in range(0,3):
            if i[j]>=1:
                i[j] = 1
            elif i[j]<=0:
                i[j] = 0
            else:
                i[j]=i[j]
    
    for i in p:
        for j in range(0,3):
            i[j] = 1.055*i[j]**(1.0/2.4)-0.055

    for i in p:
        for j in range(0,3):
            if i[j]>=1:
                i[j] = 1
            elif i[j]<=0:
                i[j] = 0
            else:
                i[j]=i[j]
    return p

def rgbs_to_rgb8(result_rgbs):
    p =copy.deepcopy(result_rgbs)
    for i in p:
        for j in range(0,3):
            i[j] = round(255*i[j])
    return p


plot_1 = read_ref(plot1_path)
plot_6 = read_ref(plot6_path)
plot_15 = read_ref(plot15_path)
plot_33 = read_ref(plot33_path)
plot_41 = read_ref(plot41_path)
plot_46 = read_ref(plot46_path)
plot_51 = read_ref(plot51_path)
plot_58 = read_ref(plot58_path)
plot_64 = read_ref(plot64_path)
plot_72 = read_ref(plot72_path)
plot_74 = read_ref(plot74_path)
plot_84 = read_ref(plot84_path)
plot_92 = read_ref(plot92_path)
xyz = read_xyz(xyz_path)

name_list = [plot_1,plot_6,plot_15,plot_33,plot_41,plot_46,plot_51,
             plot_58,plot_64,plot_72,plot_74,plot_84,plot_92]
name_list_str = ['1plot','6plot','15plot','33plot','41plot','46plot','51plot',
             '58plot','64plot','72plot','74plot','84plot','92plot']
result_xyz=[]
for name in name_list:
    plot_x = pos_l(xyz,name,1,6504)
    plot_y = pos_l(xyz,name,2,6504)
    plot_z = pos_l(xyz,name,3,6504)
    result_xyz.append(xyz_c(plot_x,plot_y,plot_z))
    #print(xyz_c(plot_x,plot_y,plot_z))

rgb_1=[[3.2406,-1.5372,-0.4986],[-0.9689,1.8758,0.0415],[0.0557,-0.2040,1.0570]]
result_xyz = np.array(result_xyz)
rgb_1 = np.array(rgb_1)
result_rgb=np.matmul(result_xyz,rgb_1)
result_rgbs = rgb_to_rgbs(result_rgb)
result_rgb8 = rgbs_to_rgb8(result_rgbs)

intensity = []
for i in result_rgb8:
    intensity.append(i.sum())
intensity = np.array(intensity)

print(result_xyz)
print(result_rgb8) 
print(intensity)
print('brightest color is',name_list_str[np.argmax(intensity)])
print('darkest color is', name_list_str[np.argmin(intensity)])