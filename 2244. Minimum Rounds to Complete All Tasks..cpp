class Solution {
public:
    int minimumRounds(vector<int>& tasks) {
        map<int,int> maps;
        int rounds = 0;
        for (auto a : tasks)
        maps[a]++;
        for (auto [a,val] : maps){
        if (val == 1)
        return -1;
        if(val%3 == 0){
            rounds = rounds + val/3;
        }
        else{
            rounds += val/3 + 1;
        }
        }
        return rounds;
    }
};
