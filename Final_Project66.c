/******************************************************************************

Welcome to GDB Online.
  GDB online is an online compiler and debugger tool for C, C++, Python, PHP, Ruby, 
  C#, OCaml, VB, Perl, Swift, Prolog, Javascript, Pascal, COBOL, HTML, CSS, JS
  Code, Compile, Run and Debug online from anywhere in world.

*******************************************************************************/
#include <stdio.h>
int sum(int a, int b);
int sub(int a, int b);
int con = 0;
int stock[4] = {50,50,50,50};

int main()
{
    int h = 0;
    for(h;con ==0 || con ==1;h++){
    int num1 = 10;
    int num2 = 15;
    int num3 = 20;
    int num4 = 25;
    int mode,result,change,number,select;
    int s = 0;
    int money1 = 0;
    int h = 0;
    result = 0;
    change = 0;
    money1 = 0;
    int money[20] = {0};
    printf("\nSelect the option\n1.order your water\n2.check the quantity\n");
    printf("\nPlease Enter number : ");
    scanf("%d", &select);
    switch(select)
    {
        case 1:
                printf("----------------------------");
                printf("\n|      Choose a mode:      |\n| 1.Water 10 Bath          |\n| 2.Coke 15 Bath           |\n| 3.Vitminwater 20 Bath    |\n| 4.Oishi Greentea 25 Bath |\n");
                printf("----------------------------\n\n");
                printf("*************************************");
                int e = 0;
                for(e;mode<1 || mode >4; e++){
                    printf("*************************************");
                    printf("\nChoose mode : ");
                    scanf("%d", &mode);
                }
                switch(mode)
                {
                    case 1:
                        printf("\nEnter quantity of bottles(1-5):");
                        scanf("%d", &number);
                        int i = 0;
                        for(i=0;number>5;i++){
                            printf("\nPlease Enter number 1-5\n");
                            printf("\nEnter quantity of bottles(1-5):");
                            scanf("%d", &number);
                        }
                        if(number<=stock[0]){
                            stock[0] -=number;
                        if(number<=5){
                            result = sum(num1,number);
                            printf("\ntotal : %d\n",result);
                            printf("\nInput money : ");
                            scanf("%d", &money[0]);
                            int result1 = sum(num1,number);
                        for(s; money[s] < result1; s++){
                            int addMoney = sub(result1,money[s]);
                            printf("\nPlease add more money\n");
                            printf("\nThe amount to be added : %d\n", addMoney);
                            printf("\nInput money : ");
                            scanf("%d", &money[s + 1]);
                            result1 = result1-money[s];
                        }
                        }
                        for(int m =0 ; m<=s ;m++){
                        money1 = money1+money[m];
                        }
                        change = sub(money1,result);
                        printf("\nchange : %d\n",change);
                        printf("********** T H A N K Y O U **********\n");
                        }else{
                            printf("NOT ENOUGH");
                        }
                        break;
                    case 2:
                        printf("\nEnter quantity of bottles(1-5):");
                        scanf("%d", &number);
                        int j = 0;
                        for(j=0;number>5;j++){
                            printf("\nPlease Enter number 1-5\n");
                            printf("\nEnter quantity of bottles(1-5):");
                            scanf("%d", &number);
                        }
                        if(number<=stock[1]){
                            stock[1] -=number;
                        if(number<=5){
                            result = sum(num2,number);
                            printf("\ntotal : %d\n",result);
                            printf("\nInput money : ");
                            scanf("%d", &money[0]);
                            int result1 = sum(num2,number);
                            for(s; money[s] < result1; s++){
                                int addMoney = sub(result1,money[s]);
                                printf("\nPlease add more money\n");
                                printf("\nThe amount to be added : %d\n", addMoney);
                                printf("\nInput money : ");
                                scanf("%d", &money[s + 1]);
                                result1 = result1-money[s];
                            }
                            }
                            for(int m =0 ; m<=s ;m++){
                                money1 = money1+money[m];
                            }
                            change = sub(money1,result);
                            printf("\nchange : %d\n",change);
                            printf("********** T H A N K Y O U **********\n");
                            }else{
                                printf("NOT ENOUGH");
                            }
                        break;
                    case 3:
                        printf("\nEnter quantity of bottles(1-5):");
                        scanf("%d", &number);
                        int k = 0;
                        for(k=0;number>5;k++){
                            printf("\nPlease Enter number 1-5\n");
                            printf("\nEnter quantity of bottles(1-5):");
                            scanf("%d", &number);
                        }
                        if(number<=stock[2]){
                            stock[2] -= number;
                            if(number<=5)
                        {
                        result = sum(num3,number);
                        printf("\ntotal : %d\n",result);
                        printf("\nInput money : ");
                        scanf("%d", &money[0]);
                        int result1 = sum(num3,number);
                        for(s; money[s] < result1; s++){
                            int addMoney = sub(result1,money[s]);
                            printf("\nPlease add more money\n");
                            printf("\nThe amount to be added : %d\n", addMoney);
                            printf("\nInput money : ");
                            scanf("%d", &money[s + 1]);
                            result1 = result1-money[s];
                        }
                        }
                        for(int m =0 ; m<=s ;m++){
                            money1 = money1+money[m];
                        }
                        change = sub(money1,result);
                        printf("\nchange : %d\n",change);
                        printf("********** T H A N K Y O U **********\n");
                        }else{
                            printf("NOT ENOUGH");
                        }  
                        break;
                    case 4:
                        printf("\nEnter quantity of bottles(1-5):");
                        scanf("%d", &number);
                        int l = 0;
                        for(l=0;number>5;l++){
                            printf("\nPlease Enter number 1-5\n");
                            printf("\nEnter quantity of bottles(1-5):");
                            scanf("%d", &number);
                        }
                        if(number<=stock[3]){
                            stock[3] -= number;
                        if(number<=5){
                            result = sum(num4,number);
                            printf("\ntotal : %d\n",result);
                            printf("\nInput money : ");
                            scanf("%d", &money[0]);
                            int result1 = sum(num4,number);
                            for(s; money[s] < result1; s++){
                                int addMoney = sub(result1,money[s]);
                                printf("\nPlease add more money\n");
                                printf("\nThe amount to be added : %d\n", addMoney);
                                printf("\nInput money : ");
                                scanf("%d", &money[s + 1]);
                                result1 = result1-money[s];
                            }
                        }
                        for(int m =0 ; m<=s ;m++){
                            money1 = money1+money[m];
                        }
                        change = sub(money1,result);
                        printf("\nchange : %d\n",change);
                        printf("********** T H A N K Y O U **********\n");
                        }else{
                            printf("NOT ENOUGH");
                        }
                        break;
                }
            break;
        case 2:
            printf("----------------------------");
            printf("\n|      Choose a mode:      |\n| 1.Water            : %d  |\n| 2.Coke             : %d  |\n| 3.Vitminwater      : %d  |\n| 4.Oishi Greentea   : %d  |\n", stock[0], stock[1], stock[2], stock[3]);
            printf("----------------------------\n\n");
    }
    printf("\n\n");
    printf("Do you need a receipt?(YES = 1, NO = 0) : ");
    int receipt;
    scanf("%d", &receipt);
    printf("\n\n");
    if(receipt == 1){
        char name[50];
        printf("Please Enter Your Name and Surname : ");
        while(getchar()!= '\n');
        fgets(name ,sizeof(name), stdin);
        printf("\n\n");
        printf("______________________________________\n");
        printf("|          BANGKOK UNIVERSITY\t      |\n");
        printf("       %s",name);
        printf("|  _________________________________  |\n");
        printf("|   Number of bottles : %d             |\n", number);
        printf("|   Total Price is    : %d            |\n", result);
        printf("|   Money you put in  : %d            |\n", money1);
        printf("|   Change is         : %d             |\n", change);
        printf("|********** T H A N K Y O U **********|\n");
        printf("\n\n");
    }else if(receipt == 0){
        printf("|********** T H A N K Y O U **********|\n");
    }
    printf("\nPlease Enter 1 to order your Water : \nPlease enter 2 do you want to reset : \n");
    scanf("%d", &con);
    }if(con == 2){
        printf("\n********** T H A N K Y O U **********\n");
    }
}

int sum(int a, int b){
    int Fn1;
    Fn1 = a*b;
    return Fn1;
}

int sub(int a, int b){
    int Fn2;
    Fn2 = a-b;
    return Fn2;
}










