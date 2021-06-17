class Itemvalue:
    def __init__(self,wt,val,ind):
        self.wt=wt
        self.val=val
        self.ind=ind
        self.cost=val//wt
    def __lt__(self,other):
        return self.cost<other.cost
class FractionalKnapsack:
    @staticmethod
    def getMaxValue(wt,val,capacity):
        ival=[]
        for i in range(len(wt)):
            ival.append(Itemvalue(wt[i],val[i],i))
        ival.sort(reverse=True)
        totalvalue=0
        for i in ival:
            curwt=int(i.wt)
            curval=int(i.val)
            if capacity-curwt>=0:
                capacity-=curwt
                totalvalue+=curval
            else:
                fraction=capacity/curwt
                totalvalue+=curval*fraction
                capacity=int(capacity-(curwt*fraction))
                break
        return totalvalue
if __name__ == "__main__":
    wt=[10,30,45]
    val=[10,34,23]
    capacity=50
    maxvalue=FractionalKnapsack.getMaxValue(wt,val,capacity)
    print(f"maximum value in knapsack is {maxvalue}")
    
