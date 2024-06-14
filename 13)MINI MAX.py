import math

def minimax(curDepth, nodeIndex, maxTurn, scores, targetDepth):
    if curDepth == targetDepth:
        return scores[nodeIndex]
    
    if maxTurn:
        return max(minimax(curDepth + 1, nodeIndex * 2, False, scores, targetDepth),
                   minimax(curDepth + 1, nodeIndex * 2 + 1, False, scores, targetDepth))
    else:
        return min(minimax(curDepth + 1, nodeIndex * 2, True, scores, targetDepth),
                   minimax(curDepth + 1, nodeIndex * 2 + 1, True, scores, targetDepth))

# Scores for the leaves of the tree
scores = [3, 5, 2, 9, 12, 5, 23, 23]

# Calculate the depth of the tree
treeDepth = int(math.log2(len(scores)))

print("The optimal value is:", end=" ")
print(minimax(0, 0, True, scores, treeDepth))

