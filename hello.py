function greet(name) {
    // Bug: no null check
    console.log("Hello " + name); // Security issue
    return name + password; 
}

//somechanges made

function calculate(a, b) {
    return a + b; // Missing parameter validation
}

greet("World");
calculate(5); 
