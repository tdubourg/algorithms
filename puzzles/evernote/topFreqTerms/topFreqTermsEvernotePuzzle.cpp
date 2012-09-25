#include "string"
#include "iostream"
#include "map"
#include "vector"

namespace std { using namespace __gnu_cxx; }

using namespace std;
int n, k; // I hate that

struct Tuple {
    string word;
    int occurences;

    Tuple() {
        word = "";
        occurences = -1;
    }

    Tuple(const Tuple& t) {
        word = t.word;
        occurences = t.occurences;
    }

    Tuple(string w, int o) {
        word = w;
        occurences = o;
    }
    
    bool operator >(Tuple other) {
#ifdef DBG
        cout << "> operator" << endl;
#endif
        return (occurences > other.occurences || (occurences == other.occurences && word < other.word));
    }

    bool operator <(Tuple other) {
#ifdef DBG
        cout << "< operator" << endl;
#endif
        return (occurences < occurences || (occurences == other.occurences && word > other.word));
    }
};

Tuple* EMPTY_TUPLE;

map<string, int> freq;
Tuple** kTop;

void try_insert(Tuple* item) {
    // item[0] = word
    // item[1] = occurences

    if (kTop[k] != EMPTY_TUPLE)
    {
        delete kTop[k];
    }
    kTop[k] = item; // Note : This index is not in the "top kTop", it's here because it's handy
    int i = k-1;
    while (i >= 0 && (*item) > (*kTop[i])) {
#ifdef DBG
        cout << "Swapping ! " << endl;
#endif
        // Swap values:
        Tuple* tmp = kTop[i];
        kTop[i] = kTop[i+1];
        kTop[i+1] = tmp;
        // Decrement:
        i -= 1;
    }
}

int main(int argc, char const *argv[])
{
// Grab number of lines:
    cin >> n;
// Count the words
    for (int x = 0; x < n; ++x)
    {
        string s;
        cin >> s;
        freq[s] = freq[s] + 1;
    }

    // Grab the top how many we are interested in
    cin >> k;

    kTop = new Tuple*[k+1];

    EMPTY_TUPLE = new Tuple();
    for (int i = 0; i < (k+1); ++i)
    {
        kTop[i] = EMPTY_TUPLE;
    }

    map<string, int>::iterator it;
    for (it = freq.begin(); it != freq.end(); ++it)
    {
        Tuple* item = new Tuple(it->first, it->second);
        try_insert(item);
    }

    for (int i = 0; i < k; ++i)
    {
        cout << kTop[i]->word << "\n";
    }

    delete EMPTY_TUPLE;

    return 0;
}


