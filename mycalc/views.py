from django.shortcuts import render
import math

def calculate_view(request):
    result = ""

    if request.method == "POST":
        expression = request.POST.get("expression")

        try:
            # Replace symbols if needed
            expression = expression.replace("^", "**")

            # Handle special functions
            if "√" in expression:
                number = float(expression.replace("√", ""))
                result = math.sqrt(number)

            elif "x²" in expression:
                number = float(expression.replace("x²", ""))
                result = number ** 2

            else:
                # Normal calculation
                result = eval(expression)

        except Exception as e:
            result = "Error"

    return render(request, "calculator/index.html", {"result": result})
