#include <iostream>
#include <stdexcept>

using namespace std;

int main(int argc, char **argv) {
    try {
        cout << "Minimum Smoke" << endl;
        return 0;
    } catch (const exception& e) {
        cerr << e.what() << endl;
    }
}
