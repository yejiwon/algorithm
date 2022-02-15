/**
 * @param {number[]} cost
 * @return {number}
 */
 var minCostClimbingStairs = function(cost) {
    let dp = [cost[0]]
    let len = cost.length

    if (cost.length > 1) {
        dp.push(cost[1])
    }
    
    for (let j = 2; j < len; j++) {
        dp.push(cost[j] + Math.min(dp[j-1], dp[j-2]))
    }
    
    return Math.min(dp[len-1], dp[len-2])
};