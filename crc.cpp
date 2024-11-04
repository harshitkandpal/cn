#include <iostream>
#include <string>

using namespace std;

// Function to compute CRC
string calculateCRC(string data, string divisor) {
    int dataLen = data.length();
    int divisorLen = divisor.length();
    
    // Append zeros to the data equal to the divisor length - 1
    string temp = data;
    temp.append(divisorLen - 1, '0');

    for (int i = 0; i <= dataLen - 1; i++) {
        // Perform XOR if the leading bit is 1
        if (temp[i] == '1') {
            for (int j = 0; j < divisorLen; j++) {
                temp[i + j] = temp[i + j] == divisor[j] ? '0' : '1'; // XOR operation
            }
        }
    }
    
    // The remainder is the CRC
    return temp.substr(dataLen, divisorLen - 1);
}

int main() {
    string data;
    string divisor;
    
    cout << "Enter the data in binary: ";
    cin >> data;
    
    cout << "Enter the divisor (generator polynomial) in binary: ";
    cin >> divisor;
    
    string crc = calculateCRC(data, divisor);
    cout << "CRC: " << crc << endl;
    
    // The transmitted data is data + CRC
    cout << "Transmitted data: " << data + crc << endl;
    
    return 0;
}
