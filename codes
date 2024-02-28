# Define all 4-fold codons， which Kd less than 130 uM
bases = ['U', 'C', 'A', 'G']
codon = [
    [Ser, Leu, Pro, Arg, Thr, Val, Ala, Gly]
    for Ser in ["UCC"]
    for Leu in ["CUC"]
    for Pro in ["CCC", "CCA", "CCG"]
    for Arg in [f"CG{n}" for n in bases]
    for Thr in ["ACC", "ACG"]
    for Val in ["GUC"]
    for Ala in [f"GC{n}" for n in bases]
    for Gly in ["GGU", "GGC", "GGA"]
]


# convert codon to anticodon, with WC and Wobble base pair
def transform_triplet(triplet):
    transformed_triplet = ""
    for letter in triplet:
        if letter == "U":
            transformed_triplet = "A" + transformed_triplet
        elif letter == "A":
            transformed_triplet = "U" + transformed_triplet
        elif letter == "G":
            transformed_triplet = "C" + transformed_triplet
        elif letter == "C":
            transformed_triplet = "G" + transformed_triplet
    return transformed_triplet


def UGtransform_triplet(triplet):
    transformed_triplet = ""
    for letter in triplet:
        if letter == "U":
            transformed_triplet = "G" + transformed_triplet
        elif letter == "A":
            transformed_triplet = "U" + transformed_triplet
        elif letter == "G":
            transformed_triplet = "C" + transformed_triplet
        elif letter == "C":
            transformed_triplet = "G" + transformed_triplet
    return transformed_triplet


def GUtransform_triplet(triplet):
    transformed_triplet = ""
    for letter in triplet:
        if letter == "U":
            transformed_triplet = "A" + transformed_triplet
        elif letter == "A":
            transformed_triplet = "U" + transformed_triplet
        elif letter == "G":
            transformed_triplet = "U" + transformed_triplet
        elif letter == "C":
            transformed_triplet = "G" + transformed_triplet
    return transformed_triplet


def GUUGtransform_triplet(triplet):
    transformed_triplet = ""
    for letter in triplet:
        if letter == "U":
            transformed_triplet = "G" + transformed_triplet
        elif letter == "A":
            transformed_triplet = "U" + transformed_triplet
        elif letter == "G":
            transformed_triplet = "U" + transformed_triplet
        elif letter == "C":
            transformed_triplet = "G" + transformed_triplet
    return transformed_triplet


def UG1transform_triplet(triplet):
    transformed_triplet = ""
    u_replaced = False
    for letter in triplet:
        if letter == "U" and not u_replaced:
            transformed_triplet = "G" + transformed_triplet
            u_replaced = True
        elif letter == "U" and u_replaced:
            transformed_triplet = "A" + transformed_triplet
        elif letter == "A":
            transformed_triplet = "U" + transformed_triplet
        elif letter == "G":
            transformed_triplet = "C" + transformed_triplet
        elif letter == "C":
            transformed_triplet = "G" + transformed_triplet
    return transformed_triplet


def GU1transform_triplet(triplet):
    transformed_triplet = ""
    g_replaced = False
    for letter in triplet:
        if letter == "G" and not g_replaced:
            transformed_triplet = "U" + transformed_triplet
            g_replaced = True
        elif letter == "G" and g_replaced:
            transformed_triplet = "C" + transformed_triplet
        elif letter == "A":
            transformed_triplet = "U" + transformed_triplet
        elif letter == "U":
            transformed_triplet = "A" + transformed_triplet
        elif letter == "C":
            transformed_triplet = "G" + transformed_triplet
    return transformed_triplet


anticodon = []

# convert codon to anticodon
for codon_set in codon:
    transformed_set = [transform_triplet(triplet) for triplet in codon_set]
    anticodon.append(transformed_set)

new_anticodon = []

# select anticodon sets
for anticodon_set in anticodon:
    # mark if should be kept
    keep_set = True
    # convert each anticodon to kissed anticodon
    transformed_triplets = [transform_triplet(triplet) for triplet in anticodon_set]
    # check if kissed anticodon in the anticodon set
    for triplet in transformed_triplets:
        if triplet in anticodon_set:
            keep_set = False
            break
    transformed_triplets = [UGtransform_triplet(triplet) for triplet in anticodon_set]
    for triplet in transformed_triplets:
        if triplet in anticodon_set:
            keep_set = False
            break
    transformed_triplets = [GUtransform_triplet(triplet) for triplet in anticodon_set]
    for triplet in transformed_triplets:
        if triplet in anticodon_set:
            keep_set = False
            break
    transformed_triplets = [GUUGtransform_triplet(triplet) for triplet in anticodon_set]
    for triplet in transformed_triplets:
        if triplet in anticodon_set:
            keep_set = False
            break
    transformed_triplets = [UG1transform_triplet(triplet) for triplet in anticodon_set]
    for triplet in transformed_triplets:
        if triplet in anticodon_set:
            keep_set = False
            break
    transformed_triplets = [GU1transform_triplet(triplet) for triplet in anticodon_set]
    for triplet in transformed_triplets:
        if triplet in anticodon_set:
            keep_set = False
            break

    if keep_set:
        new_anticodon.append(anticodon_set)

new_codon = []

# convert new anticodon set to new codon set
for new_anticodon_set in new_anticodon:
    transformed_set = [transform_triplet(triplet) for triplet in new_anticodon_set]
    new_codon.append(transformed_set)

# output new codon set
for i, a in enumerate(new_codon):
    print(f"new codon set {i + 1}: {a}")

from itertools import product


def filter_mrna(i, new_codon):
    mrna = [''.join(p) for p in product(bases, repeat=i)]
    # Initialize list A with each sublist in new_codon
    for index, new_codon_set in enumerate(new_codon):
        # Filter strings based on conditions
        mrna_filtered_1 = [s for s in mrna if s[:3] in new_codon_set and s[3:6] in new_codon_set]
        mrna_filtered_2 = [s for s in mrna_filtered_1 if s[1:4] not in new_codon_set and s[2:5] not in new_codon_set]
        # Print the remaining count
        print(f"i={i}, for new set {index + 1}, mRNA {len(mrna_filtered_2)}")


filter_mrna(6, new_codon)


def filter_mrna7(new_codon):
    mrna = [''.join(p) for p in product(bases, repeat=7)]
    # Initialize list A with each sublist in new_codon
    for index, new_codon_set in enumerate(new_codon):
        # Filter strings based on conditions
        mrna_filtered_1 = [s for s in mrna if s[:3] in new_codon_set and s[3:6] in new_codon_set]
        mrna_filtered_2 = [s for s in mrna_filtered_1 if
                           s[1:4] not in new_codon_set and s[2:5] not in new_codon_set and s[4:] not in new_codon_set]
        mrna_filtered_3 = [s for s in mrna if s[1:4] in new_codon_set and s[4:] in new_codon_set]
        mrna_filtered_4 = [s for s in mrna_filtered_3 if
                           s[:3] not in new_codon_set and s[2:5] not in new_codon_set and s[3:6] not in new_codon_set]
        # Print the remaining count
        mrna_filtered = mrna_filtered_2 + mrna_filtered_4
        print(f"i=7, for new set {index + 1}, mRNA {len(mrna_filtered)}")


filter_mrna7(new_codon)


def filter_mrna8(new_codon):
    mrna = [''.join(p) for p in product(bases, repeat=8)]
    # Initialize list A with each sublist in new_codon
    for index, new_codon_set in enumerate(new_codon):
        mrna_filtered_1 = [s for s in mrna if s[0:3] in new_codon_set and s[3:6] in new_codon_set]
        mrna_filtered_2 = [s for s in mrna_filtered_1 if
                           s[1:4] not in new_codon_set and s[2:5] not in new_codon_set and s[
                                                                                           4:7] not in new_codon_set and s[
                                                                                                                         5:8] not in new_codon_set]
        mrna_filtered_3 = [s for s in mrna if s[1:4] in new_codon_set and s[4:7] in new_codon_set]
        mrna_filtered_4 = [s for s in mrna_filtered_3 if
                           s[0:3] not in new_codon_set and s[2:5] not in new_codon_set and s[
                                                                                           3:6] not in new_codon_set and s[
                                                                                                                         5:8] not in new_codon_set]
        mrna_filtered_5 = [s for s in mrna if s[2:5] in new_codon_set and s[5:8] in new_codon_set]
        mrna_filtered_6 = [s for s in mrna_filtered_5 if
                           s[0:3] not in new_codon_set and s[1:4] not in new_codon_set and s[
                                                                                           3:6] not in new_codon_set and s[
                                                                                                                         4:7] not in new_codon_set]
        mrna_filtered = mrna_filtered_2 + mrna_filtered_4 + mrna_filtered_6
        print(f"i=8, for new set {index + 1}, mRNA {len(mrna_filtered)}")


filter_mrna8(new_codon)


def filter_mrna9(new_codon):
    mrna = [''.join(p) for p in product(bases, repeat=9)]
    # Initialize list A with each sublist in new_codon
    for index, new_codon_set in enumerate(new_codon):
        # Filter strings based on conditions
        mrna_filtered_1 = [s for s in mrna if
                           s[0:3] in new_codon_set and s[3:6] in new_codon_set and s[6:9] in new_codon_set]
        mrna_filtered_2 = [s for s in mrna_filtered_1 if
                           s[1:4] not in new_codon_set and s[2:5] not in new_codon_set and s[
                                                                                           4:7] not in new_codon_set and s[
                                                                                                                         5:8] not in new_codon_set]
        # Print the remaining count
        print(f"i=9, for new set {index + 1}, mRNA {len(mrna_filtered_2)}")


filter_mrna9(new_codon)


def filter_mrna10(new_codon):
    mrna = [''.join(p) for p in product(bases, repeat=10)]
    # Initialize list A with each sublist in new_codon
    for index, new_codon_set in enumerate(new_codon):
        # Filter strings based on conditions
        mrna_filtered_1 = [s for s in mrna if
                           s[0:3] in new_codon_set and s[3:6] in new_codon_set and s[6:9] in new_codon_set]
        mrna_filtered_2 = [s for s in mrna_filtered_1 if
                           s[1:4] not in new_codon_set and s[2:5] not in new_codon_set and s[
                                                                                           4:7] not in new_codon_set and s[
                                                                                                                         5:8] not in new_codon_set and s[
                                                                                                                                                       7:10] not in new_codon_set]  # Print the remaining count
        mrna_filtered_3 = [s for s in mrna if
                           s[1:4] in new_codon_set and s[4:7] in new_codon_set and s[7:10] in new_codon_set]
        mrna_filtered_4 = [s for s in mrna_filtered_3 if
                           s[0:3] not in new_codon_set and s[2:5] not in new_codon_set and s[
                                                                                           3:6] not in new_codon_set and s[
                                                                                                                         5:8] not in new_codon_set and s[
                                                                                                                                                       6:9] not in new_codon_set]  # Print the remaining count

        mrna_filtered = mrna_filtered_2 + mrna_filtered_4
        print(f"i=10, for new set {index + 1}, mRNA {len(mrna_filtered)}")


filter_mrna10(new_codon)


def filter_mrna11(new_codon):
    mrna = [''.join(p) for p in product(bases, repeat=11)]
    # Initialize list A with each sublist in new_codon
    for index, new_codon_set in enumerate(new_codon):
        # Filter strings based on conditions
        mrna_filtered_1 = [s for s in mrna if
                           s[0:3] in new_codon_set and s[3:6] in new_codon_set and s[6:9] in new_codon_set]
        mrna_filtered_2 = [s for s in mrna_filtered_1 if
                           s[1:4] not in new_codon_set and s[2:5] not in new_codon_set and s[
                                                                                           4:7] not in new_codon_set and s[
                                                                                                                         5:8] not in new_codon_set and s[
                                                                                                                                                       7:10] not in new_codon_set and s[
                                                                                                                                                                                      8:11] not in new_codon_set]  # Print the remaining count
        mrna_filtered_3 = [s for s in mrna if
                           s[1:4] in new_codon_set and s[4:7] in new_codon_set and s[7:10] in new_codon_set]
        mrna_filtered_4 = [s for s in mrna_filtered_3 if
                           s[0:3] not in new_codon_set and s[2:5] not in new_codon_set and s[
                                                                                           3:6] not in new_codon_set and s[
                                                                                                                         5:8] not in new_codon_set and s[
                                                                                                                                                       6:9] not in new_codon_set and s[
                                                                                                                                                                                     8:11] not in new_codon_set]  # Print the remaining count
        mrna_filtered_5 = [s for s in mrna if
                           s[2:5] in new_codon_set and s[5:8] in new_codon_set and s[8:11] in new_codon_set]
        mrna_filtered_6 = [s for s in mrna_filtered_5 if
                           s[0:3] not in new_codon_set and s[1:4] not in new_codon_set and s[
                                                                                           3:6] not in new_codon_set and s[
                                                                                                                         4:7] not in new_codon_set and s[
                                                                                                                                                       6:9] not in new_codon_set and s[
                                                                                                                                                                                     7:10] not in new_codon_set]  # Print the remaining count

        mrna_filtered = mrna_filtered_2 + mrna_filtered_4 + mrna_filtered_6
        print(f"i=11, for new set {index + 1}, mRNA {len(mrna_filtered)}")


filter_mrna11(new_codon)
