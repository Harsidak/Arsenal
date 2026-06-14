#include <stdio.h>
#include <stdlib.h>

int top3_len[200005][3];
int top3_id[200005][3];

int head[200005];
int to[200005];
int nxt[200005];
int edge_cnt = 0;

int parent_of[200005];

int max_sent_to_parent[200005];
int max_sent_to_child[200005];
int max_general_sent_to_children[200005]; 

int *queue_from;
int *queue_to;
int *queue_len;
int qu_h = 0, q_tail = 0;

int global_max_second_path = -1;

int main() {
    int num_queries;
    if (scanf("%d", &num_queries) != 1) return 0;
    
    queue_from = malloc(sizeof(int) * 5000000);
    queue_to = malloc(sizeof(int) * 5000000);
    queue_len = malloc(sizeof(int) * 5000000);
    
    for (int i = 1; i <= num_queries + 1; i++) {
        for (int j = 0; j < 3; j++) {
            top3_len[i][j] = 0;
            top3_id[i][j] = -1;
        }
        head[i] = -1;
        max_general_sent_to_children[i] = -1;
        max_sent_to_parent[i] = -1;
        max_sent_to_child[i] = -1;
    }
    
    for (int i = 0; i < num_queries; i++) {
        int p; 
        scanf("%d", &p);
        
        int u = i + 2; 
        parent_of[u] = p;
        
        to[edge_cnt] = u;
        nxt[edge_cnt] = head[p];
        head[p] = edge_cnt++;
        
        queue_from[q_tail] = u;
        queue_to[q_tail] = p;
        queue_len[q_tail] = 1;
        q_tail++;
        
        int path_from_p_to_u;
        if (u == top3_id[p][0]) {
            path_from_p_to_u = top3_len[p][1] + 1;
        } else {
            path_from_p_to_u = top3_len[p][0] + 1;
        }
        
        if (path_from_p_to_u > max_sent_to_child[u]) {
            max_sent_to_child[u] = path_from_p_to_u;
            queue_from[q_tail] = p;
            queue_to[q_tail] = u;
            queue_len[q_tail] = path_from_p_to_u;
            q_tail++;
        }
        
        while (qu_h < q_tail) {
            int from_neighbor = queue_from[qu_h];
            int current_node = queue_to[qu_h];
            int new_length = queue_len[qu_h];
            qu_h++;
            
            int old_top3_id[3];
            for (int k = 0; k < 3; k++) old_top3_id[k] = top3_id[current_node][k];
            
            int found_idx = -1;
            for (int k = 0; k < 3; k++) {
                if (top3_id[current_node][k] == from_neighbor) {
                    found_idx = k;
                    break;
                }
            }
            
            if (found_idx != -1) {
                if (new_length > top3_len[current_node][found_idx]) {
                    top3_len[current_node][found_idx] = new_length;
                } else {
                    continue; 
                }
            } else {
                if (new_length > top3_len[current_node][2]) {
                    top3_len[current_node][2] = new_length;
                    top3_id[current_node][2] = from_neighbor;
                } else {
                    continue; 
                }
            }
            
            for (int k = 0; k < 2; k++) {
                for (int j = k + 1; j < 3; j++) {
                    if (top3_len[current_node][k] < top3_len[current_node][j]) {
                        int temp_len = top3_len[current_node][k];
                        top3_len[current_node][k] = top3_len[current_node][j];
                        top3_len[current_node][j] = temp_len;
                        
                        int temp_id = top3_id[current_node][k];
                        top3_id[current_node][k] = top3_id[current_node][j];
                        top3_id[current_node][j] = temp_id;
                    }
                }
            }
            
            if (top3_len[current_node][1] > global_max_second_path) {
                global_max_second_path = top3_len[current_node][1];
            }
            
            if (current_node != 1) { 
                int p_node = parent_of[current_node];
                int best_path;
                
                if (p_node == top3_id[current_node][0]) {
                    best_path = top3_len[current_node][1] + 1;
                } else {
                    best_path = top3_len[current_node][0] + 1;
                }
                
                if (best_path > max_sent_to_parent[current_node]) {
                    max_sent_to_parent[current_node] = best_path;
                    queue_from[q_tail] = current_node;
                    queue_to[q_tail] = p_node;
                    queue_len[q_tail] = best_path;
                    q_tail++;
                }
            }
            
            int general_best_path = top3_len[current_node][0] + 1;
            
            if (general_best_path > max_general_sent_to_children[current_node]) {
                max_general_sent_to_children[current_node] = general_best_path;
                
                for (int e = head[current_node]; e != -1; e = nxt[e]) {
                    int child = to[e];
                    int path_to_send;
                    
                    if (child == top3_id[current_node][0]) {
                        path_to_send = top3_len[current_node][1] + 1;
                    } else {
                        path_to_send = top3_len[current_node][0] + 1;
                    }
                    
                    if (path_to_send > max_sent_to_child[child]) {
                        max_sent_to_child[child] = path_to_send;
                        queue_from[q_tail] = current_node;
                        queue_to[q_tail] = child;
                        queue_len[q_tail] = path_to_send;
                        q_tail++;
                    }
                }
            } else {
                int children_to_check[6];
                int num_to_check = 0;
                
                for (int k = 0; k < 3; k++) {
                    if (old_top3_id[k] != -1 && old_top3_id[k] != parent_of[current_node]) {
                        children_to_check[num_to_check++] = old_top3_id[k];
                    }
                    if (top3_id[current_node][k] != -1 && top3_id[current_node][k] != parent_of[current_node]) {
                        children_to_check[num_to_check++] = top3_id[current_node][k];
                    }
                }
                
                for (int k = 0; k < num_to_check; k++) {
                    int child = children_to_check[k];
                    
                    int is_duplicate = 0;
                    for (int j = 0; j < k; j++) {
                        if (children_to_check[j] == child) {
                            is_duplicate = 1;
                            break;
                        }
                    }
                    if (is_duplicate) continue;
                    
                    int path_to_send;
                    if (child == top3_id[current_node][0]) {
                        path_to_send = top3_len[current_node][1] + 1;
                    } else {
                        path_to_send = top3_len[current_node][0] + 1;
                    }
                    
                    if (path_to_send > max_sent_to_child[child]) {
                        max_sent_to_child[child] = path_to_send;
                        queue_from[q_tail] = current_node;
                        queue_to[q_tail] = child;
                        queue_len[q_tail] = path_to_send;
                        q_tail++;
                    }
                }
            }
        }
        
        qu_h = 0;
        q_tail = 0;
        
        int ans = global_max_second_path + 2; 
        printf("%d ", ans);
    }
    printf("\n");
    
    return 0;
}