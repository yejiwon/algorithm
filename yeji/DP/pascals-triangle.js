/**
 * @param {number} numRows
 * @return {number[][]}
 */
var generate = function (numRows) {
  let answer = [];

  for (let i = 0; i < numRows; i++) {
    answer.push([]);

    for (let j = 0; j < i + 1; j++) {
      if (j === 0 || j === i) {
        answer[i].push(1);
      } else {
        answer[i].push(answer[i - 1][j - 1] + answer[i - 1][j]);
      }
    }
  }
  return answer;
};
