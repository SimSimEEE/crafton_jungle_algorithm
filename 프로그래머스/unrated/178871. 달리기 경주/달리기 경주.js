function solution(players, callings) {
    keyPlayers = {};
    keyRank = {};
    players.forEach((player, index)=>{
        keyPlayers[player] = index;
    });
    callings.forEach((player)=>{
        const index = keyPlayers[player];
        keyPlayers[players[index-1]] = index
        keyPlayers[player] = index-1;
        [players[index-1], players[index]] = [players[index], players[index-1]]
    });
    return players;
}