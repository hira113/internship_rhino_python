import rhinoscriptsyntax as rs

pt_1=rs.AddPoint(100,100,0)
pt_2=rs.AddPoint(300,100,0)
circle_1=rs.AddCircle(pt_1,80)
circle_2=rs.AddCircle(pt_2,50)

#一つ目の関数
def getDistance(p_1,p_2):
    dis=rs.Distance(p_1,p_2)
    return dis

dis_1_2=getDistance(pt_1,pt_2)
#print(dis_1_2)

out_pts=[pt_1,pt_2]
out_circle=[circle_1,circle_2]
"""点と円を出力"""

#二つ目の関数
def getStatus(c_1, c_2):
    # 0:ちょうどいい距離なのでそのまま
    # 1:遠すぎる
    # 2:近すぎる
    
    if rs.IsCircle(c_1) and rs.IsCircle(c_2):
        radius_1 = rs.CircleRadius(c_1)
        radius_2 = rs.CircleRadius(c_2)
        
        #print(radius_1)
        #print(radius_2)
        
        pt_1 = rs.CircleCenterPoint(c_1)
        pt_2 = rs.CircleCenterPoint(c_2)
        
        #print(pt_1)
        #print(pt_2)
    
    #追加スクリプト↓
    dis_1_2=rs.Distance(pt_1,pt_2)
    #print(dis_1_2)
    #追加スクリプト↑
    
    if(dis_1_2 == radius_1 + radius_2):
        status = 0
    if(radius_1 + radius_2 < dis_1_2):
        status = 1
    if(dis_1_2 < radius_1 + radius_2):
        status = 2
    
    return status   #returnで「数値」を返している。

status=getStatus(circle_1,circle_2)
print(status)

#三つ目の関数
def Moveobj(c_1,c_2):
    
    #追加スクリプト↓
    pt_1=rs.CircleCenterPoint(c_1)
    pt_2=rs.CircleCenterPoint(c_2)
    #追加スクリプト↑
    
    if(status == 1):
        vector_1=rs.VectorCreate(pt_2,pt_1)
        
        #追加スクリプト↓
        vector_2=rs.VectorCreate(pt_1,pt_2)
        unit_vec_1=rs.VectorUnitize(vector_1)
        unit_vec_2=rs.VectorUnitize(vector_2)
        
        radius_1 = rs.CircleRadius(c_1)
        radius_2 = rs.CircleRadius(c_2)
        
        dis_1_2=rs.Distance(pt_1,pt_2)
        dis=dis_1_2 - (radius_1 + radius_2)
        move_dis=(dis/2) #/10 ←移動係数で割る？
        #追加スクリプト↑
        
        # vector_1をUnit Vector unit_vec にする
        # 円の差分距離 dis を計算
        # dis = 円中心点間の距離-(半径1+半径2)
        # 動かす距離 move_dis を計算
        # お互いに動かすので /2
        # 移動係数で割る /10
        
        #追加スクリプト↓
        move_vec_1=rs.VectorScale(unit_vec_1,move_dis)
        move_vec_2=rs.VectorScale(unit_vec_2,move_dis)
        
        move_obj_1=rs.MoveObject(c_1,move_vec_1)
        move_obj_2=rs.MoveObject(c_2,move_vec_2)
        #追加スクリプト↑
    
    return move_obj_1
    return move_obj_2
    
    #returnで「オブジェクト」を返している。

move=Moveobj(circle_1,circle_2)
#print(move)



import rhinoscriptsyntax as rs

#クラス定義
class CirclePack():
    def __init__(self,_id,_circle_obj): #イニシャライズ関数の引数を何にすれば良いのか？
        self.id=_id
        self.circle_obj=_circle_obj
    def getDistance(self)  #関数の引数も何にすれば良いのか？
    def getStatus(self)
    def MoveObj(self)


id_1=rs.AddCircle((0,0,0),40)

circle_1=CirclePack(self,id_1,_circle_obj) 
#インスタンス化(実体化)
#イニシャライズの関数の引数の数と同じ？
#ここでプログラム実行される。
#self(自分の？)




#print(circle_1) →idが出力される。
#print(circle_2) →idが出力される。
#print(rs.CircleRadius(circle_1)) →半径の数値が出力される。
#getStatus(circle_1, circle_2)
#radius_1=getStatus()

test
