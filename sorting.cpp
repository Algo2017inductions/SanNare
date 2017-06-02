//Sandip Nair 106116078
#include <iostream>

//insertion sort algorithm

using namespace std;

class array
{
    int *ar,n;
    public:
    array()
    {
        ar = nullptr;
        n = 0;
    }
    array(int x)
    {
        n = x;
        ar = new int[n];
    }
    void accept()
    {
        for(int i = 0;i<n;++i)
            cin>>ar[i];
    }
    void display()
    {
        for(int i = 0;i<n;++i)
            cout<<ar[i]<<"\t";
        cout<<endl;
    }
    void insertionSort()
    {
        for(int i = 1;i<n;i++)
        {
            int x = ar[i],j;
            for(j = i-1;j >= 0 && ar[j] > x;j--)
                ar[j+1] = ar[j];
            ar[j+1] = x;
        }
    }
};

int main()
{
    int n;
    cout<<"Enter the number of integers:"<<endl;
    cin>>n;
    array a1(n);
    cout<<"Enter "<<n<<" integers for the array:"<<endl;
    a1.accept();
    a1.insertionSort();
    cout<<"The sorted array is:"<<endl;
    a1.display();
    return 0;
}
