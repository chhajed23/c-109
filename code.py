
import random 
import statistics
import plotly.figure_factory as ff
import plotly.graph_objects as go


dice_result=[]
count=[]
for i in range(0,1000):
    dic1=random.randint(1,6)
    dic2=random.randint(1,6)
    dice_result.append(dic1+dic2)
    count.append(i)

mean=statistics.mean(dice_result)
median=statistics.median(dice_result)
mode=statistics.mode(dice_result)
sd=statistics.stdev(dice_result)
print("Mean",mean)
print("Median",median)
print("Mode",mode)
print("Sd",sd)




#Sd Start
first_sd_start,first_sd_end=mean-sd,mean+sd
second_sd_start,second_sd_end=mean-(2*sd),mean+(2*sd)
third_sd_start,third_sd_end=mean-(3*sd),mean+(3*sd)

fig=ff.create_distplot([dice_result],["Result"],show_hist=False)
fig.add_trace(go.Scatter(x=[mean,mean],y=[0,0.2],mode="lines",name="MEAN"))
fig.add_trace(go.Scatter(x=[first_sd_start,first_sd_start],y=[0,0.2],mode="lines",name="STANDARD DEVIATION ONE"))
fig.add_trace(go.Scatter(x=[first_sd_end,first_sd_end],y=[0,0.2],mode="lines",name="STANDARD DEVIATION ONE"))
fig.add_trace(go.Scatter(x=[second_sd_start,second_sd_start],y=[0,0.2],mode="lines",name="STANDARD DEVIATION TWO"))
fig.add_trace(go.Scatter(x=[second_sd_end,second_sd_end],y=[0,0.2],mode="lines",name="STANDARD DEVIATION TWO"))
fig.add_trace(go.Scatter(x=[third_sd_start,third_sd_start],y=[0,0.2],mode="lines",name="STANDARD DEVIATION THIRD"))
fig.add_trace(go.Scatter(x=[third_sd_end,third_sd_end],y=[0,0.2],mode="lines",name="STANDARD DEVIATION THIRD"))
fig.show()
list_of_data_sd_first=[result for result in dice_result if result>first_sd_start and result<first_sd_end]
list_of_data_sd_second=[result for result in dice_result if result>second_sd_start and result<second_sd_end]
list_of_data_sd_third=[result for result in dice_result if result>third_sd_start and result<third_sd_end]

print("{}% of data lies within 1 std".format(len(list_of_data_sd_first)*100/len(dice_result)))
print("{}% of data lies within 2 std".format(len(list_of_data_sd_second)*100/len(dice_result)))
print("{}% of data lies within 3 std".format(len(list_of_data_sd_third)*100/len(dice_result)))
