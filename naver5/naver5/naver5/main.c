#include <stdio.h> 
#include <stdlib.h> 
#include <string.h> 
typedef
struct student {
    char* name;
    int id;
    float gpa;
}student_t;
char* str_clone(char* s) {
    char* temp = (char*)malloc(strlen(s) + 1);
    strcpy(temp, s);
    return temp;
}
student_t* getStudent() {
    char namebuf[200];
    int id;
    float gpa;
    if (scanf("%s %d %f", namebuf, &id, &gpa) == 3) {
        student_t* t = (student_t*)malloc(sizeof(student_t));
        t->id = id;
        t->gpa = gpa;
        t->name = str_clone(namebuf);
        return t;
    }
    else {
        return (student_t*)0;
    }
}
/*
void printstudent(student_t * student){
    student_t *thestudents[10];
    int numstu;
    for( numstu = 0; (thestudents[numstu] = getStudent()) != (student_t*)0 ; numstu++){
   }
   for(int i=0 ; i< numstu ; i++){
     printf("%d %s %f\n", thestudents[i]->id, thestudents[i]->name, thestudents[i]->gpa);
  }
}
*/
int main()
{


    
    student_t* kim[10];
    int numstu;
    for (numstu = 0; (kim[numstu] = getStudent()) != (student_t*)0; numstu++) {
    }
    for (int i = 0; i < numstu; i++) {
        printf("%d %s %f\n", kim[i]->id, kim[i]->name, kim[i]->gpa);
    }
    //printstudent(kim); 
    
}