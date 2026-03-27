from django.shortcuts import render

# Create your views here.
def calculate_view(request):
    result = ''
    if request.method == 'POST':
        expression = request.POST.get('expression')

        try:
            # Evaluate the expression safely
            result = eval(expression)
        except:
            result = 'Error'

    return render (request, 'calculator/index.html', {'result': result})
