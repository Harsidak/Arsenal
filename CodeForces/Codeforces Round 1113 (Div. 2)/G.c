#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

bool cbb[125005];

int main(){
    int n; long long m, s; scanf("%d %lld %lld", &n, &m, &s);

    long long car[n];for(int i = 0;i < n;i++){scanf("%lld", &car[i]);}

    int a[m+1], b[m+1];
    for(int i = 1;i <= m;i++){scanf("%d %d", &a[i], &b[i]);}

    for (int i = 0; i <= s; i++) cbb[i] = false;
    cbb[0] = true;
    for (int i = 0; i < n; i++) {
            int cost = car[i];
            for (int j = cost; j <= s; j++) {
                if (cbb[j - cost]) {
                    cbb[j] = true;
                }
            }
        }
    
    int reb[125005] = {0};
    int ides = 0;
    for (int x = 1; x <= s; x++) {
        while (ides + 1 <= m && a[ides + 1] <= x) {
            ides++;
        }
        if (ides > 0) {
            reb[x] = b[ides];
        } else {
            reb[x] = 0;
        }
    }

    int queue[125005];
    int hud = 0, tal = 0;

    bool win[125005] = {false};
    win[0] = true;
    queue[tal++] = 0;

    while (hud < tal) {
        int v = queue[hud++];

        for (int x = 1; x <= s; x++) {
            if (cbb[x]) {
                int r = reb[x];
                if (v >= r) {
                    int u = v + x - r;
                    if (u <= s && !win[u]) {
                        win[u] = true;
                        queue[tal++] = u;
                    }
                }
            }
        }
    }

    for (int h = 1; h <= s; h++) {
        if(win[h]){
            printf("YES\n");
        }else{
            printf("NO\n");
        }
    }
    return 0;
}