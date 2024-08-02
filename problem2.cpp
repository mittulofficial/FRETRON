#include <iostream>
#include <vector>
#include <algorithm>
#include <iomanip>

using namespace std;

// Function to distribute apples
void distributeApples(const vector<int>& appleWeights, double ramContribution, double shamContribution, double rahimContribution) {
    // Calculate total contribution
    double totalContribution = ramContribution + shamContribution + rahimContribution;
    
    // Calculate proportions
    double ramProportion = ramContribution / totalContribution;
    double shamProportion = shamContribution / totalContribution;
    double rahimProportion = rahimContribution / totalContribution;
    
    // Calculate total weight of apples
    int totalWeight = 0;
    for (int weight : appleWeights) {
        totalWeight += weight;
    }
    
    // Calculate target weights for each person
    double ramTarget = ramProportion * totalWeight;
    double shamTarget = shamProportion * totalWeight;
    double rahimTarget = rahimProportion * totalWeight;
    
    vector<int> ramApples, shamApples, rahimApples;
    vector<int> remainingApples = appleWeights;
    
    // Sort apples by weight (descending)
    sort(remainingApples.begin(), remainingApples.end(), greater<int>());
    
    // Distribute apples to Ram, Sham, and Rahim
    for (int weight : remainingApples) {
        if (ramTarget >= weight) {
            ramApples.push_back(weight);
            ramTarget -= weight;
        } else if (shamTarget >= weight) {
            shamApples.push_back(weight);
            shamTarget -= weight;
        } else if (rahimTarget >= weight) {
            rahimApples.push_back(weight);
            rahimTarget -= weight;
        }
    }
    
    // Output the distribution
    cout << "Distribution Result :" << endl;
    cout << "Ram : ";
    for (int weight : ramApples) {
        cout << weight << " ";
    }
    cout << endl;
    
    cout << "Sham : ";
    for (int weight : shamApples) {
        cout << weight << " ";
    }
    cout << endl;
    
    cout << "Rahim : ";
    for (int weight : rahimApples) {
        cout << weight << " ";
    }
    cout << endl;
}

int main() {
    vector<int> appleWeights;
    int weight;
    
    cout << "Enter apple weight in gram (-1 to stop ) : ";
    while (cin >> weight && weight != -1) {
        appleWeights.push_back(weight);
    }
    
    double ramContribution, shamContribution, rahimContribution;
    
    cout << "Enter Ram's contribution: ";
    cin >> ramContribution;
    
    cout << "Enter Sham's contribution: ";
    cin >> shamContribution;
    
    cout << "Enter Rahim's contribution: ";
    cin >> rahimContribution;
    
    distributeApples(appleWeights, ramContribution, shamContribution, rahimContribution);
    
    return 0;
}
