from django.shortcuts import render, redirect
import joblib
import os
import pandas as pd 
from . models import History
# Create your views here.
path=os.path.dirname(__file__)
model=joblib.load(open(os.path.join(path,'best_model.pkl'),'rb'))
label_encoder=joblib.load(open(os.path.join(path,'label_encoder.pkl'),'rb'))
def index(request):
    return render(request,"index.html")
def aboutus(request):
    return render(request,"aboutus.html")
def fileprediction(request):
    if request.method=="POST":
        csv_file=request.FILES["csv_file"]
        df=pd.read_csv(csv_file)
        input_df=df.drop('disease',axis="columns")
        prediction = model.predict(input_df)[0]
        predicted_label = label_encoder.inverse_transform([prediction])[0]
        his=History(fever=input_df.iloc[0,0],headache=input_df.iloc[0,1],nausea=input_df.iloc[0,2],vomiting=input_df.iloc[0,3],fatigue=input_df.iloc[0,4],joint_pain=input_df.iloc[0,5],skin_rash=input_df.iloc[0,6],cough=input_df.iloc[0,7],weight_loss=input_df.iloc[0,8],yellow_eyes=input_df.iloc[0,9],res=predicted_label)
        his.save()
        return render(request,"fileprediction.html",{"res":predicted_label})
    return render(request,"fileprediction.html")
def prediction(request):
    if request.method=="POST":
        fever=request.POST['fever']
        headache=request.POST['headache']
        nausea=request.POST['nausea']
        vomiting=request.POST['vomiting']
        fatigue=request.POST['fatigue']
        joint_pain=request.POST['joint_pain']
        skin_rash=request.POST['skin_rash']
        cough=request.POST['cough']
        weight_loss=request.POST['weight_loss']
        yellow_eyes=request.POST['yellow_eyes']        
        symptoms = ["fever", "headache", "nausea", "vomiting", "fatigue","joint_pain", "skin_rash", "cough", "weight_loss", "yellow_eyes"]
        user_input=[fever,headache, nausea, vomiting, fatigue, joint_pain, skin_rash, cough, weight_loss, yellow_eyes]
        input_df = pd.DataFrame([user_input], columns=symptoms)
        prediction = model.predict(input_df)[0]
        predicted_label = label_encoder.inverse_transform([prediction])[0]
        his=History(fever=fever,headache=headache,nausea=nausea,vomiting=vomiting,fatigue=fatigue,joint_pain=joint_pain,skin_rash=skin_rash,cough=cough,weight_loss=weight_loss,yellow_eyes=yellow_eyes,res=predicted_label)
        his.save()
        return render(request,"prediction.html",{"res":predicted_label})
    return render(request,"prediction.html")
def history(request):
    his=History.objects.all()
    return render(request,"history.html",{'his':his})
def delhis(request,id):
    his=History.objects.get(id=id)
    his.delete()
    return redirect('history')
