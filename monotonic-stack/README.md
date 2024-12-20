# Monotonic Stack
data structure that maintains its elements in a sorted order, either strictly increasing or strictly decreasing. This is useful in problems where 
we have to find the next smallest or next largest element or previous smallest or previous largest
- Monotonically Increasing
  - The elements in the stack are kept in non-decreasing order from bottom to top.
  - This means that when you process a new element, you pop from the stack as long as the top of the stack is greater than (or sometimes greater than or equal to) the new element before pushing the new one.

- Monotonically Decreasing Stack:
  - The elements in the stack are kept in non-increasing order from bottom to top.
  - In this scenario, when a new element is processed, you pop from the stack while the top of the stack is smaller than (or smaller than or equal to) the new element.

## General Pattern in Using a Monotonic Stack:
- Initialize an empty stack.
- Traverse the list of elements:
  - While the stack is not empty and the current element breaks the monotonic property (e.g., if it’s larger than the stack top and we want a decreasing stack), pop from the stack.
  - Use the popping action to derive a solution component (e.g., next greater element, area calculation, waiting days, etc.).
  - Push the current element (or its index) onto the stack to maintain the monotonic order.
- After the traversal, any elements left in the stack represent positions or values that could not find a "next" element of interest. Handle them accordingly if needed.
