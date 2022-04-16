#include <iostream>
using namespace std;

int main(void) {
    int m, n, k;
    cin >> m >> n;
    cin >> k;

    int temp;
    bool flag = false;
    for(int i = 0; i < m; i++) {
        for(int j = 0; j < n; j++) {
            cin >> temp;
            if(temp == k) {
                cout << "True\n";
                cout << i << " " << j << endl;
                flag = true;
                break;
            }
        }
    }

    if(!flag) {
        cout << "False\n";
    }

    return 0;
}