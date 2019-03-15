#shared by Prabhi sir for python books - https://drive.google.com/drive/folders/0B5qd5nQpDK2GcDBzMXZGR3FPeDg
def getresult(*a):
    from sklearn.neighbors import KNeighborsClassifier as kn
    import pandas as pd

    df=pd.read_csv(r'C:\Users\Admin\Desktop\Laxman\log\iris.csv')
    #print(df)
    x=df.iloc[:,:4]
    #print(x)
    y=df.iloc[:,4]
    y=y.replace('setosa',0)
    y=y.replace('versicolor',1)
    y=y.replace('virginica',2)
    #print(y)

    mymodule=kn()
    mymodule.fit(x,y)

    i=[1,5,4,2]
    r=mymodule.predict([a])
    print('r=',r)
    return r

