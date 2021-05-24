
import random 
import statistics
import plotly.figure_factory as ff
import plotly.graph_objects as go
import pandas as pd

df=pd.read_csv("weight.csv")
hlist=df["Height(Inches)"].tolist()
wlist=df["Weight(Pounds)"].to_list()



hmean=statistics.mean(hlist)
hmedian=statistics.median(hlist)
hmode=statistics.mode(hlist)
hsd=statistics.stdev(hlist)
print("height-Mean",hmean)
print("height-Median",hmedian)
print("height-Mode",hmode)
print("height-Sd",hsd)

wmean=statistics.mean(wlist)
wmedian=statistics.median(wlist)
wmode=statistics.mode(wlist)
wsd=statistics.stdev(wlist)
print("weight-Mean",wmean)
print("weight-Median",wmedian)
print("weight-Mode",wmode)
print("weight-Sd",wsd)




#Sd Start
hfirst_sd_start,hfirst_sd_end=hmean-hsd,hmean+hsd
hsecond_sd_start,hsecond_sd_end=hmean-(2*hsd),hmean+(2*hsd)
hthird_sd_start,hthird_sd_end=hmean-(3*hsd),hmean+(3*hsd)

wfirst_sd_start,wfirst_sd_end=wmean-wsd,wmean+wsd
wsecond_sd_start,wsecond_sd_end=wmean-(2*wsd),wmean+(2*wsd)
wthird_sd_start,wthird_sd_end=wmean-(3*wsd),wmean+(3*wsd)

fig=ff.create_distplot([hlist],["Height"],show_hist=False)

fig.add_trace(go.Scatter(x=[hmean,hmean],y=[0,0.2],mode="lines",name="MEAN"))
fig.add_trace(go.Scatter(x=[hfirst_sd_start,hfirst_sd_start],y=[0,0.2],mode="lines",name="STANDARD DEVIATION ONE"))
fig.add_trace(go.Scatter(x=[hfirst_sd_end,hfirst_sd_end],y=[0,0.2],mode="lines",name="STANDARD DEVIATION ONE"))
fig.add_trace(go.Scatter(x=[hsecond_sd_start,hsecond_sd_start],y=[0,0.2],mode="lines",name="STANDARD DEVIATION TWO"))
fig.add_trace(go.Scatter(x=[hsecond_sd_end,hsecond_sd_end],y=[0,0.2],mode="lines",name="STANDARD DEVIATION TWO"))
fig.add_trace(go.Scatter(x=[hthird_sd_start,hthird_sd_start],y=[0,0.2],mode="lines",name="STANDARD DEVIATION THIRD"))
fig.add_trace(go.Scatter(x=[hthird_sd_end,hthird_sd_end],y=[0,0.2],mode="lines",name="STANDARD DEVIATION THIRD"))
fig.show()
fig1=ff.create_distplot([wlist],["Weight"],show_hist=False)
fig1.add_trace(go.Scatter(x=[wmean,wmean],y=[0,0.2],mode="lines",name="MEAN"))
fig1.add_trace(go.Scatter(x=[wfirst_sd_start,wfirst_sd_start],y=[0,0.2],mode="lines",name="STANDARD DEVIATION ONE"))
fig1.add_trace(go.Scatter(x=[wfirst_sd_end,wfirst_sd_end],y=[0,0.2],mode="lines",name="STANDARD DEVIATION ONE"))
fig1.add_trace(go.Scatter(x=[wsecond_sd_start,wsecond_sd_start],y=[0,0.2],mode="lines",name="STANDARD DEVIATION TWO"))
fig1.add_trace(go.Scatter(x=[wsecond_sd_end,wsecond_sd_end],y=[0,0.2],mode="lines",name="STANDARD DEVIATION TWO"))
fig1.add_trace(go.Scatter(x=[wthird_sd_start,wthird_sd_start],y=[0,0.2],mode="lines",name="STANDARD DEVIATION THIRD"))
fig1.add_trace(go.Scatter(x=[wthird_sd_end,wthird_sd_end],y=[0,0.2],mode="lines",name="STANDARD DEVIATION THIRD"))
fig1.show()






list_of_data_sd_first=[result for result in hlist if result>hfirst_sd_start and result<hfirst_sd_end]
list_of_data_sd_second=[result for result in hlist if result>hsecond_sd_start and result<hsecond_sd_end]
list_of_data_sd_third=[result for result in hlist if result>hthird_sd_start and result<hthird_sd_end]

print("{}% of data lies within height-1 std".format(len(list_of_data_sd_first)*100/len(hlist)))
print("{}% of data lies within height-2 std".format(len(list_of_data_sd_second)*100/len(hlist)))
print("{}% of data lies within height-3 std".format(len(list_of_data_sd_third)*100/len(hlist)))

wlist_of_data_sd_first=[result for result in wlist if result>wfirst_sd_start and result<wfirst_sd_end]
wlist_of_data_sd_second=[result for result in wlist if result>wsecond_sd_start and result<wsecond_sd_end]
wlist_of_data_sd_third=[result for result in wlist if result>wthird_sd_start and result<wthird_sd_end]

print("{}% of data lies within weight-1 std".format(len(list_of_data_sd_first)*100/len(wlist)))
print("{}% of data lies within weight-2 std".format(len(list_of_data_sd_second)*100/len(wlist)))
print("{}% of data lies within weight-3 std".format(len(list_of_data_sd_third)*100/len(wlist)))
