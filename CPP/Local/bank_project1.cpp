#include<iostream>
#include<string>
#include <iomanip>
#include<cctype>
#include<vector>
#include<fstream>
#include<limits>
using namespace std;
struct stinfo{
    string accountnumber,pin,name,phon,accountbalance;
    bool markfound=false;
};
const string filename="helloworld.txt";
void Main_Menu();
string readtext(string message){
    string s;
    cout<<message;
    getline(cin>>ws,s);
    return s;
}
string add_line(stinfo client ,string sep){
    string s="";
    s+=client.accountnumber+sep;
    s+=client.pin+sep;
    s+=client.name+sep;
    s+=client.phon+sep;
    s+=client.accountbalance;
    return s;
}
void add_new_data_tofile(stinfo client){
    
    fstream Myfile;
    Myfile.open(filename,ios::out|ios::app);
    if(Myfile.is_open()){
        string line=add_line(client,"//");
        Myfile<<line;
        cout<<endl;
    }Myfile.close();
}
stinfo read_client(string accn){
    stinfo client;
    client.accountnumber=accn;
    client.pin=readtext("enter rpin code :");
    client.name=readtext("enter client name :");
    client.phon=readtext("enter client phone number :");
    client.accountbalance=readtext("enter client balance :");
    return client;
}
void add_actully_client(string accn){
    stinfo client=read_client(accn);
    add_new_data_tofile(client);

}



vector<string>Splitine(string s,string sep){
    int pos=0;
    string word;
    vector<string>vstr;
    while((pos=s.find(sep))!=std::string::npos){
        word=s.substr(0,pos);
        if(!word.empty()){
            vstr.push_back(word);
        }
        s.erase(0,pos+sep.length());
    }if(!s.empty()){
        vstr.push_back(s);
    }
    return vstr;
}
stinfo fromvectortost(string line,string sep){
    stinfo client;
    vector<string>vstr;
    vstr=Splitine(line,sep);
    client.accountnumber=vstr[0];
    client.pin=vstr[1];
    client.name=vstr[2];
    client.phon=vstr[3];
    client.accountbalance=vstr[4];
    return client;

}
vector<stinfo>allclientsvector(){
    vector<stinfo>vclients;
    fstream Myfile;
    Myfile.open(filename,ios::in);
    if(Myfile.is_open())  {
        string line;
        stinfo client;
        while(getline(Myfile,line)){
            client=fromvectortost(line,"//");
            vclients.push_back(client);
        }Myfile.close();
    }return vclients;
}
void print_client_toshow(stinfo client){
    cout<<"|"<<setw(15)<<client.accountnumber
        <<"|"<<setw(10)<<client.pin
        <<"|"<<setw(35)<<client.name
        <<"|"<<setw(12)<<client.phon
        <<"|"<<setw(12)<<client.accountbalance<<"      |"
        <<endl;
}
void show_listofclient()
{
    vector<stinfo>vclients;
    vclients=allclientsvector();
    cout<<"|______________________________________________________________________________________________|\n";
    cout<<"|                                                                                   |\n";
    cout<<"|______________________________________________________________________________________________|\n";
    cout<<"|"<<setw(15)<<"accountnumber"
    <<"|"<<setw(10)<<"pin"
    <<"|"<<setw(35)<<"name"
    <<"|"<<setw(12)<<"phon"
    <<"|"<<setw(12)<<"accountbalance    |"
    <<endl;
    cout<<"|______________________________________________________________________________________________|\n";
    for(stinfo c:vclients){
        print_client_toshow(c);
    }
    cout<<"|______________________________________________________________________________________________|\n";
}


bool searsh_fo_client(vector<stinfo>&vclients,string accn,stinfo &client){
    for(stinfo &c:vclients){
        if(c.accountnumber==accn){
            client=c;
            return true;
        }
    }return false;
}
void print_found_client(stinfo client){
    cout<<"Client data :"<<endl;
    cout<<"account number : "<<client.accountnumber<<endl;
    cout<<"code pin : "<<client.pin<<endl;
    cout<<"name : "<<client.name<<endl;
    cout<<"phone number : "<<client.phon<<endl;
    cout<<"balance $$ : "<<client.accountbalance<<endl;
}
void find_and_show_client(vector<stinfo>vclients,string accn){
    stinfo client;
    if(searsh_fo_client(vclients,accn,client)){
        print_found_client(client);
    }
    else{
        cout<<" client with accounnt number :"<<accn<<" not found\n";
    }
}
void loop_find(){
    vector<stinfo>vclients;
    vclients=allclientsvector();
    cout<<"_____________________________________\n";
    cout<<"            Find a client\n";
    cout<<"______________________________________\n";
    string c="n";
    do
    {
        string accn=readtext("enter the account number :");
        find_and_show_client(vclients,accn);
        cout<<"do you want find mor clients?y/n :";
        cin>>c;
    } while (c=="Y"||c=="y");
    
}


void add_new_daleted_tofile(stinfo client){
    
    fstream Myfile;
    Myfile.open(filename,ios::out);
    if(Myfile.is_open()){
        Myfile<<add_line(client,"//")<<endl;
    }Myfile.close();
}
void mark_as_found(vector<stinfo>&vclients,string accn)
{
    for(stinfo&client:vclients){
        if(client.accountnumber==accn){
            client.markfound=true;
        }
    }
}
void fill_file_without_deleted(vector<stinfo>&vclients)
{
    fstream Myfile;
    Myfile.open(filename, ios::out); 
    if(Myfile.is_open()){
        for(stinfo &c : vclients){
            if(!c.markfound){ 
                Myfile << add_line(c, "//") << endl;
            }
        }
        Myfile.close();
    }
}

void delete_choisen(vector<stinfo>&vclients,string accn){
    stinfo client;
    string answer="y";
    if(searsh_fo_client(vclients,accn,client)){
        print_found_client(client);
        cout<<"are you sure to delete thise client y/n :";
        cin>>answer;
        if(answer=="Y"||answer=="y"){
            mark_as_found(vclients,accn);
            fill_file_without_deleted(vclients);
            vclients=allclientsvector();
            cout<<"client deleted successfully!! \n";
        }
        
    }else{
        cout<<" client with accounnt number :"<<accn<<" not found\n";
    }
    
}
void loop_delete(){
    vector<stinfo>vclients;
    vclients=allclientsvector();
    cout<<"_____________________________________\n";
    cout<<"            Delete a client\n";
    cout<<"______________________________________\n";
    string c="y";
    do
    {
        string accn=readtext("enter the account number :");
        delete_choisen(vclients,accn);
        cout<<"do you want delete more clients?y/n :";
        cin>>c;
    } while (c=="Y"||c=="y");
}


void read_updated_client(vector<stinfo>&vclients,string accn){ 
    for(stinfo &client:vclients){
        if(client.accountnumber==accn){
            client.pin=readtext("enter pin code :");
            client.name=readtext("enter client name :");
            client.phon=readtext("enter client phone number :");
            client.accountbalance=readtext("enter client balance :");
            break;
        }
    }   
}
void updated_client(vector<stinfo>&vclients,string accn){
    stinfo client;
    string answer="y";
    if(searsh_fo_client(vclients,accn,client)){
        print_found_client(client);
        cout<<"are you sure to update thise client y/n :";
        cin>>answer;
        if(answer=="Y"||answer=="y"){
            read_updated_client(vclients,accn);
            fill_file_without_deleted(vclients);
            vclients=allclientsvector();
            cout<<"client updated successfully!! \n";
        }
    }else{
        cout<<" client with accounnt number :"<<accn<<" not found\n";
    }
}
void loop_update(){
    vector<stinfo>vclients;
    vclients=allclientsvector();
    cout<<"_____________________________________\n";
    cout<<"            Add client\n";
    cout<<"______________________________________\n";
    string c="y";
    do
    {
        string accn=readtext("enter the account number :");
        updated_client(vclients,accn);
        cout<<"do you want update mor clients?y/n :";
        cin>>c;
    } while (c=="Y"||c=="y");
}



void  check_for_add(vector<stinfo>&vclients,string accn){
    stinfo client;
    if(!searsh_fo_client(vclients,accn,client)){
        add_actully_client(accn);
        cout<<"client added successfully !!\n";
    }
    else{
        cout<<"the client is exist in the servise!!\n";
    }
    
}
void loop_add(){
    vector<stinfo>vclients;
    vclients=allclientsvector();
    cout<<"______________________________________\n";
    cout<<"            Add a client\n";
    cout<<"______________________________________\n";
    string c="y";
    do
    {
        string accn=readtext("enter the account number :");
        check_for_add(vclients,accn);
        cout<<"do you want add mor clients?y/n :";
        cin>>c;
    } while (c=="Y"||c=="y");
}




void goback_to_menu(){
    cout << "\n\nPress enter key to go back to Main Menue...";
    cin.ignore(1,'\n');
    cin.get();  // تنتظر إدخال Enter
    
    Main_Menu();
}
void final_edit(){
    short choise;
    
    
    do
    {
        
        cout<<"enter your choice :";
        cin>>choise;
        if(choise==1){
            system("clear");
            show_listofclient();
            goback_to_menu();
            
            continue;
        }
        else if(choise==2){
            system("clear");
            loop_add();
            goback_to_menu();
            continue;
        }
        if(choise==3){
            system("clear");
            loop_delete();
            goback_to_menu();
            continue;
        }
        if(choise==4){
            system("clear");
            loop_update();
            goback_to_menu();
            continue;
        }
        if(choise==5){
            system("clear");
            loop_find();
            goback_to_menu();
            continue;
        }
        if(choise==6){
            break;
        }
        
    } while (choise!=6);
    cout<<"=====================================\n";
    cout<<"            ****END***\n";
    cout<<"=====================================\n";



}
void Main_Menu(){
    cout<<"\n__________________MENU________________\n";
    cout<<"1:show list of clients\n";
    cout<<"2:add new cliens \n";
    cout<<"3:delete a client \n";
    cout<<"4:update a client\n";
    cout<<"5:find a client\n";
    cout<<"6:exit\n";
    cout<<"__________________________________\n";
    
    final_edit();

}
int main(){
    
    system("clear");
    Main_Menu();
}