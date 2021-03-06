/**
 * @param {number} n
 * @return {number}
 */
var tribonacci = function (n) {
  let dp = [0, 1, 1];
  if (n > 2) {
    for (let i = 3; i <= n; i++) {
      dp.push(dp[i - 3] + dp[i - 2] + dp[i - 1]);
    }
  }
  return dp[n];
};
