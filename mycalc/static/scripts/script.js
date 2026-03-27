const display = document.getElementById('display');

// Add value
function appendToResult(value) {
    display.value += value;
}
// Clear
function clearResult() {
    display.value = '';
}

// Backspace
function backspace() {
    display.value = display.value.slice(0, -1);
}

// Calculate result (for "=" button if not submitting form)
function calculate() {
    try {
        display.value = eval(display.value);
    } catch {
        display.value = "Error";
    }
}
