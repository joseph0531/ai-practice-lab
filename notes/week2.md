2026/6/1

pands:
    pd.read_csv() //讀取檔案

    head(n) //可以顯示出n筆資料

    info() //可以看到該資料的資訊(包括 檔案大小,多少columns, 檔案類型等等)

    describe() //可以快速生成該檔案的資料統計訊息

            count：非空值的数量
            mean：平均值
            std：标准差
            min：最小值
            25%：第一四分位数（Q1）
            50%：第二四分位数（中位数，Q2）
            75%：第三四分位数（Q3）
            max：最大值

    isnull() //找出欄位遺漏


        PassengerId      0
        Survived         0
        Pclass           0
        Name             0
        Sex              0
        Age            177
        SibSp            0
        Parch            0
        Ticket           0
        Fare             0
        Cabin          687
        Embarked         2
        dtype: int64


    sum() //資料表加總
    shape //資料有幾筆, 幾個欄位
    dropna() //移除資料

        dropna(how='all') 移除有遺漏值的資料
        dropna(subset=['欄位名稱'],  how='any') 任一個指定的欄位有遺漏值(Missing Value)的資料就移除
        dropna(subset=['欄位名稱'],  how='all') 指定的欄位皆有遺漏值(Missing Value)的資料就移除
    
    fillna(value='', inplace=True) 可填入指定關鍵字參數