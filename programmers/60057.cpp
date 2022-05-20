#include <string>
#include <vector>
#include <iostream>

using namespace std;

int solution(string s) {
    int answer = 0;

    for(int i=1; i<s.length()/2; i++){
        string tmp = "";
        int nTmp = 0;
        for(int j=0; j<s.length(); j++){
            tmp += s.substr(j, i);
            cout << tmp << endl;
        }
    }

    return answer;
}

solution("abcabcabde");