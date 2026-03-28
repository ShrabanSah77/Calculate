from django.shortcuts import render
from django.http import HttpResponse
import math

def calculate_view(request):
    result = ""

    if request.method == "POST":
        operation = request.POST.get("operation")

        try:
            # Replace symbols if needed
            operation = operation.replace("^", "**")

            # Handle special functions
            if "√" in operation:
                number = float(operation.replace("√", ""))
                result = math.sqrt(number)

            elif "x²" in operation:
                number = float(operation.replace("x²", ""))
                result = number ** 2

            else:
                # Normal calculation
                result = eval(operation)

        except Exception as e:
            result = "Error"

    return render(request, "calculator/index.html", {"result": result})
