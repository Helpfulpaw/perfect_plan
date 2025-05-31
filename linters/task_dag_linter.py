#!/usr/bin/env python3
"""Check that tasks form a DAG and documentation is consistent."""
import os
import re
import sys
from collections import defaultdict, deque

PLAN_PATH = os.path.join('docs', 'planning', 'PROJECT_PLAN.md')
TASKS_DIR = 'tasks'

# Extract task numbers from project plan
TASK_PATTERN = re.compile(r"^\|\s*(\d+)\s+\|")

def parse_tasks():
    ids = []
    with open(PLAN_PATH, 'r', encoding='utf-8') as f:
        for line in f:
            m = TASK_PATTERN.match(line)
            if m:
                ids.append(int(m.group(1)))
    return ids

# Extract dependencies from followups files
DEP_PATTERN = re.compile(r"Depends on:\s*([0-9, ]+)", re.IGNORECASE)

def parse_deps(task_id):
    path = os.path.join(TASKS_DIR, f"task_{task_id:02d}", 'followups.md')
    deps = []
    if os.path.exists(path):
        with open(path, 'r', encoding='utf-8') as f:
            for line in f:
                m = DEP_PATTERN.search(line)
                if m:
                    parts = re.split(r"[, ]+", m.group(1).strip())
                    for p in parts:
                        if p.isdigit():
                            deps.append(int(p))
    return deps

# Topological check

def check_dag(ids, dependencies):
    indeg = {i: 0 for i in ids}
    graph = defaultdict(list)
    for t, deps in dependencies.items():
        for d in deps:
            if d not in ids:
                raise ValueError(f"Task {t} depends on unknown task {d}")
            graph[d].append(t)
            indeg[t] += 1
    # Kahn's algorithm
    q = deque([i for i in ids if indeg[i] == 0])
    visited = []
    while q:
        n = q.popleft()
        visited.append(n)
        for v in graph[n]:
            indeg[v] -= 1
            if indeg[v] == 0:
                q.append(v)
    if len(visited) != len(ids):
        raise ValueError('Cycle detected in task dependencies')


def main():
    ids = parse_tasks()
    if ids != sorted(ids) or ids != list(range(ids[0], ids[-1] + 1)):
        print('Task numbers in project plan are not sequential')
        sys.exit(1)
    deps = {i: parse_deps(i) for i in ids}
    try:
        check_dag(ids, deps)
    except ValueError as e:
        print(str(e))
        sys.exit(1)
    print('Task DAG OK')

if __name__ == '__main__':
    main()
