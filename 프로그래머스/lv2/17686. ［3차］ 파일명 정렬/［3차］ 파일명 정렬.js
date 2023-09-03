function solution(files) {
  return files.sort((a, b) => {
    const regex = /^([a-zA-Z-\s.]+)(\d+)(.*)$/i; 
    const matchA = a.match(regex);
    const matchB = b.match(regex);

    if (!matchA || !matchB) {
      return 0;
    }

    const headA = matchA[1].toLowerCase();
    const headB = matchB[1].toLowerCase();
    const numberA = parseInt(matchA[2], 10);
    const numberB = parseInt(matchB[2], 10);

    if (headA < headB) return -1;
    if (headA > headB) return 1;

    if (numberA < numberB) return -1;
    if (numberA > numberB) return 1;

    return 0;
  });
}