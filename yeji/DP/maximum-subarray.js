var maxSubArray = function(nums) {
    let currSum = nums[0];
    let maxSum = nums[0];
    
    for(let i = 1; i < nums.length; i++) {
        currSum = Math.max(0, currSum);
        currSum += nums[i];
        maxSum = Math.max(maxSum, currSum);
    }
    return maxSum;
};

// js로는 한 4번 정도 통과를 못했는데
// currSum이랑 maxSum을 nums[0]으로 초기화해놓곤
// for문을 i=0부터 돌려서 그런거였다ㅜ