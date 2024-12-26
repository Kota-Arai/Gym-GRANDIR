from django.shortcuts import render  # renderをインポート
from django.http import HttpResponse

# 簡単なビューを作成
def home(request):
    return render(request, 'gym/home.html')  # gym/home.htmlを返す (ホームページ用テンプレートをレンダリング)

def about(request):
    return render(request, 'gym/about.html')  # gym/about.htmlを返す (アバウトページ用テンプレートをレンダリング)

def contact(request):  
    return render(request, 'gym/contact.html')  # gym/contact.htmlを返す (コンタクトページ用テンプレートをレンダリング)
