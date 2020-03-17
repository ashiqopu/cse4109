#include <bits/stdc++.h>
using namespace std;

#define Bits 64
#define bitstring first
#define fitness second

int mx_gen, pop_size, num_bits;
double p_crossover, p_mutation;

typedef pair<string,int> people;

bool cmpSort(const people x, const people y)
{
    if (x.fitness > y.fitness)
        return true;
    return false;
}

int oneMax(string BitString)
{
    int sum = 0;
    for(int i = 0; i < BitString.size() ; i++){
        if(BitString[i] == '1') sum += 1;
    }
    return sum;
}

string random_bitstring()
{
    string s = "";
    for(int i = 0 ; i < num_bits ; i++){
        double r = ((double) rand() / (RAND_MAX));
        s += (r < 0.5) ? "1" : "0";
    }
    return s;
}

people binary_tournament(vector< people > pops)
{
    int i = rand() % pops.size();
    int j = rand() % pops.size();

    while(j==i) j = rand() % pops.size();

    return (pops[i].fitness > pops[j].fitness) ? pops[i] : pops[j];
}

string point_mutation(string BitString)
{
    string child = "";
    for(int i = 0; i < BitString.size() ; i++){
        char bit = BitString[i];

        if( (double)((rand()*1.0)/(RAND_MAX*1.0)) < p_mutation )
            child += (bit=='1') ? "0" : "1";
        else
            child += bit;
    }

    return child;
}

string crossover(string parent1, string parent2)
{
    if ( (double)((rand()*1.0)/(RAND_MAX*1.0)) >= p_crossover)
        return parent1;

    int point = 1 + (rand()%(parent1.size()-1));

    //cout << parent1 << " :: " << parent2 << endl;
    //cout << "Crossover size: " << parent1.substr(0,point).size() << " :: " <<  parent2.substr(point).size() << endl << endl;
    //cout << "Crossover : " << parent1.substr(0,point) << " :: " <<  parent2.substr(point) << endl << endl;

    return (parent1.substr(0,point) + parent2.substr(point));
}

vector<people> reproduce(vector<people> selected)
{
    vector<people> children;

    for(int i = 0; i < selected.size() ; i++){
        people p1 = selected[i];
        people p2 = ((i%2)==0) ? selected[i+1] : selected[i-1] ;

        if(i == selected.size()-1){
            p2 = selected[0];
        }

        people child;
        child.bitstring = crossover(p1.bitstring, p2.bitstring);
        child.bitstring = point_mutation(child.bitstring);

        //cout << "Mutated Child: " << child.bitstring << endl << endl;

        children.push_back(child);

        if(children.size() >= pop_size) break;
    }

    //cout << endl;

    return children;
}

people Solve()
{
    vector<people> population(pop_size);
    for(int i = 0; i < pop_size ; i++){
        population[i].bitstring = random_bitstring();
        population[i].fitness = oneMax(population[i].bitstring);
    }

    sort(population.begin(), population.end(), cmpSort);

    //for(int i = 0; i < pop_size ; i++){
    //    cout << population[i].bitstring << " :: " << population[i].fitness << endl;
    //}

    people best = population[0];
    // cout << "Best => " << best.bitstring << " :: " << best.fitness << endl << endl;

    for(int i = 0 ; i < mx_gen ; i++){
        vector<people> selected(pop_size);

        for(int j = 0; j < pop_size ; j++){
            selected[j] = binary_tournament(population);
        }

        vector<people> children = reproduce(selected);
        for(int j = 0; j < children.size() ; j++){
            children[j].fitness = oneMax(children[j].bitstring);
        }

        sort(children.begin(), children.end(), cmpSort);

        if(children[0].fitness >= best.fitness){
            best.bitstring = children[0].bitstring;
            best.fitness = children[0].fitness;
        }

        population = children;

        cout << " => gen: " << i+1 << endl;
        cout << "    best fitness: " << best.fitness << " :: best bitstring: " << best.bitstring << endl << endl;

        if(best.fitness == num_bits) break;
    }

    return best;
}

int main()
{
    //freopen("res.txt", "w", stdout);

    num_bits = Bits;
    cout << "Number of Bits: " << num_bits << endl;

    cout << "Enter maximum generations: ";
    cin >> mx_gen;
    //cout << mx_gen;

    cout << "Enter maximum population size: ";
    cin >> pop_size;
    //cout << pop_size;

    cout << "Enter crossover probability [0 to 1]: ";
    cin >> p_crossover;
    //cout << p_crossover;

    cout << "Enter mutation probability [0 to 1]: ";
    cin >> p_mutation;
    //cout << p_mutation;

    p_mutation = (p_mutation*1.0)/(num_bits*1.0);

    cout << endl << endl;

    people best = Solve();

    cout << "> done! Solution: fitness = " << best.fitness << ", BitString = " << best.bitstring <<endl << endl;

    return 0;
}
