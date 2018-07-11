from django.shortcuts import render



def main_page(request):
    data = [1, 2, 3, 4]
    return render(request, 'index.html', {'data': data})

'''
html使用

< div > {{data}} < / div >
'''

