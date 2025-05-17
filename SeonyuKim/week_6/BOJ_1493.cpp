#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    long long L, W, H;
    cin >> L >> W >> H;
    int N;
    cin >> N;
    
    map<int,int> counts;
    for (int i=0 ; i <N ; ++i){
        int size_idx, count;
        cin >> size_idx >> count;
        counts[size_idx] = count;
    }

    long long total_cubes = 0;
    long long filled_volume = 0;

    for (int i =19; i >=0; --i){
        long long side = 1LL << i;
        long long cube_volume = side * side * side;

        if (L < side || W < side || H < side) {
            continue;
        }
        long long max_cubes = (L / side) * (W / side) * (H / side);
        long long filled_volume_cur_cube = filled_volume / cube_volume;
        long long available_cubes = max_cubes - filled_volume_cur_cube;

        long long cubes_to_use = min(available_cubes, (long long)counts[i]);
        filled_volume += cubes_to_use * cube_volume;
        total_cubes += cubes_to_use;

    }
    if (filled_volume == L * W * H) {
            cout << total_cubes << "\n";
    }else{
            cout << -1 << "\n";
    }
    
    return 0;
}

