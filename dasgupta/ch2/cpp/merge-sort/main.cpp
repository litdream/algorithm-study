// Gemini generated the test driver.

#include "merge-sort.hpp"
#include <iostream>
#include <vector>
#include <string>
#include <sstream>

/**
 * @brief Helper function to print the contents of an integer vector.
 * @param vec The vector to print.
 * @return std::string A formatted string representation of the vector.
 */
std::string vector_to_string(const std::vector<int>& vec) {
    std::stringstream ss;
    ss << "[";
    for (size_t i = 0; i < vec.size(); ++i) {
        ss << vec[i];
        if (i < vec.size() - 1) {
            ss << ", ";
        }
    }
    ss << "]";
    return ss.str();
}

/**
 * @brief Runs a single test case for the integer-based merge_sort function.
 * @param name The name of the test case.
 * @param input The input vector.
 * @param expected The expected sorted output vector.
 */
void run_int_test(const std::string& name, const std::vector<int>& input, const std::vector<int>& expected) {
    std::vector<int> sorted_result = merge_sort(input);
    
    std::string input_str = vector_to_string(input);
    std::string result_str = vector_to_string(sorted_result);
    std::string expected_str = vector_to_string(expected);

    bool success = (sorted_result == expected);

    std::cout << "--- Test: " << name << " ---\n";
    std::cout << "Input:    " << input_str << "\n";
    std::cout << "Result:   " << result_str << "\n";
    std::cout << "Expected: " << expected_str << "\n";
    std::cout << (success ? "Status:   PASS\n" : "Status:   FAIL <------------------\n");
    std::cout << "\n";
}

int main() {
    std::cout << "### Merge Sort (Integer Only) C++ Implementation Test Driver ###\n\n";

    // Test Case 1: Standard case (as per Python example)
    run_int_test("Standard Integer Sort", 
                   {5, 2, 8, 1, 9}, 
                   {1, 2, 5, 8, 9});

    // Test Case 2: Empty list
    run_int_test("Empty List", 
                   {}, 
                   {});

    // Test Case 3: Single element
    run_int_test("Single Element", 
                   {42}, 
                   {42});

    // Test Case 4: Already sorted
    run_int_test("Already Sorted", 
                   {1, 2, 3, 4, 5}, 
                   {1, 2, 3, 4, 5});

    // Test Case 5: Reverse sorted
    run_int_test("Reverse Sorted", 
                   {9, 7, 5, 3, 1}, 
                   {1, 3, 5, 7, 9});
                   
    // Test Case 6: Duplicate elements
    run_int_test("With Duplicates", 
                   {3, 1, 2, 3, 0}, 
                   {0, 1, 2, 3, 3});
                   
    // Test Case 7: Large vector
    run_int_test("Large Random-ish Vector",
                   {50, 10, 40, 20, 30, 60, 0},
                   {0, 10, 20, 30, 40, 50, 60});

    return 0;
}
