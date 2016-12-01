from api.model.ingredient import Ingredient, IngredientSerializer

def createDefaults():
    fields = (
        'name',
        'measureValue',
        'measureUnit',
        'defaultValue',
        'defaultUnit',
        'energy',
        'protein',
        'carb',
        'sugar',
        'fibre',
        'fat',
        'saturatedFat',
        'cholesterol',
        'calcium',
        'iron',
        'sodium',
        'potassium',
        'magnesium',
        'phosphorus',
        'thiamin',
        'riboflavin',
        'niacin',
        'folate',
    )
    IngredientArr = (
        ('Rice flour'     ,125 ,'ml'     ,83  ,'g'   ,305 ,5   ,67  ,1   ,0.3  ,0    ,8    ,0.3  ,0    ,63.0 ,29.0 ,82.0 ,0.1   ,0.02  ,3.2  ,3    ,0    ,1   ),
        ('Soy flour'      ,125 ,'ml'     ,53  ,'g'   ,174 ,25  ,20  ,11  ,9.2  ,1    ,0.1  ,0    ,127  ,4.9  ,11.0 ,1259 ,153   ,356   ,0.4  ,0.13 ,7.4  ,161 ),
        ('Wheat bran'     ,125 ,'ml'     ,4   ,'g'   ,8   ,1   ,2   ,0   ,1.6  ,0    ,0    ,0    ,3    ,0.4  ,0    ,43   ,22    ,37    ,0    ,0.02 ,0.7  ,3   ),
        ('Bread'          ,125 ,'ml'     ,64  ,'g'   ,170 ,6   ,35  ,1   ,4.7  ,2    ,0.3  ,0    ,10   ,2    ,340  ,109  ,44.0  ,115   ,0.2  ,0.05 ,3.4  ,22  ),
        ('Biscuit'        ,1   ,'count'  ,51  ,'g'   ,186 ,3   ,25  ,2   ,0.7  ,8    ,1.3  ,1    ,25   ,1.7  ,537  ,114  ,9.0   ,219   ,0.2  ,0.15 ,2.4  ,58  ),
        ('Granola bar'    ,1   ,'count'  ,25  ,'g'   ,118 ,3   ,16  ,0   ,1.3  ,5    ,0.6  ,0    ,15   ,0.7  ,74   ,84   ,24.0  ,69.0  ,0.1  ,0.03 ,1.1  ,6   ),
        ('Chocolate chip' ,1   ,'count'  ,20  ,'g'   ,98  ,1   ,13  ,7   ,0.6  ,5    ,1.5  ,0    ,7    ,0.7  ,59   ,30   ,10    ,23    ,0    ,0.05 ,0.7  ,20  ),
        ('Bean sprouts'   ,125 ,'g'      ,66  ,'ml'  ,125 ,137 ,3   ,7   ,0    ,1.2  ,0    ,9    ,1.2  ,6    ,143  ,22   ,52    ,1     ,12   ,0    ,46   ,10  ),
        ('Cabbage'        ,125 ,'ml'     ,37  ,'g'   ,9   ,1   ,2   ,1   ,0.7  ,0    ,17   ,0.2  ,7    ,91   ,6    ,9    ,3     ,33    ,0    ,16   ,12   ,0   ),
        ('Carrot'         ,1   ,'count'  ,61  ,'g'   ,25  ,1   ,6   ,3   ,1.5  ,0    ,20   ,0.2  ,42   ,195  ,7    ,21   ,367   ,3522  ,1    ,12   ,4    ,0   ),
        ('Cucumber'       ,4   ,'slice'  ,28  ,'g'   ,3   ,0   ,1   ,0   ,0.2  ,0    ,4    ,0.1  ,1    ,3    ,8    ,3    ,6     ,1     ,9    ,0    ,4    ,10  ),
        ('Eggplant'       ,125 ,'ml'     ,52  ,'g'   ,18  ,0   ,5   ,2   ,1.3  ,0    ,3    ,0.1  ,1    ,64   ,6    ,8    ,1     ,12    ,0    ,7    ,1    ,0   ),
        ('Lettuce'        ,250 ,'ml'     ,58  ,'g'   ,8   ,1   ,1   ,1   ,0.6  ,0    ,20   ,0.7  ,3    ,138  ,8    ,19   ,96    ,1155  ,0    ,42   ,2    ,0   ),
        ('Mushrooms'      ,3   ,'medium' ,54  ,'g'   ,12  ,2   ,2   ,1   ,0.6  ,0    ,2    ,0.3  ,2    ,170  ,5    ,46   ,0     ,0     ,0    ,9    ,1    ,0.2 ),
        ('Onion'          ,1   ,'medium' ,15  ,'g'   ,5   ,0   ,1   ,0   ,0.4  ,0    ,11   ,0.2  ,2    ,41   ,3    ,6    ,8     ,90    ,0    ,10   ,3    ,0   ),
        ('Potato'         ,1   ,'count'  ,156 ,'g'   ,145 ,3   ,34  ,3   ,3.4  ,0    ,8    ,0.5  ,8    ,610  ,39   ,78   ,0     ,0     ,0    ,14   ,20   ,0   ),
        ('Radishes'       ,3   ,'medium' ,14  ,'g'   ,2   ,0   ,0   ,0   ,0.2  ,0    ,3    ,0    ,5    ,31   ,1    ,3    ,0     ,1     ,0    ,3    ,2    ,0   ),
        ('Tomatoe'        ,1   ,'count'  ,123 ,'g'   ,22  ,1   ,5   ,3   ,1.5  ,0    ,12   ,0.3  ,6    ,292  ,14   ,30   ,52    ,552   ,3165 ,18   ,16   ,0   ),
        ('Apple'          ,1   ,'count'  ,138 ,'g'   ,72  ,0   ,19  ,14  ,2.6  ,0    ,8    ,0.2  ,1    ,148  ,7    ,15   ,4     ,37    ,0    ,4    ,6    ,0   ),
        ('Banana'         ,1   ,'count'  ,118 ,'g'   ,105 ,1   ,27  ,14  ,2.1  ,0    ,6    ,0.3  ,1    ,422  ,32   ,26   ,4     ,31    ,0    ,24   ,10   ,0   ),
        ('Figs'           ,1   ,'count'  ,50  ,'g'   ,37  ,0   ,10  ,8   ,1.5  ,0    ,18   ,0.2  ,1    ,116  ,9    ,7    ,4     ,43    ,0    ,3    ,1    ,0   ),
        ('Grapes'         ,20  ,'count'  ,100 ,'g'   ,69  ,1   ,18  ,15  ,1.2  ,0    ,10   ,0.4  ,2    ,191  ,7    ,20   ,3     ,39    ,0    ,2    ,11   ,0   ),
        ('Mango'          ,1   ,'count'  ,104 ,'g'   ,67  ,1   ,18  ,15  ,1.9  ,0    ,10   ,0.1  ,2    ,161  ,9    ,11   ,39    ,461   ,0    ,14   ,29   ,0   ),
        ('Orange'         ,1   ,'count'  ,131 ,'g'   ,62  ,1   ,15  ,12  ,2.3  ,0    ,52   ,0.1  ,0    ,237  ,13   ,18   ,8     ,93    ,0    ,39   ,70   ,0   ),
        ('Peach'          ,1   ,'count'  ,98  ,'g'   ,38  ,1   ,9   ,8   ,1.9  ,0    ,6    ,0.2  ,0    ,186  ,9    ,20   ,16    ,159   ,0    ,3    ,6    ,0   ),
        ('Pear'           ,1   ,'count'  ,166 ,'g'   ,96  ,1   ,26  ,16  ,5.0  ,0    ,15   ,0.3  ,2    ,198  ,12   ,18   ,2     ,22    ,0    ,12   ,7    ,0   ),
        ('Raspberries'    ,125 ,'ml'     ,65  ,'g'   ,34  ,1   ,8   ,3   ,4.2  ,0    ,16   ,0.4  ,1    ,98   ,14   ,19   ,1     ,8     ,0    ,14   ,17   ,0   ),
        ('Strawberries'   ,7   ,'count'  ,84  ,'g'   ,27  ,1   ,6   ,4   ,1.9  ,0    ,13   ,0.4  ,1    ,129  ,11   ,20   ,1     ,6     ,0    ,20   ,49   ,0   ),
        ('Buttermilk'     ,250 ,'ml'     ,259 ,'g'   ,104 ,9   ,12  ,12  ,2    ,1.4  ,10   ,300  ,0.1  ,272  ,391  ,28   ,230   ,18    ,0.2  ,13   ,0.57 ,0.40),
        ('Milk'           ,250 ,'ml'     ,259 ,'g'   ,88  ,9   ,13  ,13  ,0    ,0.2  ,5    ,324  ,0.1  ,109  ,404  ,28   ,261   ,158   ,2.7  ,13   ,1.37 ,0.47),
        ('Yogourt'        ,200 ,'ml'     ,207 ,'g'   ,145 ,5   ,24  ,24  ,3    ,2.1  ,12   ,191  ,0.2  ,81   ,257  ,23   ,157   ,0     ,0.2  ,25   ,0.58 ,0.23),
        ('Cheddar'        ,50  ,'g'      ,50  ,'g'   ,202 ,12  ,1   ,0   ,17   ,10.5 ,53   ,361  ,0.3  ,311  ,49   ,14   ,256   ,133   ,0.1  ,9    ,0.42 ,0.19),
        ('Cottage cheese' ,125 ,'ml'     ,119 ,'g'   ,86  ,1   ,5   ,3   ,3    ,1    ,0.8  ,573  ,0.2  ,500  ,103  ,6    ,160   ,13    ,0    ,14   ,0.75 ,0.20),
        ('Cream cheese'   ,30  ,'ml'     ,29  ,'g'   ,103 ,2   ,1   ,0   ,10   ,6.5  ,32   ,24   ,0.4  ,87   ,35   ,2    ,31    ,108   ,0    ,4    ,0.12 ,0.3 ),
        ('Feta cheese'    ,50  ,'g'      ,50  ,'g'   ,132 ,7   ,2   ,2   ,11   ,7.7  ,46   ,247  ,0.3  ,558  ,31   ,10   ,169   ,63    ,0.2  ,16   ,0.87 ,0.44),
        ('Mozzarella'     ,50  ,'g'      ,50  ,'g'   ,141 ,10  ,1   ,1   ,11   ,6.8  ,39   ,269  ,0.1  ,187  ,34   ,10   ,186   ,90    ,0.1  ,4    ,0.33 ,0.13),
        ('Sour cream'     ,15  ,'g'      ,15  ,'g'   ,22  ,0   ,1   ,0   ,2    ,1.3  ,6    ,16   ,0    ,6    ,19   ,1    ,14    ,17    ,0.1  ,2    ,0.04 ,0.02),
        ('Egg'            ,1   ,'count'  ,33  ,'g'   ,16  ,3   ,0   ,0   ,0    ,0    ,0    ,0    ,3    ,0    ,106  ,39   ,4     ,0     ,0    ,0    ,0.01 ,0   ),
        ('Beef'           ,75  ,'g'      ,75  ,'g'   ,200 ,26  ,0   ,10  ,4.0  ,5.0  ,0.4  ,71   ,2.5  ,46   ,202  ,18   ,142   ,0     ,0.5  ,2.38 ,4    ,0.1 ),
        ('Veal'           ,75  ,'g'      ,75  ,'g'   ,173 ,23  ,0   ,9   ,3.2  ,3.3  ,0.6  ,86   ,0.9  ,65   ,244  ,20   ,179   ,0     ,1.1  ,1.18 ,11   ,0.3 ),
        ('Pork'           ,75  ,'g'      ,75  ,'g'   ,274 ,21  ,0   ,20  ,7.9  ,8.9  ,2.6  ,85   ,0.9  ,100  ,251  ,18   ,147   ,2     ,0.8  ,0.83 ,2    ,0   ),
        ('Lamb'           ,75  ,'g'      ,75  ,'g'   ,182 ,21  ,0   ,10  ,4.2  ,4.3  ,0.7  ,80   ,1.6  ,54   ,193  ,17   ,125   ,0     ,0.2  ,1.71 ,13   ,0.1 ),
        ('Chicken'        ,75  ,'g'      ,75  ,'g'   ,142 ,19  ,0   ,7   ,1.8  ,2.6  ,1.4  ,63   ,0.4  ,45   ,241  ,20   ,0     ,20    ,0.2  ,0.24 ,3    ,0.2 ),
        ('Falafel'        ,1   ,'ball'   ,17  ,'g'   ,57  ,2   ,5   ,0   ,1.3  ,3    ,0.4  ,1.7  ,0.7  ,9    ,0.6  ,50   ,99    ,14    ,33   ,18   ,0    ,0   ),
        ('Beans'          ,175 ,'ml'     ,187 ,'g'   ,283 ,10  ,40  ,0   ,10.3 ,10   ,3.6  ,4.0  ,1.4  ,114  ,3.7  ,790  ,670   ,80    ,204  ,90   ,0    ,0   ),
        ('Lentils'        ,175 ,'ml'     ,179 ,'g'   ,190 ,14  ,32  ,0   ,5.9  ,1    ,0.2  ,0.3  ,0.6  ,22   ,4.1  ,4    ,317   ,39    ,161  ,112  ,0    ,0   ),
        ('Peas'           ,175 ,'ml'     ,145 ,'g'   ,171 ,12  ,31  ,4   ,4.2  ,1    ,0.1  ,0.1  ,0.2  ,20   ,1.9  ,3    ,525   ,52    ,144  ,94   ,0    ,0   ),
        ('Soybeans'       ,175 ,'ml'     ,127 ,'g'   ,220 ,21  ,13  ,4   ,8.0  ,11   ,1.7  ,2.5  ,6.4  ,130  ,6.5  ,1    ,655   ,109   ,312  ,69   ,0    ,0   ),
        ('Peanut butter'  ,30  ,'ml'     ,32  ,'g'   ,191 ,8   ,7   ,3   ,2.6  ,16   ,2.6  ,8.0  ,4.8  ,15   ,0.6  ,158  ,242   ,52    ,103  ,30   ,0    ,2.0 ),
        ('Almonds'        ,60  ,'ml'     ,36  ,'g'   ,208 ,8   ,7   ,2   ,4.2  ,18   ,1.4  ,11.6 ,4.4  ,89   ,1.5  ,0    ,262   ,99    ,171  ,10   ,0    ,9.3 ),
        ('Hazelnuts'      ,60  ,'ml'     ,34  ,'g'   ,215 ,5   ,6   ,1   ,3.3  ,21   ,1.5  ,15.6 ,2.7  ,39   ,1.6  ,0    ,233   ,56    ,99   ,39   ,0    ,5.2 ),
        ('Walnuts'        ,60  ,'ml'     ,25  ,'g'   ,166 ,4   ,3   ,1   ,1.7  ,17   ,1.6  ,2.3  ,12.0 ,25   ,0.7  ,1    ,112   ,40    ,88   ,25   ,0    ,0.2 ),
        ('Brown sugar'    ,5   ,'ml'     ,5   ,'g'   ,18  ,0   ,5   ,4   ,0    ,0    ,0    ,0    ,4    ,0.1  ,2    ,16   ,1     ,1     ,0    ,0    ,0    ,0   ),
        ('White sugar'    ,5   ,'ml'     ,4   ,'g'   ,16  ,0   ,4   ,4   ,0    ,0    ,0    ,0    ,0    ,0    ,0    ,0    ,0     ,0     ,0    ,0    ,0    ,0   ),
        ('Brown sugar'    ,5   ,'ml'     ,5   ,'g'   ,18  ,0   ,5   ,4   ,0    ,0    ,0    ,0    ,4    ,0.1  ,2    ,16   ,1     ,1     ,0    ,0    ,0    ,0   ),
        ('Cola'           ,250 ,'ml'     ,262 ,'g'   ,110 ,0   ,28  ,24  ,0    ,0    ,0    ,0    ,8    ,0.1  ,10   ,3    ,3     ,34    ,0    ,0    ,0    ,26  ),
        ('Coffee'         ,250 ,'ml'     ,250 ,'g'   ,3   ,0   ,0   ,0   ,0    ,0    ,0    ,0    ,5    ,0    ,5    ,123  ,8     ,8     ,0    ,0    ,0    ,100 ),
        ('Coffee latte'   ,250 ,'ml'     ,256 ,'g'   ,101 ,5   ,7   ,9   ,0    ,6    ,3.5  ,16   ,188  ,0.2  ,79   ,340  ,89    ,156   ,46   ,0    ,0    ,93  ),
        ('Tea'            ,250 ,'ml'     ,250 ,'g'   ,3   ,0   ,1   ,0   ,0    ,0    ,0    ,0    ,0    ,0.1  ,8    ,93   ,8     ,3     ,0    ,0    ,0    ,0   )
    )

    for ingredientVals in IngredientArr:
        ingredientDict = {}
        for i, field in enumerate(fields):
            ingredientDict[field] = ingredientVals[i]
        serializer = IngredientSerializer(data=ingredientDict)

        if serializer.is_valid():
            serializer.save()
        else:
            print(serializer.errors)
