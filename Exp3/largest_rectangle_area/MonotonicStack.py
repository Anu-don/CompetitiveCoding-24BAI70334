def largestRectangleArea(heights):
    stack = []
    max_area = 0
    heights.append(0)

    for i in range(len(heights)):
        while stack and heights[stack[-1]] > heights[i]:
            height = heights[stack.pop()]

            if stack:
                width = i - stack[-1] - 1
            else:
                width = i

            max_area = max(max_area, height * width)

        stack.append(i)

    heights.pop()
    return max_area


n = int(input("Enter number of bars: "))
heights = list(map(int, input("Enter heights: ").split()))

print(largestRectangleArea(heights))