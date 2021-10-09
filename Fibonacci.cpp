/* # Fibonacci Zahlen

Die Fibonacci Zahlen sind rekursiv definiert durch:
F(0) = 0
F(1) = 1
F(i) = F(i-1) + F(i-2) für i >= 2


Als Eingabe erhält ihr Programm eine Reihe von Zahlen kleiner oder gleich 5000 (eine Zahl pro Zeile). Für jede dieser Zahlen 
soll Ihr Programm die zugehörige Fibonacci Zahl berechnen und auf einer Zeile ausgeben.

Beispiel Eingabe:
5
7
11

Beispiel Ausgabe:
Die Fibonacci Zahl für 5 ist: 5
Die Fibonacci Zahl für 7 ist: 13
Die Fibonacci Zahl für 11 ist: 89
*/

#include <iostream>
using namespace std;

int fibonacci(int i)
{
    int Fib = 0;

    if (i >= 2)
    {
        Fib = fibonacci(i - 1) + fibonacci(i - 2);
    }
    else if (i == 1)
    {
        Fib = 1;
    }
    else
    {
        Fib = 0;
    }

    return Fib;
}

int main()
{
    int i, j;
    

    while(true)
    {
        cout << "Please enter a positive integer value: \n";
        string line;

        if(not getline(cin, line) or line.empty())
            break;

        i = stoi(line);
        if (i < 0)
        {
            cout << "Please input a positive integar number instead of" << i << ".\n";
        }
        else
        {
            j = fibonacci(i);
            cout << "Die Fibonacci Zahl für " << i << " is: " << j << ".\n";
        }
    }
        
    return 0;
}