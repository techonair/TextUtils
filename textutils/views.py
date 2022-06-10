from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    param = {'name': 'Bhanu', 'place': 'Mars' }
    return render(request, 'index.html', param)

def analyse(request):
    
    djtext = request.POST.get('text', 'default' )

    removepunc = request.POST.get('removepunc', 'off' )
    fullcap = request.POST.get('fullcap', 'off')
    newlineremover = request.POST.get("newlineremover", 'off')
    extraspaceremover = request.POST.get("extraspaceremover", 'off')
    charcount = request.POST.get("charcount", 'off')

    analysed = djtext
    tmp = ''
    purpose = ''
    if newlineremover == 'on':
        #analysed = ''
        for char in djtext:
            if char != '\n' and char != '\r':
                tmp += char
        purpose += '\nNew Line Remover;'
        analysed = tmp
    tmp = ''
    if removepunc == 'on':
        punctuations = '''}{!()-[];:'"\,<>./?@#$%^&*_~'''
        for char in analysed:
            if char not in punctuations or char == " ":
                tmp += char
        purpose += '\nRemove Punctuations;'
        analysed = tmp

    tmp = ''
    if fullcap == 'on':
        #analysed = ''
        for char in analysed:
            tmp += char.upper()
        analysed = tmp
    purpose += '\nUpper Cap;'
    #print(analysed)

    tmp = ''
    if extraspaceremover == 'on':
        #analysed = ''
        for index, char in enumerate(analysed):
            if index < len(analysed)-1 and not (analysed[index] == ' ' and analysed[index+1] == ' '):
                tmp += char
        purpose += '\nExtra Space Remover;'
        analysed = tmp
    
    if charcount == 'on':
        analysed += "\n"
        cnt = 0
        for char in analysed:
            if char != ' ':
                cnt += 1
        purpose += '\nCharacter Count;'
        analysed += f'Total Character count is {cnt}'
        
    if not (charcount == 'on' or extraspaceremover == 'on' or newlineremover == 'on' or fullcap == 'on' or removepunc == 'on'):
        return HttpResponse('<h2>Error- No operation selected<h2> <br> <h3>Please Select any operation<h3>')

    param = {'purpose': purpose, 'analysed_text': analysed}
    return render(request, 'analyse.html', param)

def about(request):
    param = {'name': 'TextUtils', 'work': 'Text Analysis' }
    return render(request, 'about.html', param)

def contact(request):
    param = {'name': 'Bhanu', 'work': 'Software Engineer' }
    return render(request, 'contact.html', param)
