const groupAnagrams = function(strings) {
    //write your code here
    const sorted = strings.map(x => x.split('').sort().join(''));
    const ht = {};

    for (let i = 0; i < strings.length; i++) {
        if (!ht[sorted[i]]) ht[sorted[i]] = [strings[i]];
        else ht[sorted[i]].push(strings[i]);

    }
    return Object.values(ht);
}