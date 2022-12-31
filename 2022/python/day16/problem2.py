#TODO : read https://www.geeksforgeeks.org/graph-data-structure-and-algorithms

import re
import sys
import time as t
from copy import copy

inf = sys.maxsize

def create_adj_matrix(valve_connections,adj_matrix,name_map) : 
    for key in valve_connections.keys() : 
        adj_matrix[name_map[key]][name_map[key]] = 0
        for ele in valve_connections[key] : 
            adj_matrix[name_map[key]][name_map[ele]] = 1
    return adj_matrix

def floyd_warshall(adj_matrix) : 
    for k in range(len(adj_matrix)) : 
        for i in range(len(adj_matrix)) : 
            for j in range(len(adj_matrix)) : 
                if adj_matrix[i][j] > adj_matrix[i][k] + adj_matrix[k][j] : 
                    adj_matrix[i][j] = adj_matrix[i][k] + adj_matrix[k][j]
    return adj_matrix

# def get_valid_perms(valve_to_open,adj_matrix) : 
#     valid_perms = []
#     for perm in itertools.permutations(valve_to_open) : 
#         valid = True
#         time = 30 
#         elements = []
#         # if adj_matrix[0][perm[0]] > time : 
#         #     valid = False
#         # else :
#         time -= adj_matrix[0][perm[0]]
#         time -= 1
#         for i in range(len(perm)-1) : 
#             # if adj_matrix[perm[i]][perm[i+1]] == inf : 
#             #     valid = False
#             #     break
#             # else :
#             if adj_matrix[perm[i]][perm[i+1]] > time : 
#                 valid = False
#                 break
#             else :
#                 time -= (adj_matrix[perm[i]][perm[i+1]]+1)
#                 elements.append(perm[i])
#         elements.append(perm[-1])
#         yield elements # too much memory to store in a list 
#     yield valid_perms

def get_flow_rate(perm,adj_matrix,flow_rt) : 

    valid = True
    time = 26 
    elements = []
    flow_rate = 0
    if type(perm) != list :
        perm = list(perm)
    if perm!= [] :
        if adj_matrix[0][perm[0]] < time : 
        #     valid = False
        # else :
            time -= adj_matrix[0][perm[0]]
            time -= 1
            flow_rate +=(time*flow_rt[perm[0]])
            for i in range(len(perm)-1) : 
                if adj_matrix[perm[i]][perm[i+1]] == inf : 
                    valid = False
                    break
                else :
                    if adj_matrix[perm[i]][perm[i+1]] > time : 
                        valid = False
                        break
                    else :
                        time -= (adj_matrix[perm[i]][perm[i+1]]+1)
                        flow_rate +=(time*flow_rt[perm[i+1]])
                        elements.append(perm[i])
            elements.append(perm[-1])
    return (elements,flow_rate)
    #yield valid_perms


""" faster permutations , stolen from interwebs """
def generate_open_options(pos, open_valves, time_left,valve_to_open,adj_matrix):
    for next in valve_to_open:
        if next not in open_valves and adj_matrix[pos][next] < time_left:
            open_valves.append(next)
            yield from generate_open_options(
                next, open_valves, time_left - adj_matrix[pos][next] - 1,valve_to_open,adj_matrix
            )
            open_valves.pop()

    yield copy(open_valves)

if __name__ == "__main__" :
    with open("input.txt", 'r') as f:
        raw_input = [x.replace("\n", "") for x in f.readlines()]
        #regex to extract the value connections and flow rate 
        #for "Valve AA has flow rate=0; tunnels lead to valves DD, II, BB"
        flow_rate = {}
        valve_connections = {}
        for ele in raw_input : 
            flow_rate[ele[6:8]] = int(re.search(r"flow rate=(-?\d+)", ele).group(1))
            if "valves" in ele :
                valve_connections[ele[6:8]] = re.search(r"tunnels lead to valves (.*)", ele).group(1).split(", ")
            else : 
                valve_connections[ele[6:8]] = re.search(r"tunnel leads to valve (.*)", ele).group(1).split(", ")
        print(flow_rate)
        print(valve_connections)
        
        #create adj martix 
        name_map = {}
        idx = 0
        valve_connections_arr = sorted(valve_connections.keys())
        for key in valve_connections_arr : 
            name_map[key] = idx
            idx += 1
        print(name_map)
        
        adj_matrix = [[ inf for x in range(len(valve_connections))] for y in range(len(valve_connections))]
        adj_matrix = create_adj_matrix(valve_connections,adj_matrix,name_map)

        #floyd warshall
        adj_matrix = floyd_warshall(adj_matrix)
        print("after floyd warshall")
        for ele in adj_matrix :
            print(ele)

        #valves to open - non zero 
        valve_to_open = [ name_map[k] for k,v in flow_rate.items() if v != 0]
        print(valve_to_open)

        flow_rt = [flow_rate[k] for k in valve_connections_arr]
        print(flow_rt)


        
        time = 26
        ans = 0
        flow_rate_dict = {}
        #start time
        s_time = t.time()
        #bruteforce
        for perm in generate_open_options(0, [], time,valve_to_open,adj_matrix) :
            perm = list(perm)
            elements , flow_rate = get_flow_rate(perm,adj_matrix,flow_rt)
            if elements != [] :
                flow_rate_dict[tuple(elements)] = flow_rate
        mid_time = t.time()
        print("grenerating all permutations flow rate time : ",mid_time-s_time)
        flow_rate_keys = list(flow_rate_dict.keys())
        #print(flow_rate_keys)
        #TODO : optimize this current time ~10min 
        for i in range(len(flow_rate_keys)) : 
            for j in range(i+1,len(flow_rate_keys)) :
                if set(flow_rate_keys[i]).isdisjoint(set(flow_rate_keys[j])) :
                    ans= max(ans,flow_rate_dict[flow_rate_keys[i]]+flow_rate_dict[flow_rate_keys[j]])
        end_time = t.time()
        print("finding max flow rate time : ",end_time-mid_time)

        print(ans)

