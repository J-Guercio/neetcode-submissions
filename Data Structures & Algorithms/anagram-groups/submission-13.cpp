class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
                std::unordered_map<std::string ,std::vector<std::string>> anagramMap;
        std::vector<std::vector<std::string>> finalList;

        for(std::string& s : strs){
            std::string key = s;
            std::sort(key.begin(), key.end());
            anagramMap[key].push_back(s);
        }

        finalList.reserve(anagramMap.size());
        for(auto& [key,group] : anagramMap){
            finalList.push_back(std::move(group));
        }
        return finalList;
    }
};
