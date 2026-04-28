# Disease Prediction - Django App

ML-based disease prediction app using symptoms. Deployed on Render.

## 🚀 Render par Deploy karne ke Steps

### Step 1: GitHub par Upload karo
1. GitHub par naya repository banao (e.g. `disease-prediction`)
2. Is folder ki saari files us repository mein push karo:
```bash
git init
git add .
git commit -m "Initial commit"
git remote add origin https://github.com/YOUR_USERNAME/disease-prediction.git
git push -u origin main
```

### Step 2: Render par Service banao
1. [render.com](https://render.com) par login karo
2. **"New +"** → **"Web Service"** click karo
3. Apna GitHub repo connect karo
4. Settings ye rakho:
   - **Name:** `disease-prediction`
   - **Environment:** `Python 3`
   - **Build Command:** `./build.sh`
   - **Start Command:** `gunicorn dpproject.wsgi:application`

### Step 3: Environment Variables set karo
Render dashboard mein **"Environment"** tab mein jao aur add karo:
| Key | Value |
|-----|-------|
| `SECRET_KEY` | (koi bhi lamba random string) |
| `DEBUG` | `False` |

### Step 4: Deploy!
- **"Create Web Service"** click karo
- Render automatically build karega aur deploy karega
- ~2-3 minutes mein URL milega jaise: `https://disease-prediction.onrender.com`

---

## Local Development
```bash
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

## Features
- Symptom-based disease prediction (ML model)
- CSV file upload for batch prediction
- Prediction history tracking
- Admin panel
"# Disease-Prediction" 
