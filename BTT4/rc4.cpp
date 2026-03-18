#include <iostream>
#include <string>
using namespace std;

int S[10] = {0,1,2,3,4,5,6,7,8,9};
int K[4] = {2,4,1,7};
int N = 10;

void printS() {
    cout << "S = [";
    for (int i = 0; i < N; i++) {
        if (i) cout << ",";
        cout << S[i];
    }
    cout << "]" << endl;
}

// Buoc 1: KSA
void KSA() {
    cout << "=== KSA ===" << endl;
    int j = 0;
    for (int i = 0; i < N; i++) {
        int j_old = j;
        j = (j + S[i] + K[i % 4]) % N;
        swap(S[i], S[j]);
        cout << "i=" << i << ": j=(" << j_old << "+" << S[j] << "+" << K[i%4] << ")%" << N << "=" << j << "  ";
        printS();
    }
    cout << endl;
}

// Buoc 2: PRGA - sinh keystream
int PRGA(int &pi, int &pj) {
    pi = (pi + 1) % N;
    pj = (pj + S[pi]) % N;
    swap(S[pi], S[pj]);
    int t = (S[pi] + S[pj]) % N;
    return S[t];
}

int main() {
    cout << "== BAI TAP RC4 - An toan thong tin E9 2025.2 ==" << endl << endl;

    // Cau 1: Tinh dong khoa
    cout << "--- CAU 1: Tinh dong khoa RC4 ---" << endl;
    cout << "S ban dau: "; printS();
    cout << "K = [2,4,1,7]" << endl << endl;

    KSA();

    cout << "S sau KSA: "; printS();
    cout << endl;

    // Sinh keystream cho 13 ky tu "cybersecurity"
    string plaintext = "cybersecurity";
    int pi = 0, pj = 0;
    int keystream[13];

    cout << "=== PRGA ===" << endl;
    for (int t = 0; t < 13; t++) {
        keystream[t] = PRGA(pi, pj);
        cout << "t=" << t << ": i=" << pi << " j=" << pj << " Key=" << keystream[t] << endl;
    }

    cout << endl << "KeyStream: ";
    for (int i = 0; i < 13; i++) cout << keystream[i] << " ";
    cout << endl << endl;

    // Cau 2: Ma hoa C(t) = m(t) XOR Key(t)
    cout << "--- CAU 2: Ma hoa ---" << endl;
    cout << "Plaintext: " << plaintext << endl << endl;

    cout << "Ky tu\tASCII\tKey\tXOR\tHex\tKy tu ma" << endl;
    cout << "-----\t-----\t---\t---\t---\t--------" << endl;

    for (int i = 0; i < 13; i++) {
        int m = (unsigned char)plaintext[i];
        int c = m ^ keystream[i];
        cout << plaintext[i] << "\t" << m << "\t" << keystream[i] << "\t" << c << "\t0x" << hex << uppercase << c << dec << "\t" << (char)c << endl;
    }

    cout << endl << "Ban ma (hex): ";
    for (int i = 0; i < 13; i++) {
        int c = (unsigned char)plaintext[i] ^ keystream[i];
        cout << "0x" << hex << uppercase << c << " ";
    }
    cout << dec << endl;

    cout << "Ban ma (ky tu): ";
    for (int i = 0; i < 13; i++) {
        int c = (unsigned char)plaintext[i] ^ keystream[i];
        cout << (char)c;
    }
    cout << endl;

    // Kiem tra giai ma
    cout << endl << "Giai ma kiem tra: ";
    for (int i = 0; i < 13; i++) {
        int c = (unsigned char)plaintext[i] ^ keystream[i];
        cout << (char)(c ^ keystream[i]);
    }
    cout << endl;

    return 0;
}
