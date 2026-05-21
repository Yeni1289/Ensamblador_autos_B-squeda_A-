from __future__ import annotations

from dataclasses import dataclass
from heapq import heappop, heappush
from itertools import permutations
from typing import Dict, List, Tuple

WheelType = str
Company = str
Prices = Dict[Company, Dict[WheelType, int]]
Assignment = Dict[WheelType, Company]


@dataclass
class SearchResult:
    assignment: Assignment
    total_cost: int
    expanded_nodes: int


@dataclass
class PartialEvaluation:
    g_cost: int
    h_cost: int
    f_cost: int
    is_valid: bool
    message: str


def _companies(prices: Prices) -> List[Company]:
    return list(prices.keys())


def _wheel_types(prices: Prices) -> List[WheelType]:
    first_company = _companies(prices)[0]
    return list(prices[first_company].keys())


def assignment_cost(prices: Prices, assignment: Assignment) -> int:
    return sum(prices[company][wheel] for wheel, company in assignment.items())


def admissible_heuristic(
    prices: Prices,
    assigned_wheels: List[WheelType],
    assigned_companies: List[Company],
) -> int:
    wheels = _wheel_types(prices)
    remaining_wheels = [wheel for wheel in wheels if wheel not in assigned_wheels]
    remaining_companies = [c for c in _companies(prices) if c not in assigned_companies]

    if not remaining_wheels:
        return 0

    if not remaining_companies:
        return 10**9

    # Lower bound: sum of the cheapest available price per remaining wheel.
    return sum(min(prices[company][wheel] for company in remaining_companies) for wheel in remaining_wheels)


def evaluate_partial_assignment(prices: Prices, partial: Assignment) -> PartialEvaluation:
    wheels = _wheel_types(prices)

    assigned_wheels = list(partial.keys())
    assigned_companies = list(partial.values())

    if len(set(assigned_companies)) != len(assigned_companies):
        return PartialEvaluation(
            g_cost=0,
            h_cost=0,
            f_cost=0,
            is_valid=False,
            message="Asignacion invalida: una empresa no puede repetirse.",
        )

    if any(wheel not in wheels for wheel in assigned_wheels):
        return PartialEvaluation(
            g_cost=0,
            h_cost=0,
            f_cost=0,
            is_valid=False,
            message="Asignacion invalida: hay tipos de rueda desconocidos.",
        )

    g_cost = assignment_cost(prices, partial)
    h_cost = admissible_heuristic(prices, assigned_wheels, assigned_companies)

    return PartialEvaluation(
        g_cost=g_cost,
        h_cost=h_cost,
        f_cost=g_cost + h_cost,
        is_valid=True,
        message="Asignacion valida.",
    )


def astar_optimal_assignment(prices: Prices) -> SearchResult:
    wheels = _wheel_types(prices)
    companies = _companies(prices)

    start_assignment: Tuple[Tuple[WheelType, Company], ...] = tuple()
    start_used: Tuple[Company, ...] = tuple()
    start_g = 0
    start_h = admissible_heuristic(prices, [], [])

    heap: List[Tuple[int, int, int, Tuple[Tuple[WheelType, Company], ...], Tuple[Company, ...]]] = []
    counter = 0
    heappush(heap, (start_g + start_h, counter, start_g, start_assignment, start_used))

    best_g = {(start_assignment, start_used): 0}
    expanded = 0

    while heap:
        _, _, g_cost, assignment_t, used_t = heappop(heap)
        state_key = (assignment_t, used_t)

        if g_cost > best_g.get(state_key, 10**12):
            continue

        assignment = dict(assignment_t)
        used = set(used_t)

        if len(assignment) == len(wheels):
            return SearchResult(assignment=assignment, total_cost=g_cost, expanded_nodes=expanded)

        expanded += 1

        next_wheel = wheels[len(assignment)]
        for company in companies:
            if company in used:
                continue

            edge_cost = prices[company][next_wheel]
            new_g = g_cost + edge_cost
            new_assignment = tuple(list(assignment_t) + [(next_wheel, company)])
            new_used = tuple(sorted(list(used) + [company]))

            new_key = (new_assignment, new_used)
            if new_g >= best_g.get(new_key, 10**12):
                continue

            assigned_wheels = [wheel for wheel, _ in new_assignment]
            assigned_companies = [company_name for _, company_name in new_assignment]
            h_cost = admissible_heuristic(prices, assigned_wheels, assigned_companies)
            f_cost = new_g + h_cost

            best_g[new_key] = new_g
            counter += 1
            heappush(heap, (f_cost, counter, new_g, new_assignment, new_used))

    raise RuntimeError("No se encontro una solucion valida.")


def brute_force_optimal(prices: Prices) -> SearchResult:
    wheels = _wheel_types(prices)
    companies = _companies(prices)

    best_assignment: Assignment = {}
    best_cost = 10**12

    for perm in permutations(companies, len(wheels)):
        assignment = {wheel: company for wheel, company in zip(wheels, perm)}
        cost = assignment_cost(prices, assignment)
        if cost < best_cost:
            best_cost = cost
            best_assignment = assignment

    return SearchResult(assignment=best_assignment, total_cost=best_cost, expanded_nodes=0)
