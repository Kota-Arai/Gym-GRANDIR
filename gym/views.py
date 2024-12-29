from django.shortcuts import render  # renderをインポート
from django.http import HttpResponse

# 簡単なビューを作成
def home(request):
    return render(request, 'gym/home.html')  # gym/home.htmlを返す (ホームページ用テンプレートをレンダリング)

def about(request):
    return render(request, 'gym/about.html')  # gym/about.htmlを返す (アバウトページ用テンプレートをレンダリング)

def contact(request):  
    return render(request, 'gym/contact.html')  # gym/contact.htmlを返す (コンタクトページ用テンプレートをレンダリング)

def training(request):
    return render(request, 'gym/training.html')  # gym/training.htmlを返す (トレーニングページ用テンプレートをレンダリング)

def equipment(request):  
    return render(request, 'gym/equipment.html')  # gym/equipment.htmlを返す (設備ページ用テンプレートをレンダリング)


def rental(request):
    return render(request, 'gym/rental.html')  # gym/rental.htmlを返す (レンタルページ用テンプレートをレンダリング)

def oatmeal(request):
    return render(request, 'gym/oatmeal.html')  # gym/oatmeal.htmlを返す (オートミールページ用テンプレートをレンダリング)

def smoothie(request):
    return render(request, 'gym/smoothie.html')  # gym/smoothie.htmlを返す (スムージーページ用テンプレートをレンダリング)
