#!/usr/bin/env python3
"""
K Most Frequent Words Problem

This script finds the k most frequent words in a file using a min heap approach.
The min heap maintains exactly k elements, keeping track of the top k frequent words.

Usage: python3 count_words.py [filename] [k]
Example: python3 count_words.py words.txt 5
"""

import heapq
import sys
import re
from collections import Counter


def clean_word(word):
    """Clean word by removing punctuation and converting to lowercase"""
    # Remove punctuation and convert to lowercase
    cleaned = re.sub(r'[^a-zA-Z]', '', word).lower()
    return cleaned


def read_words_from_file(filename):
    """Read and clean words from file"""
    words = []
    
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            for line in file:
                # Split line into words and clean each word
                line_words = line.strip().split()
                for word in line_words:
                    cleaned_word = clean_word(word)
                    if cleaned_word:  # Only add non-empty words
                        words.append(cleaned_word)
        
        print(f"Successfully read {len(words)} words from {filename}")
        return words
    
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found")
        return []
    except Exception as e:
        print(f"Error reading file: {e}")
        return []


def count_word_frequencies(words):
    """Count frequency of each word"""
    return Counter(words)


def k_most_frequent_words_minheap(word_freq, k):
    """
    Find k most frequent words using min heap approach
    
    Algorithm:
    1. Use a min heap of size k
    2. For each word-frequency pair:
       - If heap size < k, add the pair
       - If current frequency > minimum frequency in heap, replace minimum
    3. Return all elements in heap (these are the k most frequent)
    
    Time Complexity: O(n log k) where n is number of unique words
    Space Complexity: O(k)
    """
    if k <= 0:
        return []
    
    min_heap = []
    
    for word, freq in word_freq.items():
        if len(min_heap) < k:
            # Heap not full, add current word
            heapq.heappush(min_heap, (freq, word))
        elif freq > min_heap[0][0]:
            # Current frequency is higher than minimum in heap
            # Replace the minimum
            heapq.heapreplace(min_heap, (freq, word))
    
    # Extract results and sort by frequency (descending)
    result = []
    while min_heap:
        freq, word = heapq.heappop(min_heap)
        result.append((word, freq))
    
    # Reverse to get highest frequency first
    result.reverse()
    return result

