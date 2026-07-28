class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        	std::vector<std::vector<std::string>> finalResults;
	std::unordered_map<std::string, std::vector<std::string>> mapStrings;

	for(std::string s : strs){
		std::string key = s;
		std::sort(key.begin(), key.end());
		mapStrings[key].push_back(s);
		}

	for(const auto &pair : mapStrings){
		finalResults.push_back(pair.second);
	}

	return finalResults;
    }
};
