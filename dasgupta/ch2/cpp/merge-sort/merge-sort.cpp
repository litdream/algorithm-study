#include "merge-sort.hpp"

using std::vector;

vector<int>
merge(const vector<int>& left, const vector<int>& right) {

    vector<int> result;
    result.reserve(left.size() + right.size());

    size_t i = 0; // left-half index
    size_t j = 0; // right-half index

    // Select minimum of two, and build result vector<int>
    while (i < left.size() && j < right.size())
        left[i] <= right[j] ?
            result.push_back(left[i++]) :
            result.push_back(right[j++]);

    // Handle the remainings.
    while (i < left.size()) 
        result.push_back(left[i++]);
    while (j < right.size()) 
        result.push_back(right[j++]);

    return result;    // will use move-semantics?
}

vector<int> merge_sort(const vector<int>& nums) {

    // Special Case.
    if (nums.size() <= 1) {
        return nums;
    }

    size_t mid = nums.size() / 2;

    // left = nums[:mid]
    std::vector<int> left;
    for (auto it = nums.begin(); it != nums.begin() + mid; ++it)
        left.push_back(*it);

    // right = nums[mid+1:]
    std::vector<int> right;
    for (auto it = nums.begin() + mid; it != nums.end(); ++it)
        right.push_back(*it);
    
    vector<int> left_sorted = merge_sort(left);
    vector<int> right_sorted = merge_sort(right);

    // Recursive Merge and Return.
    return merge(left_sorted, right_sorted);
}
