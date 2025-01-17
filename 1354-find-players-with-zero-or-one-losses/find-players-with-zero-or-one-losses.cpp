class Solution {
public:
    vector<vector<int>> findWinners(vector<vector<int>>& matches) {
        unordered_set<int> zero_loss;
        unordered_set<int> one_loss;
        unordered_set<int> more_loss;

        for (auto match : matches) {
            int winner = match[0];
            int loser = match[1];

            if (one_loss.find(winner) == one_loss.end() &&
                more_loss.find(winner) == more_loss.end()) {
                    zero_loss.insert(winner);
            } 

            if (one_loss.find(loser) != one_loss.end()) {
                one_loss.erase(loser);
                more_loss.insert(loser);
            } else if (zero_loss.find(loser) != zero_loss.end()) {
                zero_loss.erase(loser);
                one_loss.insert(loser);
            } else if (more_loss.find(loser) != more_loss.end()) {
                continue;
            } else {
                one_loss.insert(loser);
            }
        }
        
        vector<int> zero_loss_vec(zero_loss.begin(), zero_loss.end());
        sort(zero_loss_vec.begin(), zero_loss_vec.end());
        vector<int> one_loss_vec(one_loss.begin(), one_loss.end());
        sort(one_loss_vec.begin(), one_loss_vec.end());
        return {zero_loss_vec, one_loss_vec};

    }
};