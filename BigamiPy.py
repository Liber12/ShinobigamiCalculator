import seaborn as sns
import matplotlib.pyplot as plt

def TargetNum(TargetX, TargetY, TokugiX, TokugiY):
    return abs(TargetX - TokugiX) + abs(TargetY - TokugiY) + 5


TokugiSource = [['絡繰術', '火術', '水術', '針術', '仕込み', '衣装術', '縄術', '登術', '拷問術', '壊器術', '掘削術'],
                ['騎乗術', '砲術', '手裏剣術', '手練', '身体操術','歩法', '走法', '飛術', '骨法術', '刀術', '怪力'],
                ['生存術', '潜伏術', '遁走術', '盗聴術', '腹話術', '隠形術','変装術', '香術', '分身の術', '隠蔽術', '第六感'],
                ['医術', '毒術', '罠術', '調査術', '詐術', '対人術','遊芸', '九ノ一の術', '傀儡の術', '流言の術', '経済力'],
                ['兵糧術', '鳥獣術', '野戦術', '地の利', '意気', '用兵術','記憶術', '見敵術', '暗号術', '伝達術', '人脈'],
                ['異形化', '召喚術', '死霊術', '結界術', '封術', '言霊術', '幻術', '瞳術', '千里眼の術', '憑依術', '呪術']]
TokugiTable = [[0] * 12 for i in range(12)]  # 特技表
TargetTable = [[0] * 12 for i in range(12)]  # 目標値表

Tokugi = [[6, 7], [2, 6], [8, 3]]  # 習得特技

for TargetY in range(len(TokugiTable)):
    for TargetX in range(len(TokugiTable[TargetY])):
        TargetTable[TargetX][TargetY] = TargetNum(TargetX, TargetY,
                                                    Tokugi[0][0], Tokugi[0][1])

sns.heatmap(TargetTable, vmin=5, center=7, cmap='winter')
plt.show()

#print(*TargetTable, sep='\n')
