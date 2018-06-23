#include <string>
#include <vector>
#include <iostream>
#include <fstream>
#include <algorithm>
using std::cout;
using std::string;
using std::vector;
using std::cin;
using std::endl;
using std::sort;
class TrieNode {
 public:
  TrieNode* children[26] = {NULL};
};
class MyTrie {
 public:
  TrieNode *root = new TrieNode();
  void insert(string *s) {
    TrieNode *cur = root;
    TrieNode *next;
    for (char c : (*s)) {
      if (cur->children[c - 'a'] != NULL) {
        next = (cur->children)[c - 'a'];
      } else {
        next = new TrieNode();
        (cur->children)[c - 'a'] = next;
      }
      cur = next;
    }
  }
  bool find(string *s){
     return helper(root, s, 0);
  }
  bool helper(TrieNode* root, string *s, int layer){
    if(layer == s->length()){
      return true;
    }
    if(root->children[(*s)[layer]-'a']!= NULL){
      return helper(root->children[(*s)[layer]-'a'], s, layer+1);
    }
    return false;
  }
};
class Coordinate{
 public:
  int x;
  int y;
  Coordinate(int x, int y){
    this->x = x;
    this->y = y;
  }
};
MyTrie* smallwordlist[30] = {NULL};
MyTrie* largewordlist[30] = {NULL};
int Direction[8][2] =  {{0,1},{1,0},{0,-1},{-1,0},{1,1},{1,-1},{-1,1},{-1,-1}};
bool isValid(vector<vector<char>> *matrix, int x, int y, vector<vector<bool>> *visited){
  return x<matrix->size() && x>=0 && y < (*matrix)[0].size() && y >= 0 && (*matrix)[x][y] != '*' && ((*visited)[x][y] == false);
}
void DFSHelper (vector<vector<bool>> *visited, vector<vector<char>> *matrix, string *pivot, int x,
  int y, vector<vector<Coordinate>> *result, int layer, vector<Coordinate>*list, string *s, MyTrie* wordlist[]){
       if((*pivot)[layer] != '*' && (*matrix)[x][y] != (*pivot)[layer]){
        return;
       }
       if(layer == pivot->length()-1) {
        if(wordlist[pivot->length()]->find(s)){
          vector<Coordinate> temp(*list);
          result->push_back(temp);
          return;
        }
       }
       for(int i=0; i<8; i++) {
        int nextx = x + Direction[i][0];
        int nexty = y + Direction[i][1];
        if(!isValid(matrix, nextx, nexty, visited)){
          continue;
        }
        s->push_back((*matrix)[nextx][nexty]);
        if(wordlist[pivot->length()]->find(s)){
          (*visited)[x][y]=true;
          list->push_back(Coordinate(nextx,nexty));
          DFSHelper(visited, matrix, pivot, nextx, nexty, result, layer+1, list, s, wordlist);
          list->pop_back();
          (*visited)[x][y]=false;
        }
        s->pop_back();
       }
}
void findResult(vector<vector<string>>*result, vector<vector<char>>*matrix, 
  vector<string>*number, int layer, vector<string>*list, MyTrie* wordlist[]){
  if(layer == number->size()){
    vector<string>temp;
    for(string s : (*list)){
      temp.push_back(s);
    }
    result->push_back(temp);
  }
  for(int i=0; i<matrix->size(); i++){
     for(int j=0; j<(*matrix)[0].size(); j++){
      if((*matrix)[i][j] == '*'){
        continue;
      }
      vector<vector<Coordinate>>results;
      vector<vector<bool>> visited(matrix->size(),vector<bool>((*matrix)[0].size(),false));
      string temps;
      temps.push_back((*matrix)[i][j]);
      vector<Coordinate>templist;
      templist.push_back(Coordinate(i,j));
      DFSHelper(&visited, matrix, &(*number)[layer], i, j, &results, 0, &templist, &temps, wordlist);
      if(!results.empty()){
         if(results.size()>1){
            for(int i=0; i<results.size(); i++){
              for(int j=i+1; j<results.size(); j++){
                 string s1,s2;
                 for(Coordinate c: results[i]){
                     s1.push_back((*matrix)[c.x][c.y]);
                 }
                 for(Coordinate c: results[j]){
                     s2.push_back((*matrix)[c.x][c.y]);
                 }
                 if(s1 == s2){
                    results.erase(results.begin()+j);
                    j--;
                 }
               }   
            }
         }
         for(vector<Coordinate> Clist : results){
          string s;
          for(Coordinate c: Clist){
            s.push_back((*matrix)[c.x][c.y]);
          }
          list->push_back(string(s));
          vector<vector<char>>newmatrix(*matrix);
          for(Coordinate c:Clist){
              newmatrix[c.x][c.y]='*';
          }
          for(int i=0; i<newmatrix.size(); i++){
              for(int j=0; j<newmatrix[0].size(); j++){
                 if(i+1 <newmatrix.size() && newmatrix[i+1][j] == '*') {
                    for(int k=i; k>=0 ; k--) {
                     char temp = newmatrix[k][j];
                     newmatrix[k][j] = newmatrix[k+1][j];
                     newmatrix[k+1][j] = temp;
                    }
                }         
            }
          }
          findResult(result, &newmatrix, number, layer+1, list, wordlist);
          list->pop_back();
         }
      }
     }
  }
}
void readfromfile(string s, MyTrie* wordlist[]){
  std::ifstream in(s);
  string line;
  int var;
  while (getline(in, line)) {
    var = line.length();
    if (wordlist[var] == NULL) {
      MyTrie *newtrie = new MyTrie();
      newtrie->insert(&line);
      wordlist[var] = newtrie;
    } else {
      wordlist[var]->insert(&line);
    }
  }
}
int main(int argc, char const *argv[]){
   readfromfile(argv[1],smallwordlist);
   readfromfile(argv[2],largewordlist);
   vector<vector<char>>input;
  string str;
  while(!cin.eof()){
    vector<vector<char>>input;
    getline(cin,str);
    input.push_back(vector<char>());
    for(int i=0; i<str.length(); i++){
     input[0].push_back(str[i]);
    }
    for(int i=0; i<str.length()-1; i++){
     getline(cin,str);
     input.push_back(vector<char>());
     for(int j=0; j<str.length(); j++){
      input[i+1].push_back(str[j]);
     }
    }
    getline(cin,str);
    vector<string>number;
    string buff{""};
    for(auto n:str){
        if(n != ' '){ 
        	buff += n; 
        }
        else if(n == ' ' && buff != ""){
         number.push_back(buff); buff = "";
        }
    }
    if(buff != "") {
     number.push_back(buff);
    }
    vector<vector<string>> result = vector<vector<string>>();
    vector<string>list;
    findResult(&result, &input, &number, 0, &list, smallwordlist);
    if(result.empty()){
      findResult(&result,&input,&number,0, &list, largewordlist);
    }
    if(result.empty()){
      cout<<"."<<endl;
    } else {
      sort(result.begin(), result.end());
      for(vector<string> v : result){
          for(string s : v){
            cout << s << " ";
          }
          cout<<endl;
      }
      cout<<"."<<endl;
    }
  }
  exit(0);
}