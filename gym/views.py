from django.http import HttpResponse

# 簡単なビューを作成
def home(request):
    return HttpResponse("こんにちはともやです!!")
