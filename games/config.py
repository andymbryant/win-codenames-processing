import os
# Number to multiply the average distance threshold for clustering
# Higher numbers result in less clusters of a larger clusters
AVG_DIST_MULT = 1.15

# Number to multiply the rank
# Higher numbers favor the top words and penalize the lower words (a lower rank number is better)
RANK_MULT = 1.25

# Column order for ranking in the first sorting algorithm (when candidate dfs are first made)
PRIMARY_SORT_BY_COLUMNS = ['goodness', 'bad_minimax', 'frequency', 'neutrals_minimax']
PRIMARY_SORT_ASCENDING = [False for i in range(len(PRIMARY_SORT_BY_COLUMNS))]

# Column order for ranking in the secondary sorting algorithm (when candidate dfs are merged)
SECONDARY_SORT_BY_COLUMNS = ['rank', 'variance', 'goodness']
SECONDARY_SORT_ASCENDING = [True,False,False]

HIGH_SIZE = 2000
LOW_SIZE = 200

# Assassin cutoff
ASSASSIN_CUTOFF = 0.78

ID_LENGTH = 8

VECTORS_OUTPUT_PATH = vectors_output_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'vectors/output'))