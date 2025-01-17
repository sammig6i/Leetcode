class Solution {
public:
    vector<vector<int>> findWinners(vector<vector<int>>& matches) {
        vector<vector<int>> res;
        unordered_map<int, int> losses;
        for (vector<int> match : matches) {
            int loser = match[1];
            losses[loser]++;
        }

        unordered_set<int> no_loss;
        unordered_set<int> one_loss;
        for (vector<int> match : matches) {
            int winner = match[0], loser = match[1];
            if (losses.find(winner) == losses.end()) {
                no_loss.insert(winner);
            } 
            if (losses.find(loser) != losses.end() && losses[loser] == 1) {
                one_loss.insert(loser);
            }
        }
        
        vector<int> no_loss_vec(no_loss.begin(), no_loss.end());
        vector<int> one_loss_vec(one_loss.begin(), one_loss.end());
        sort(no_loss_vec.begin(), no_loss_vec.end());
        sort(one_loss_vec.begin(), one_loss_vec.end());
        return {no_loss_vec, one_loss_vec};

    }
};