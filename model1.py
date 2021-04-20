import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
#print(sys.executable)
import numpy as np
import pickle as pk
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from flask import Flask,render_template,request,url_for
app = Flask(__name__, instance_relative_config=True, template_folder='template')
@app.route('/hellos')
def hellos():
    return render_template('xyz.html')
    #app.debug="TRUE"
    #return app
@app.route('/detect',methods=['POST'])
def predicts():
    
    x=request.form.to_dict()
    #120,130,140,150,160,120,180,65,135,23,145,1,32,165,124,176,143,123,156,178,176,32,145,164,176,187,197,234,129,130
    #pred=model.predict(np.array([[0.10,0.48,0.92,0.15,0.22,1,0,0,1,0,0,1,0,1,0,0,1,0,0,1,0,1,0,0,0,0,0,0,1,0]]).reshape(1,30))
    #pred1=pred[0]
    #x=[63,1,2,138,250,1,0,150,0,2,3,0,0,1,1]
    '''X=pd.DataFrame(x)
    pr=pd.get_dummies(X, columns=categorical_val)
    pred=model.predict(np.array(pr))'''
    #--------------------------------------------------------
    X=pd.DataFrame(x,index=[0])
    m_columns=list(X_train.columns)
    pk.dump(m_columns,open('modelcolumns.pkl','wb'))
    pr=pd.get_dummies(X, columns=categorical_val)
    pr=pr.reindex(columns=m_columns,fill_value=0)
    pred=model.predict(pr)
    pred=pred[0]
    return render_template('xyz.html',prediction="The pedicted value is {}".format(pred),val=X)
if __name__=='__main__':
    app.run(debug="True")