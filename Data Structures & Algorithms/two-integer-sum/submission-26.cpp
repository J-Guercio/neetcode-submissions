class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        std::unordered_map<int,int> seen;
        
        for(int i = 0; i < nums.size(); i++){
            int complament = target - nums[i];
            if(seen.count(complament)){
                return {seen[complament],i};
            }
            seen[nums[i]] = i;
        }
        return {};
    }
};
