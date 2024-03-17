def dfs(start_idx, path):
    if is_leaf(start_idx):
        report(path)
        return
    for edge in get_edges(start_idx):
        path.add(edge)
        dfs(start_idx + 1, path)
        path.pop()

    return report


def dfs_v_1_1(start_idx, path):
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
