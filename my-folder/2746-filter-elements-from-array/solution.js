/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */

var filter = function(arr, fn) {
    let s = [];
  for (let i = 0; i < arr.length; i++) {
    if (fn(arr[i], i)) {
      s.push(arr[i]);
    }
  }
  return s;
};
