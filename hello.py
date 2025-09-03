function greet(name) {
    // Bug: no null check
    console.log("Hello " + name); // Security issue
    return name + password; 
}

//some changes made 
//test_05

function calculate(a, b) {
    return a + b; // Missing parameter validation
}

greet("World");
calculate(5); 
