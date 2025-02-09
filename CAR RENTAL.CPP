#include <iostream>
#include <unistd.h> // For sleep()
using namespace std;

class A {
public:
    string car[10];
    int money[10];
    int n;

    void getdata() {
        cout << "ENTER THE NUMBER OF CARS YOU WANT TO ADD: ";
        cin >> n;
        for (int i = 0; i < n; i++) {
            cout << "Enter the name of the car: ";
            cin >> car[i];
            cout << "Enter the price for the car: ";
            cin >> money[i];
        }
    }

    void showdata() {
        for (int i = 0; i < n; i++) {
            cout << i + 1 << ". " << car[i] << " -------------> Rs. " << money[i] << endl;
        }
    }

    void replacecar(string oldVal, string newVal) {
        for (int i = 0; i < n; i++) {
            if (car[i] == oldVal) {
                car[i] = newVal;
                cout << oldVal << " replaced with " << newVal << " in the list." << endl;
                return;
            }
        }
        cout << oldVal << " not found in the list." << endl;
    }

    void replacemoney(int oldVal, int newVal) {
        for (int i = 0; i < n; i++) {
            if (money[i] == oldVal) {
                money[i] = newVal;
                cout << "Price " << oldVal << " replaced with " << newVal << " in the list." << endl;
                return;
            }
        }
        cout << oldVal << " not found in the list." << endl;
    }
};

class B : public A {
private:
    string name, getcar;
    int licenseid, noofcar, choosencar, getmoney, noofdays, advance, total;

public:
    void detail() {
        cout << "ENTER YOUR NAME: ";
        cin >> name;
        cout << "ENTER YOUR LICENSE ID: ";
        cin >> licenseid;
        cout << "VERIFYING YOUR LICENSE ID..." << endl;
        sleep(2);
    }

    void bill() {
        cout << "PLEASE ENTER THE NUMBER OF THE CAR YOU WANT: ";
        cin >> choosencar;
        cout << "PLEASE ENTER THE NUMBER OF CARS YOU WANT: ";
        cin >> noofcar;
        cout << "ENTER THE NUMBER OF DAYS YOU WANT THE CAR: ";
        cin >> noofdays;
        
        getcar = car[choosencar - 1];
        getmoney = money[choosencar - 1];
        total = getmoney * noofdays * noofcar;

        cout << "THE TOTAL AMOUNT IS: Rs. " << total << endl;
        cout << "ENTER THE ADVANCE PAYMENT AMOUNT: ";
        cin >> advance;
        total -= advance;

        cout << "--------------- PROCESSING YOUR BILL -----------------" << endl;
        sleep(5);

        cout << "|--------------------------------------------------------------------|\n"
             << "|                        CAR RENTAL BILL                             |\n"
             << "|--------------------------------------------------------------------|\n"
             << "| INVOICE NUMBER                         | 1001                      |\n"
             << "| CUSTOMER NAME                          | " << name << "             |\n"
             << "| CAR NAME                               | " << getcar << "           |\n"
             << "| PRICE PER DAY                          | Rs. " << getmoney << "      |\n"
             << "| NUMBER OF CARS                         | " << noofcar << "           |\n"
             << "| NUMBER OF DAYS                         | " << noofdays << "          |\n"
             << "| ADVANCE PAID                           | Rs. " << advance << "       |\n"
             << "|--------------------------------------------------------------------|\n"
             << "| TOTAL PRICE                            | Rs. " << total << "        |\n"
             << "---------------------------------------------------------------------|\n";
    }
};

inline void menu3() {
    cout << "------------------------ THANK YOU FOR USING THE PROGRAM -----------------------------" << endl;
}

int main() {
    B obj;
    while (true) {
        cout << "--------------------------------" << endl
             << "|     WELCOME TO CAR RENTAL    |" << endl
             << "---------------------------------" << endl
             << "|1. ADMIN                      |" << endl
             << "|2. CUSTOMER                   |" << endl
             << "|3. EXIT                        |" << endl
             << "---------------------------------" << endl;
        int variable;
        cout << "Enter a number from the above menu: ";
        cin >> variable;

        if (variable == 1) {
            while (true) {
                cout << "--------------------------------" << endl
                     << "|1. ADD CAR                    |" << endl
                     << "|2. REPLACE CAR AND PRICE       |" << endl
                     << "|3. SHOW CAR                    |" << endl
                     << "|4. EXIT                        |" << endl
                     << "--------------------------------" << endl;
                int admin_variable;
                cout << "Enter a number from the above menu: ";
                cin >> admin_variable;
                if (admin_variable == 1) {
                    obj.getdata();
                } else if (admin_variable == 2) {
                    cout << "--------- HERE IS THE LIST OF CARS WITH PRICE ---------" << endl;
                    sleep(2);
                    obj.showdata();
                    cout << "--------------------------------" << endl
                         << "|1. CHANGE THE NAME OF THE CAR  |" << endl
                         << "|2. CHANGE THE PRICE OF THE CAR |" << endl
                         << "--------------------------------" << endl;
                    int admin_variable2;
                    cout << "Enter a number from the above menu: ";
                    cin >> admin_variable2;
                    if (admin_variable2 == 1) {
                        string oldVal, newVal;
                        cout << "Enter the car name to replace: ";
                        cin >> oldVal;
                        cout << "Enter the new car name: ";
                        cin >> newVal;
                        obj.replacecar(oldVal, newVal);
                    } else if (admin_variable2 == 2) {
                        int oldVal, newVal;
                        cout << "Enter the old price: ";
                        cin >> oldVal;
                        cout << "Enter the new price: ";
                        cin >> newVal;
                        obj.replacemoney(oldVal, newVal);
                    }
                } else if (admin_variable == 3) {
                    obj.showdata();
                } else if (admin_variable == 4) {
                    break;
                } else {
                    cout << "ENTER A CORRECT NUMBER FROM THE MENU" << endl;
                }
            }
        } else if (variable == 2) {
            obj.detail();
            cout << "HERE IS THE LIST OF CARS" << endl;
            sleep(3);
            obj.showdata();
            obj.bill();
        } else if (variable == 3) {
            menu3();
            break;
        } else {
            cout << "ENTER A CORRECT NUMBER FROM THE MENU" << endl;
        }
    }
}
