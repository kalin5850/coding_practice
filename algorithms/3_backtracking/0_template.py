#  basic template
def dfs(start_idx, path):
    if is_leaf(start_idx):
        report(path)
        return
    for edge in get_edges(start_idx):
        path.add(edge)
        dfs(start_idx + 1, path)
        path.pop()

    return report


# prune the branches
def dfs_v_1(start_idx, path):
    if is_leaf(start_idx):
        report(path)
        return

    for edge in get_edge(start_idx):
        # prune the condition
        if not is_valid(edge):
            continue
        path.add(edge)
        dfs(start_idx + len(edge), path)
        path.pop()

    return report


# prune the branches and check state
def dfs_v_2(start_idx, path, [... additional_states]):
    if is_leaf(start_idx):
        report(path)
        return
    
    for edge in get_edge(start_idx, [... additional_states]):
        # prune if needed
        if not is_valid(edge):
            continue
        path.add(edge)
        if additional_states:
            update(... additional_states)
        dfs(start_idx + len(edge), path, [... additional_states])
        # revert(...additional states) if necessary e.g.: permutations
        path.pop()
        
    return

# aggregate
def dfs_v_3(start_idx, [...additional_states]):
    if is_leaf(start_idx):
        return 1
    ans = initial_value
    for edge in get_edge(start_idx, [...additional_states]):
        if additional_states:
            update([...additional_states])
        ans = aggregate(ans, dfs(start_idx + len(edge), [...additional_states]))
        if additional_states:
            revert([...additional_states])
    
    return ans