#  **My Shop Project**

## Table of contents:
1. [My Shop Project](#my-shop-project)
2. [My Page](#my-page)
3. [Description](#description)
4. [Requirements](#requirements)
5. [Features](#features)
6. [Install](#install)


## My page
[GitHub Page](https://github.com/ArtemSimon)


<a href="https://t.me/@Messi3026">
  <img src="https://img.shields.io/badge/Telegram-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white" alt="Telegram">
</a>

## Description
This site was made for friends (not the full version here) for an online shop.

## Requirements
+ Python 3.10+
+ Django 5.0+
+ Docker 

### Features
- [x] Developed the bakend part in Python, the frontend part in JavaScript / HTML / CSS.
- [x] Configured automatic assembly of the application into a Docker image via CI (GitHub Actions)
- [x] Configured automatic deployment of the application to VPS via CD (Continuous Deployment)
- [x] Implemented two-factor authentication (2FA) to improve system security. (OTP token)
- [x] Used Docker and Docker Compose to containerize and manage the application.
- [x] Developed a high-performance API for the site based on FastAPI.
- [x] Experience writing tests in pytest: creating fixtures, parameterizing tests, using markers and plugins.


# Install 
1. Clone repository
```
git clone https://github.com/ArtemSimon/myshop.git
cd myshop # cd project
```
2. Activate venv
```
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate    # Windows
```
3. Install requirements
```
pip install -r requirements.txt
```
4. Apply migrations
```
python manage.py runserver
```
5. Run server
```
python manage.py runserver
```

