class Solution {
public:
    bool isAnagram(string s, string t) {
        std::map<char,int> sMap, tMap;

        for(char c : s) sMap[c]++;
        for(char c : t) tMap[c]++;

        return sMap == tMap;
    }
};
