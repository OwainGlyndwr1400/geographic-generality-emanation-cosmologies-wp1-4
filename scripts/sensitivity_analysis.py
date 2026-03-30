"""
sensitivity_analysis.py
WP 1.3 -- Sensitivity Analysis & Sub-Clustering

Three analyses:
1. Branching alternatives (Suhrawardi, Zurvanite Bundahishn) -- reclassify and measure impact
2. Sub-clustering within the linear-chain family by node count
3. Full pipeline re-run under branching alternatives (optional)

Usage:
    python sensitivity_analysis.py
"""

import json
import os
import sys
import copy
import numpy as np
import networkx as nx
from itertools import combinations
from collections import defaultdict

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from encode_schemas import load_all_schemas, compute_depth, compute_max_branching

SCHEMAS_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "data", "schemas")
OUTPUTS_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "outputs")
GED_TIMEOUT = 30


def _sep(char="-", width=70):
    print(char * width)


# ---------------------------------------------------------------------------
# Branching alternative builders
# ---------------------------------------------------------------------------

def build_ishraq_branching(schemas):
    """Build Suhrawardi branching alternative: victorial_lights has out-degree 2."""
    G_orig, data = schemas["ishraq_illuminationist"]
    G = G_orig.copy()
    # Remove the single edge victorial_lights -> lords_of_species
    # Add two edges: victorial_lights -> lords_of_species AND victorial_lights -> accidental_lights
    if G.has_edge("victorial_lights", "lords_of_species"):
        G.remove_edge("lords_of_species", "accidental_lights")
        G.add_edge("victorial_lights", "accidental_lights",
                   relationship="emanation",
                   description="Branching alt: longitudinal chain directly generates accidental lights")
    return G


def build_zurvanite_bundahishn(schemas):
    """Build Zurvanite alternative: Zurvan at apex, bifurcating to Ohrmazd + Ahriman."""
    G_orig, data = schemas["bundahishn_zoroastrian"]
    G = G_orig.copy()
    # Add Zurvan as new root
    G.add_node("zurvan", id="zurvan", name="Zurvan (Infinite Time)",
               functional_role="source", level=-1,
               source_reference="Zaehner 1955, Zurvan ch.3")
    # Add Ahriman as dark branch
    G.add_node("ahriman", id="ahriman", name="Ahriman (Angra Mainyu)",
               functional_role="demiurge", level=0,
               source_reference="GBd 1.1-1.6; Zaehner 1955")
    # Reclassify Ohrmazd from source to first_emanation
    G.nodes["ohrmazd"]["functional_role"] = "first_emanation"
    G.nodes["ohrmazd"]["level"] = 0
    # Add edges from Zurvan
    G.add_edge("zurvan", "ohrmazd", relationship="emanation",
               description="Ohrmazd born from Zurvan's sacrifice")
    G.add_edge("zurvan", "ahriman", relationship="fragmentation",
               description="Ahriman born from Zurvan's doubt")
    return G


# ---------------------------------------------------------------------------
# GED computation
# ---------------------------------------------------------------------------

def pairwise_ged(graphs: dict) -> dict:
    """Compute pairwise structural GED for all pairs."""
    names = sorted(graphs.keys())
    matrix = {}
    n = len(names)
    total = n * (n - 1) // 2
    done = 0
    for i in range(n):
        for j in range(i + 1, n):
            a, b = names[i], names[j]
            ged = nx.graph_edit_distance(graphs[a], graphs[b], timeout=GED_TIMEOUT)
            if ged is None:
                ged = float("inf")
            matrix[(a, b)] = ged
            matrix[(b, a)] = ged
            done += 1
            if done % 10 == 0:
                print(f"    GED: {done}/{total} pairs computed...")
    for name in names:
        matrix[(name, name)] = 0.0
    return matrix


# ---------------------------------------------------------------------------
# Topology family classification
# ---------------------------------------------------------------------------

def classify_families(graphs: dict):
    """Classify into linear_chain vs branching_tree by max branching factor."""
    families = {"linear_chain": [], "branching_tree": []}
    for name, G in graphs.items():
        mb = compute_max_branching(G)
        if mb <= 1:
            families["linear_chain"].append(name)
        else:
            families["branching_tree"].append(name)
    return families


def family_stats(families, ged_matrix, all_names):
    """Compute intra-family and inter-family mean GED."""
    def mean_ged(members):
        if len(members) < 2:
            return 0.0
        geds = [ged_matrix[(a, b)] for a, b in combinations(members, 2)]
        return np.mean(geds)

    chains = families.get("linear_chain", [])
    branches = families.get("branching_tree", [])

    intra_chain = mean_ged(chains)
    intra_branch = mean_ged(branches)

    # Inter-family
    inter_geds = [ged_matrix[(a, b)] for a in chains for b in branches]
    inter = np.mean(inter_geds) if inter_geds else 0.0

    # Separation ratio
    min_intra = min(intra_chain, intra_branch) if (intra_chain > 0 and intra_branch > 0) else max(intra_chain, intra_branch)
    sep_ratio = inter / min_intra if min_intra > 0 else float("inf")

    return {
        "intra_chain": round(intra_chain, 4),
        "intra_branch": round(intra_branch, 4),
        "inter_family": round(inter, 4),
        "separation_ratio": round(sep_ratio, 4),
        "n_chains": len(chains),
        "n_branches": len(branches),
    }


# ---------------------------------------------------------------------------
# Sub-clustering analysis
# ---------------------------------------------------------------------------

def subclustering_analysis(schemas, ged_matrix):
    """
    Sub-clustering within the linear-chain family by node count.
    Tests whether {5-node chains} and {7-8-node chains} form distinct sub-clusters.
    """
    print("\n  SUB-CLUSTERING WITHIN LINEAR-CHAIN FAMILY")
    _sep()

    # Get linear chains
    chains = []
    for name, (G, _) in schemas.items():
        if compute_max_branching(G) <= 1:
            chains.append((name, G.number_of_nodes()))

    chains.sort(key=lambda x: x[1])
    print(f"  Linear chains ({len(chains)} members):")
    for name, n in chains:
        print(f"    {name:<35} N={n}")

    # Define sub-clusters by node count
    small = [name for name, n in chains if n <= 6]  # 5-6 nodes
    large = [name for name, n in chains if n >= 7]   # 7-8 nodes

    print(f"\n  Sub-cluster A (N<=6, 'compact'): {small}")
    print(f"  Sub-cluster B (N>=7, 'deep'):    {large}")

    # Intra-cluster GED
    def mean_ged(members):
        if len(members) < 2:
            return 0.0
        geds = [ged_matrix[(a, b)] for a, b in combinations(members, 2)]
        return np.mean(geds)

    intra_small = mean_ged(small)
    intra_large = mean_ged(large)
    inter_geds = [ged_matrix[(a, b)] for a in small for b in large]
    inter = np.mean(inter_geds) if inter_geds else 0.0

    print(f"\n  Intra-cluster A (compact) mean GED: {intra_small:.4f}")
    print(f"  Intra-cluster B (deep) mean GED:    {intra_large:.4f}")
    print(f"  Inter-cluster mean GED:             {inter:.4f}")

    min_intra = min(intra_small, intra_large) if (intra_small > 0 and intra_large > 0) else max(intra_small, intra_large)
    sub_sep = inter / min_intra if min_intra > 0 else float("inf")
    print(f"  Sub-cluster separation ratio:       {sub_sep:.4f}x")

    # Silhouette-style score
    silhouettes = []
    all_members = small + large
    for member in all_members:
        own_cluster = small if member in small else large
        other_cluster = large if member in small else small

        if len(own_cluster) > 1:
            a_i = np.mean([ged_matrix[(member, m)] for m in own_cluster if m != member])
        else:
            a_i = 0.0

        if other_cluster:
            b_i = np.mean([ged_matrix[(member, m)] for m in other_cluster])
        else:
            b_i = 0.0

        if max(a_i, b_i) > 0:
            s_i = (b_i - a_i) / max(a_i, b_i)
        else:
            s_i = 0.0
        silhouettes.append(s_i)

    mean_silhouette = np.mean(silhouettes)
    print(f"\n  Mean silhouette score: {mean_silhouette:.4f}")
    print(f"  (>0.5 = strong clustering, >0.25 = moderate, <0.25 = weak)")
    _sep()

    return {
        "small_cluster": small,
        "large_cluster": large,
        "intra_small": round(intra_small, 4),
        "intra_large": round(intra_large, 4),
        "inter_cluster": round(inter, 4),
        "sub_separation_ratio": round(sub_sep, 4),
        "mean_silhouette": round(mean_silhouette, 4),
        "silhouettes": {m: round(s, 4) for m, s in zip(all_members, silhouettes)},
    }


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")

    print()
    _sep("=")
    print("  WP 1.3 -- Sensitivity Analysis & Sub-Clustering")
    _sep("=")

    # Load primary schemas
    schemas = load_all_schemas(SCHEMAS_DIR)
    primary_graphs = {name: G for name, (G, _) in schemas.items()}

    # -----------------------------------------------------------------------
    # ANALYSIS 1: Primary corpus family classification (already done by pipeline,
    # but we recompute here for the sensitivity comparison baseline)
    # -----------------------------------------------------------------------
    print("\n  BASELINE: Primary Corpus (14 schemas)")
    _sep()

    # Load pre-computed GED matrix if available
    ged_path = os.path.join(OUTPUTS_DIR, "similarity_matrix", "structural_ged.json")
    if os.path.exists(ged_path):
        with open(ged_path, "r") as f:
            ged_raw = json.load(f)
        # Convert "A vs B" keyed dict to tuple-keyed dict
        primary_ged = {}
        names = sorted(primary_graphs.keys())
        for key, val_dict in ged_raw.items():
            parts = key.split(" vs ")
            if len(parts) == 2:
                a, b = parts
                ged_val = val_dict.get("structural_ged", 0.0)
                primary_ged[(a, b)] = ged_val
                primary_ged[(b, a)] = ged_val
        # Self-distances
        for name in names:
            primary_ged[(name, name)] = 0.0
        print("  Loaded pre-computed GED matrix.")
    else:
        print("  Computing pairwise GED (may take a few minutes)...")
        primary_ged = pairwise_ged(primary_graphs)

    primary_families = classify_families(primary_graphs)
    primary_stats = family_stats(primary_families, primary_ged, list(primary_graphs.keys()))

    print(f"  Linear chains ({primary_stats['n_chains']}): {', '.join(sorted(primary_families['linear_chain']))}")
    print(f"  Branching trees ({primary_stats['n_branches']}): {', '.join(sorted(primary_families['branching_tree']))}")
    print(f"  Intra-chain GED:  {primary_stats['intra_chain']}")
    print(f"  Intra-branch GED: {primary_stats['intra_branch']}")
    print(f"  Inter-family GED: {primary_stats['inter_family']}")
    print(f"  Separation ratio: {primary_stats['separation_ratio']}x")

    # -----------------------------------------------------------------------
    # ANALYSIS 2: Suhrawardi branching alternative
    # -----------------------------------------------------------------------
    print("\n\n  SENSITIVITY 1: Suhrawardi Branching Alternative")
    _sep()
    print("  Reclassifying ishraq_illuminationist from linear chain to branching tree.")
    print("  (Victorial Lights gets out-degree 2: -> Lords of Species AND -> Accidental Lights)")

    alt_ishraq = build_ishraq_branching(schemas)
    alt1_graphs = dict(primary_graphs)
    alt1_graphs["ishraq_illuminationist"] = alt_ishraq

    print("  Computing GED for affected pairs...")
    # Only recompute pairs involving Ishraq
    alt1_ged = dict(primary_ged)
    for other in alt1_graphs:
        if other == "ishraq_illuminationist":
            continue
        ged_val = nx.graph_edit_distance(alt_ishraq, alt1_graphs[other], timeout=GED_TIMEOUT)
        if ged_val is None:
            ged_val = float("inf")
        alt1_ged[("ishraq_illuminationist", other)] = ged_val
        alt1_ged[(other, "ishraq_illuminationist")] = ged_val

    alt1_families = classify_families(alt1_graphs)
    alt1_stats = family_stats(alt1_families, alt1_ged, list(alt1_graphs.keys()))

    print(f"  Linear chains ({alt1_stats['n_chains']}): {', '.join(sorted(alt1_families['linear_chain']))}")
    print(f"  Branching trees ({alt1_stats['n_branches']}): {', '.join(sorted(alt1_families['branching_tree']))}")
    print(f"  Intra-chain GED:  {alt1_stats['intra_chain']}")
    print(f"  Intra-branch GED: {alt1_stats['intra_branch']}")
    print(f"  Inter-family GED: {alt1_stats['inter_family']}")
    print(f"  Separation ratio: {alt1_stats['separation_ratio']}x")

    # Key isomorphism check
    ishraq_samkhya = alt1_ged.get(("ishraq_illuminationist", "samkhya"), "N/A")
    print(f"\n  Ishraq-Samkhya GED under branching: {ishraq_samkhya}")
    print(f"  (Was 0.0 under primary linear encoding)")
    if ishraq_samkhya != 0.0:
        print("  --> Ishraq-Samkhya isomorphism DISSOLVED by branching alternative.")
    else:
        print("  --> Ishraq-Samkhya isomorphism PRESERVED even under branching.")

    # -----------------------------------------------------------------------
    # ANALYSIS 3: Zurvanite Bundahishn alternative
    # -----------------------------------------------------------------------
    print("\n\n  SENSITIVITY 2: Zurvanite Bundahishn Alternative")
    _sep()
    print("  Adding Zurvan at apex; bifurcating to Ohrmazd + Ahriman.")
    print("  Reclassifying bundahishn_zoroastrian from linear chain to branching tree.")

    alt_bundahishn = build_zurvanite_bundahishn(schemas)
    alt2_graphs = dict(primary_graphs)
    alt2_graphs["bundahishn_zoroastrian"] = alt_bundahishn

    print("  Computing GED for affected pairs...")
    alt2_ged = dict(primary_ged)
    for other in alt2_graphs:
        if other == "bundahishn_zoroastrian":
            continue
        ged_val = nx.graph_edit_distance(alt_bundahishn, alt2_graphs[other], timeout=GED_TIMEOUT)
        if ged_val is None:
            ged_val = float("inf")
        alt2_ged[("bundahishn_zoroastrian", other)] = ged_val
        alt2_ged[(other, "bundahishn_zoroastrian")] = ged_val

    alt2_families = classify_families(alt2_graphs)
    alt2_stats = family_stats(alt2_families, alt2_ged, list(alt2_graphs.keys()))

    print(f"  Linear chains ({alt2_stats['n_chains']}): {', '.join(sorted(alt2_families['linear_chain']))}")
    print(f"  Branching trees ({alt2_stats['n_branches']}): {', '.join(sorted(alt2_families['branching_tree']))}")
    print(f"  Intra-chain GED:  {alt2_stats['intra_chain']}")
    print(f"  Intra-branch GED: {alt2_stats['intra_branch']}")
    print(f"  Inter-family GED: {alt2_stats['inter_family']}")
    print(f"  Separation ratio: {alt2_stats['separation_ratio']}x")

    # Key comparison
    bund_ishraq = alt2_ged.get(("bundahishn_zoroastrian", "ishraq_illuminationist"), "N/A")
    print(f"\n  Zurvanite Bundahishn vs Ishraq GED: {bund_ishraq}")
    print(f"  (Was 2.0 under primary encoding)")

    # -----------------------------------------------------------------------
    # ANALYSIS 4: Sub-clustering within linear-chain family
    # -----------------------------------------------------------------------
    subcluster_results = subclustering_analysis(schemas, primary_ged)

    # -----------------------------------------------------------------------
    # ANALYSIS 5: Summary comparison table
    # -----------------------------------------------------------------------
    print("\n\n  SENSITIVITY COMPARISON TABLE")
    _sep("=")
    print(f"  {'Scenario':<35} {'Chains':>6} {'Branch':>6} {'Intra-C':>8} {'Intra-B':>8} {'Inter':>8} {'Sep':>8}")
    _sep()
    rows = [
        ("Primary (14 schemas)", primary_stats),
        ("Alt 1: Ishraq branching", alt1_stats),
        ("Alt 2: Zurvanite Bundahishn", alt2_stats),
    ]
    for label, s in rows:
        print(f"  {label:<35} {s['n_chains']:>6} {s['n_branches']:>6} {s['intra_chain']:>8.4f} {s['intra_branch']:>8.4f} {s['inter_family']:>8.4f} {s['separation_ratio']:>7.4f}x")
    _sep("=")

    # -----------------------------------------------------------------------
    # Save results
    # -----------------------------------------------------------------------
    results = {
        "primary": primary_stats,
        "primary_families": primary_families,
        "alt1_ishraq_branching": alt1_stats,
        "alt1_families": alt1_families,
        "alt1_ishraq_samkhya_ged": ishraq_samkhya,
        "alt2_zurvanite": alt2_stats,
        "alt2_families": alt2_families,
        "alt2_bundahishn_ishraq_ged": bund_ishraq,
        "subclustering": subcluster_results,
    }

    out_path = os.path.join(OUTPUTS_DIR, "sensitivity_results.json")
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2, default=str)
    print(f"\n  Results saved to: {out_path}")
    _sep("=")
    print()


if __name__ == "__main__":
    main()
