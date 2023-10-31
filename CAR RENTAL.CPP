#include <bits/stdc++.h>
using namespace std;
class A{
    public:
        string car [10];
        int money[10];
        int n;
        int elem,i;
        void getdata(){
            cout<<"ENTER THE NUMBER OF CAR YOU WANT TO ADD :- ";
            cin>>n;
            for (int i=0;i<n;i++){
                        cout<<"Enter the name of the car :- ";
                        cin>>car[i];
                        cout<<"Enter the price for the car :- ";
                        cin>>money[i];
            }  
        }
        void showdata(){
            for (int i=0;i<n;i++){
                        cout<<i+1<<"."<<car[i]<<"------------->"<<money[i]<<endl;
            }
        }
         void replacecar(string oldVal, string newVal) {
            for (int i = 0; i < n; i++) {
                if (car[i] == oldVal) {
                    car[i] = newVal;
                    cout << oldVal << " REPLACES WITH " << newVal << " in the LIST." << endl;
                    return;
                }                                                                                                                      

            }
            cout << oldVal << " NOT FOUND IN THE LIST." << endl;
        }
        void replacemoney(int oldVal, int newVal) {
            for (int i = 0; i < n; i++) {
                if (money[i] == oldVal) {
                    money[i] = newVal;
                    cout << oldVal << " REPLACES WITH " << newVal << " in the LIST." << endl;
                    return;
                }
            }
            cout << oldVal << " NOT FOUND IN THE LIST." << endl;
        }
};
class B : public A{
    private:
        string name,getcar;
        int lisenceid,noofcar,choosencar,getmoney,noofdays,advance,total;
    public:
        void detail(){
            cout<<"ENTER YOUR NAME :- ";
            cin>>name;
            cout<<"ENTER YOUR LISENCE ID :- ";
            cin>>lisenceid;
            cout<<"VERFYING YOUR LISENCE ID......."<<endl;
            sleep(2);
        }
        void bill(){
            cin>>choosencar;
            cout<<"PLEASE ENTER THE NUMBER OF THE CARS YOU WANT :- ";
            cin>>noofcar;
            cout<<"ENTER THE NUMBER OF DAYS YOU WANT THE CAR :- ";
            cin>>noofdays;                                                                                           
            getcar=car[choosencar-1];
            getmoney=money[choosencar-1];
            total=getmoney*noofdays*noofcar;
            cout<<"THE TOTAL AMOUNT IS :- "<<total<<endl;
            cout<<"ENTER THE AMOUNT OF ADVANCE YOU WANT PAY :- ";
            cin>>advance;
            total=total-advance;
            cout<<"---------------PROCESSING YOUR BILL-----------------"<<endl;
            sleep(5);
            cout<<"|--------------------------------------------------------------------|"<<endl
            <<"|                        CAR RENTAL BILL                             |"<<endl
            <<"|--------------------------------------------------------------------|"<<endl
            <<"|INVOICE NUMBER                             |1001                    |"<<endl
            <<"|CUSTOMER NAME                              |"<<name<<"                       |"<<endl
            <<"|NAME OF THE CAR                            |"<<getcar<<"                        |"<<endl
            <<"|PRICE OF THE CAR                           |Rs."<<getmoney<<"                   |"<<endl
            <<"|NUMBER OF THE CAR                          |"<<noofcar<<"                       |"<<endl
            <<"|NUMBER OF DAYS                             |"<<noofdays<<"                       |"<<endl
            <<"|ADVANCE                                    |RS."<<advance<<"                    |"<<endl
            <<"|--------------------------------------------------------------------|"<<endl
            <<"|TOATL PRICE                                |Rs. "<<total<<"                |"<<endl
            <<"---------------------------------------------------------------------|"<<endl;  
        }
        
};
inline void menu3(){
    cout<<"------------------------THANKYOU FOR USING THE PROGRAM-----------------------------"<<endl;
}
int main(){
    B objj;
    while(true){
        cout<<"--------------------------------"<<endl
        <<"|     WELCOME TO CAR  RENTAL    |"<<endl
        <<"---------------------------------"<<endl
        <<"|1.ADMIN                        |"<<endl
        <<"|2.CUSTOMER                     |"<<endl
        <<"|3.EXIT                         |"<<endl
        <<"---------------------------------"<<endl;
        int variable;
        cout<<"Enter a number from the above menu :- ";
        cin>>variable;
        if (variable==1){
            while(true){
                cout<<"--------------------------------"<<endl
                    <<"|1.ADD CAR                     |"<<endl
                    <<"|2.REPLACE CAR AND PRICE       |"<<endl
                    <<"|3.SHOW CAR                    |"<<endl
                    <<"|4.EXIT                        |"<<endl
                    <<"--------------------------------"<<endl;
                int admin_variable;
                cout<<"Enter a number from the above menu :- ";
                cin>>admin_variable;
                if (admin_variable==1){
                    objj.getdata();
                }
                else if(admin_variable==2){
                    int admin_variable2;
                    cout<<"---------HERE IS THE LIST OF CAR WITH PRICE---------"<<endl;
                    sleep(2);
                    objj.showdata();
                    cout<<"--------------------------------"<<endl
                        <<"|1.CHANGE THE NAME OF THE CAR  |"<<endl                          
                        <<"|2.CHANGE THE PRICE OF THE CAR |"<<endl
                        <<"--------------------------------"<<endl;
                    cout<<"Enter a number from the above menu :- ";
                    cin>>admin_variable2;
                    while(true){
                        if (admin_variable2==1){
                            string oldVal, newVal;
                            cout << "Enter the value to replace: ";
                            cin >> oldVal;
                            cout << "Enter the new value: ";
                            cin >> newVal;
                            objj.replacecar(oldVal, newVal);
                            break;
                        }
                        else if(admin_variable2==2){
                            int oldVal, newVal;
                            cout << "Enter the value to replace: ";
                            cin >> oldVal;
                            cout << "Enter the new value: ";
                            cin >> newVal;
                            objj.replacemoney(oldVal, newVal);
                            break;
                        }
                    }
                }
               
                else if (admin_variable==3){
                    objj.showdata();
                }
                else if(admin_variable==4){
                    break;
                }
                else {
                cout<<"ENTER A CORRECT NUMBER FROM THE MENU";
                }                                                                                                                      
        
            }
        }
        else if(variable==2){
            while(true){
                objj.detail();
                cout<<"HERE IS THE LIST OF THE CAR"<<endl;
                sleep(3);
                cout<<"---------------------"<<endl;
                objj.showdata();
                cout<<"---------------------"<<endl;
                cout<<"PLEASE ENTER THE NUMBER OF THE CAR WHICH YOU WANT TO SELECT :- ";
                objj.bill();
                break;
            }
        }
        else if(variable==3){
            menu3();
            break;
        }
        else{
            cout<<"ENTER A CORRECT NUMBER FROM THE MENU"<<endl;
        }
    
    }
}





