import pandas as pd
import matplotlib.pyplot as plt
import io
import base64
import pickle
import os
import seaborn as sns
import joblib
from django.shortcuts import render, redirect
from django import forms
from django.conf import settings
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from sklearn.metrics import accuracy_score, confusion_matrix
from .models import CyberThreat

model = joblib.load(os.path.join(settings.BASE_DIR, 'simple_model.pkl'))

def homepage(request):
    return render(request, 'analysis/homepage.html')

def generate_base64_image():
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    image_base64 = base64.b64encode(buf.read()).decode('utf-8')
    buf.close()
    return image_base64

@login_required
def analysis(request):
    data = CyberThreat.objects.all().values()
    df = pd.DataFrame(data)

    attack_counts = df['attack_type'].value_counts()
    plt.figure(figsize=(10, 6))
    attack_counts.plot.pie(autopct='%1.1f%%', startangle=90, colors=sns.color_palette("coolwarm", len(attack_counts)))
    plt.title('Attack Types Distribution')
    plt.ylabel('')
    image_base64 = generate_base64_image()
    plt.close()

    df['timestamp'] = pd.to_datetime(df['timestamp'])
    time_series = df.set_index('timestamp').resample('M').size()
    plt.figure(figsize=(10, 6))
    time_series.plot()
    plt.title('Attack Frequency Over Time')
    plt.xlabel('Time')
    plt.ylabel('Number of Attacks')
    time_series_base64 = generate_base64_image()
    plt.close()

    heatmap_data = pd.crosstab(df['source_ip'], df['destination_ip'])
    plt.figure(figsize=(10, 6))
    sns.heatmap(heatmap_data, cmap="YlGnBu", linewidths=.5)
    plt.title('Heatmap of Attacks by IP')
    heatmap_base64 = generate_base64_image()
    plt.close()

    source_counts = df['source_ip'].value_counts().head(5)
    destination_counts = df['destination_ip'].value_counts().head(5)
    common_ips = [(ip, count, 'Source') for ip, count in source_counts.items()] + [(ip, count, 'Destination') for ip, count in destination_counts.items()]

    context = {
        'attack_counts': attack_counts,
        'image_base64': image_base64,
        'time_series_base64': time_series_base64,
        'heatmap_base64': heatmap_base64,
        'common_ips': common_ips,
    }
    return render(request, 'analysis/analysis.html', context)

class PredictionForm(forms.Form):
    packet_length = forms.FloatField(label='Packet Length')
    anomaly_scores = forms.FloatField(label='Anomaly Scores')
    source_ip = forms.IntegerField(label='Source IP (encoded)')
    destination_ip = forms.IntegerField(label='Destination IP (encoded)')

@login_required
def prediction(request):
    if request.method == 'POST':
        form = PredictionForm(request.POST)
        if form.is_valid():
            packet_length = form.cleaned_data['packet_length']
            anomaly_scores = form.cleaned_data['anomaly_scores']
            source_ip = form.cleaned_data['source_ip']
            destination_ip = form.cleaned_data['destination_ip']
            
            model_severity_path = os.path.join(settings.BASE_DIR, 'model_severity.pkl')
            model_attack_path = os.path.join(settings.BASE_DIR, 'model_attack.pkl')
            with open(model_severity_path, 'rb') as file:
                model_severity = pickle.load(file)
            with open(model_attack_path, 'rb') as file:
                model_attack = pickle.load(file)
            
            features = [[packet_length, anomaly_scores, source_ip, destination_ip]]
            severity_level = model_severity.predict(features)[0]
            severity_proba = model_severity.predict_proba(features).max()
            attack_type = model_attack.predict(features)[0]
            attack_proba = model_attack.predict_proba(features).max()
            
            context = {
                'form': form,
                'severity_level': severity_level,
                'severity_proba': severity_proba,
                'attack_type': attack_type,
                'attack_proba': attack_proba,
            }
            return render(request, 'analysis/prediction.html', context)
    else:
        form = PredictionForm()
    return render(request, 'analysis/prediction.html', {'form': form})

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('homepage')
    else:
        form = UserCreationForm()
    return render(request, 'analysis/signup.html', {'form': form})

def home_redirect(request):
    if request.user.is_authenticated:
        return redirect('homepage')
    else:
        return redirect('login')

model_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'model2.pkl')
model = joblib.load(model_path)

@login_required
def model_accuracy(request):
    data = {
        'Anomaly Scores': [0.99, 0.45, 0.17, 0.63],
        'Packet Length': [182, 147, 377, 1415],
        'Attack Type': [1, 0, 1, 0]
    }
    df = pd.DataFrame(data)
    X = df[['Anomaly Scores', 'Packet Length']]
    y = df['Attack Type']

    try:
        y_pred = model.predict(X)
        accuracy = accuracy_score(y, y_pred)
    except ValueError as e:
        return render(request, 'analysis/model_accuracy.html', {'error': str(e)})

    context = {
        'accuracy': accuracy,
    }
    return render(request, 'analysis/model_accuracy.html', context)

@login_required
def model_confusion_matrix(request):
    data = {
        'Anomaly Scores': [0.99, 0.45, 0.17, 0.63],
        'Packet Length': [182, 147, 377, 1415],
        'Attack Type': [1, 0, 1, 0]
    }
    df = pd.DataFrame(data)
    X = df[['Anomaly Scores', 'Packet Length']]
    y = df['Attack Type']

    try:
        y_pred = model.predict(X)
        conf_matrix = confusion_matrix(y, y_pred)
    except ValueError as e:
        return render(request, 'analysis/model_confusion_matrix.html', {'error': str(e)})

    context = {
        'conf_matrix': conf_matrix,
    }
    return render(request, 'analysis/model_confusion_matrix.html', context)
