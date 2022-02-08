var countBits = function(n) {
    let dp = [0]
    let offset = 1;
    
    for (let i=1; i< n+1; i++) {
        dp.push(0)
    }
    
    
    for (let i=1; i < n+1; i++) {
        if ((offset * 2) === i) {
            offset = i
        }
        dp[i] = dp[i-offset] + 1
    }
    
    return dp
};