class Solution {
public:
    int minDeletionSize(vector<string>& strs) {
        int K = strs[0].size();
        int r = strs.size();
        int count = 0;
        for(int i =0; i < K;i++){
            for(int j = 1; j < r ;j++){
                if (strs[j][i] < strs[j-1][i]){
                count++;
                break;
                }
                
            }
        }
        return count;
    }
};
