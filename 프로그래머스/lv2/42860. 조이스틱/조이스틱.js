function solution(name) {
  let answer = 0;
  let L2 = 0;
  let move = name.length - 1;
  const length = name.length;

  for (let L1 = 0; L1 < name.length; L1++) {
    answer += Math.min(name[L1].charCodeAt(0) - 'A'.charCodeAt(0), 'Z'.charCodeAt(0) - name[L1].charCodeAt(0) + 1);

    let L2_idx = L1 + 1;
    while (L2_idx < length) {
      if (name[L2_idx] === 'A') {
        L2_idx++;
      } else {
        break;
      }
    }
    L2 = length - 1 - L2_idx + 1;
    move = Math.min(move, L1 + L2 + Math.min(L1, L2));
  }
  return answer + move;
}