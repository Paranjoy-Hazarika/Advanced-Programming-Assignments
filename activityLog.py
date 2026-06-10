from typing import List, Dict, Set
from collections import defaultdict
from functools import reduce
import time


def total_time_per_user(logs: List[Dict]) -> Dict[str, float]:
    user_totals = defaultdict(float)

    reduce(
        lambda acc, log: acc.__setitem__(
            log["user"],
            acc.get(log["user"], 0) + log["duration"]
        ) or acc,
        logs,
        user_totals
    )

    return dict(user_totals)


def most_active_users(logs: List[Dict], k: int) -> List[str]:
    totals = total_time_per_user(logs)

    sorted_users = sorted(
        totals.items(),
        key=lambda x: x[1],
        reverse=True
    )

    return [user for user, _ in sorted_users[:k]]


def unique_actions(logs: List[Dict]) -> Set[str]:
    return {log["action"] for log in logs}


if __name__ == "__main__":

    logs = [
        {"user": "user 1", "action": "YouTube", "duration": 30.5},
        {"user": "user 2", "action": "Instagram", "duration": 20},
        {"user": "user 3", "action": "Chrome", "duration": 40},
        {"user": "user 4", "action": "YouTube", "duration": 10},
        {"user": "user 5", "action": "WhatsApp", "duration": 25}
    ]

    start_time = time.perf_counter()

    print("Total time per user:")
    print(total_time_per_user(logs))

    print("\nMost active users:")
    print(most_active_users(logs, 2))

    print("\nUnique actions:")
    print(unique_actions(logs))

    end_time = time.perf_counter()
    print(f"\nExecution Time: {(end_time - start_time) * 1e6:.2f} µs")