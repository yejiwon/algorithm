/**
 * @param {number} n
 * @return {number}
 */
 var fib = function(n) {
    if (n < 2) {
        return n
    };
    
    let fibo = {
        0: 0,
        1: 1,
    };
    
    for (let i = 2; i < n+1; i++) {
        fibo[i] = fibo[i-1] + fibo[i-2];
    };
    
    return fibo[n]
};