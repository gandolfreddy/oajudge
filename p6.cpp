# include <bits/stdc++.h>
using namespace std;


int main() {
    int num;
    int maxNums = INT_MIN;

    // input & process
    for (int i=0; i<10; i++) {
        cin >> num;
        maxNums = max(maxNums, num);
    }

    // process
    cout << maxNums << endl;
    return 0;
}